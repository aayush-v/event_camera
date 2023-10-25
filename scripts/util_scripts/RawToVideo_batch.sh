#!/bin/bash

folder_path="/media/exx/Elements/aayush/data/event_data/transfer"

for file in "$folder_path"/*
do
    if [ -f "$file" ]; then
        echo "Processing file: $file"

        filename=$(basename "$file")
        output_path="/media/exx/Elements/aayush/data/RawToVideo_videos/$filename.avi"
        metavision_file_to_video -i "$file" -o "$output_path" --accumulation-time 20000
    fi
done

