#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: $0 <directory_path>"
    exit 1
fi

directory_path="$1"
mkdir -p "$directory_path/h5"

cd "$directory_path" || exit

# Loop through all .raw files
for raw_file in *.raw; do
    # Check if the item is a file (not a directory)
    if [ -f "$raw_file" ]; then

        # Check if a corresponding .hdf5 file is already created
        hdf5_file="h5/${raw_file%.raw}.hdf5"
        if [ ! -f "$hdf5_file" ]; then
            metavision_file_to_hdf5 -i "$raw_file"
        fi
    fi
done

mv *.hdf5 h5/
