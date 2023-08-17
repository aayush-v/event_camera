# Copyright (c) Prophesee S.A. - All Rights Reserved
#
# Subject to Prophesee Metavision Licensing Terms and Conditions ("License T&C's").
# You may not use this file except in compliance with these License T&C's.
# A copy of these License T&C's is located in the "licensing" folder accompanying this file.

"""
Sample code that demonstrates how to visualizes live data (CD events only) from a Prophesee sensor and estimates the event rate
"""

"""
Steps to use:
    1. Choose which filter to use and mention that in the --s-filter. This will make the raw file run with that filter from the start, instead of the default None.
    2. Custom values for the filter can be used by passing them in the previously given args.
    2. Make sure --csv-save arg is passed as True or else the conversion to csv will not take place.
    3. Add the -output-path (-o) for the .csv file with filtered events.
    4. Use metavision_evt2_raw_file_encoder to convert csv file to evt2 (csv to evt3 does not exist)
"""

from metavision_core.event_io import EventsIterator, LiveReplayEventsIterator, is_live_camera
from metavision_sdk_core import PeriodicFrameGenerationAlgorithm
from metavision_sdk_base import EventCDBuffer
from metavision_sdk_cv import AntiFlickerAlgorithm, SpatioTemporalContrastAlgorithm, ActivityNoiseFilterAlgorithm
from metavision_sdk_ui import EventLoop, BaseWindow, MTWindow, UIKeyEvent, UIAction
import argparse
import os
import cv2
from tqdm import tqdm

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Metavision Data Rate Sample.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '-i', '--input-raw-file', dest='input_path', default="",
        help="Path to input RAW or DAT file. If not specified, the live stream of the first available camera is used. "
             "If it's a camera serial number, it will try to open that camera instead.")

    parser.add_argument(
        '-t', '--delta-t', dest='delta_t', type=int, default=1e3,
        help="Time interval used to accumulate events")

    parser.add_argument(
        '--fps', dest='fps', type=float, default=50.0,
        help="Display FPS")

    parser.add_argument(
        '--flicker-dt', dest='time_window_flicker', type=int, default=15000,
        help='Time interval threshold for AntiFlickerAlgorithm (in us)'
    )

    parser.add_argument(
        '--st-dt', dest='time_window_stc', type=int, default=15000,
        help='Time interval threshold for SpatioTemporalContrastAlgorithm (in us)'
    )

    parser.add_argument(
        '--activity-dt', dest='time_window_activity', type=int, default=15000,
        help='Time interval threshold for ActivityNoiseFilterAlgorithm (in us)'
    )

    parser.add_argument(
        '--filter-length', type=int, default=7,
        help='Number of successive activations to detect a blinking pattern for AntiFlickerAlgorithm'
    )

    parser.add_argument(
        '--min-freq', type=int, default=70,
        help='Minimum frequency for AntiFlickerAlgorithm'
    )


    parser.add_argument(
        '--max-freq', type=int, default=130,
        help='Maximum frequency for AntiFlickerAlgorithm'
    )

    parser.add_argument(
        '--cut-trail', type=bool, default=True,
        help='whether to cut off all the following events until a change of polarity is detected'
    )

    parser.add_argument(
        '--csv-save', dest='save',type=bool, default=False,
        help='whether to save file as CSV'
    )

    parser.add_argument(
        '--o', dest='out_path', default="output.csv",
        help='output_file path'
    )

    parser.add_argument(
        '--s-filter', dest='filter_save_type', default=None,
        help='output_file path'
    )


    args = parser.parse_args()
    return args


class AntiFlickerSTCFilter(object):
    """
    Apply AFK and STC filter consecutively

    Args:
        width (int): camera width
        height (int): camera height
        time_window_flicker (int): Time interval threshold for AntiFlickerAlgorithm in us
        time_window_stc (int): Time interval threshold for SpatioTemporalContrastAlgorithm in us
        filter_length (int): Number of successive activations to detect a blinking pattern for AntiFlickerAlgorithm
        min_freq (int) : Minimum frequency for AntiFlickerAlgorithm
        max_freq (int): Maximum frequency for AntiFlickerAlgorithm
        cut_trail (bool): whether to cut off all the following events until a change of polarity is detected.

    """

    def __init__(self, width, height, time_window_flicker=15000, time_window_stc=10000,
                 filter_length=7, min_freq=70, max_freq=130, cut_trail=True):
        self.anti_flicker = AntiFlickerAlgorithm(width, height, filter_length, min_freq, max_freq, time_window_flicker)
        self.spatio_temporal_filter = SpatioTemporalContrastAlgorithm(width, height, time_window_stc, cut_trail)
        self.event_buffer = EventCDBuffer()

    def process_events(self, evs, st_buffer):
        self.anti_flicker.process_events(evs, self.event_buffer)
        self.spatio_temporal_filter.process_events(self.event_buffer, st_buffer)


def main():
    """ Main """
    args = parse_args()

    # Show different keyboard options to do noise filtering
    print("Available keyboard options:\n"
          "     -C: Filter events using Anti-Flicker & Spatio-Temporal Algorithm\n"
          "     -F: Filter events using Anti-Flicker Algorithm\n"
          "     -S: Filter events using Spatio-Temporal-Contrast Filter Algorithm\n"
          "     -A: Filter events using ActivityNoise-Filter Algorithm\n"
          "     -E: Show all events\n"
          "     -Q/Escape: Quit the application\n")

    # Events iterator on Camera or RAW file
    mv_iterator = EventsIterator(input_path=args.input_path, delta_t=args.delta_t)
    height, width = mv_iterator.get_size()  # Camera Geometry

    # Initiate the filters
    my_filters = {'activity': ActivityNoiseFilterAlgorithm(width, height, args.time_window_activity),
                  'stc': SpatioTemporalContrastAlgorithm(width, height, args.time_window_stc, args.cut_trail),
                  'anti_flicker': AntiFlickerAlgorithm(width, height, args.filter_length, args.min_freq, args.max_freq,
                                                       args.time_window_flicker),
                  'anti_flicker_stc': AntiFlickerSTCFilter(width, height, args.time_window_flicker, args.time_window_stc,
                                                           args.filter_length, args.min_freq, args.max_freq,
                                                           args.cut_trail)
                  }

    events_buf = EventCDBuffer()

    ### ############################################################################################## ###
    filter_type = args.filter_save_type
    output_file = args.out_path

    with open(output_file, 'a') as csv_file:
        for evs in tqdm(mv_iterator):
            my_filters[filter_type].process_events(evs, events_buf)

            for (x, y, p, t) in events_buf.numpy():
                csv_file.write("%d,%d,%d,%d\n" % (x, y, p, t))

if __name__ == "__main__":
    main()
