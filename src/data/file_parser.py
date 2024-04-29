# -*- coding: utf-8 -*-
from pathlib import Path
import csv
import sys
import os


def process_file(input_file, output_dir, num_fields=15):
    csv_lines = []
    non_matching_lines = []
    blank_lines = 0

    with open(input_file, 'r') as file:
        lines = file.readlines()
        line_count = len(lines)

        for line in lines:
            line = line.strip()
            if not line:
                blank_lines += 1
            else:
                fields = line.split(',')
                if len(fields) == num_fields:
                    csv_lines.append(fields)
                else:
                    non_matching_lines.append(line)

    # Output CSV file
    output_csv_file = os.path.join(output_dir,
                                   f"{os.path.splitext(os.path.basename(input_file))[0]}"
                                   f"_detection.csv")
    with open(output_csv_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(csv_lines)

    # Output non-matching lines
    output_non_matching_file = os.path.join(output_dir,
                                            f"{os.path.splitext(os.path.basename(input_file))[0]}"
                                            f"_non_detection.txt")
    with open(output_non_matching_file, 'w') as non_matching_file:
        non_matching_file.write('\n'.join(non_matching_lines))

    # Output log file in CSV format
    log_file = os.path.join(output_dir,
                            f"{os.path.splitext(os.path.basename(input_file))[0]}_log.csv")
    with open(log_file, 'w', newline='') as log_csv:
        writer = csv.writer(log_csv)
        writer.writerow(["file", "lines", "detections", "non_detections", "blanks"])
        writer.writerow(
            [Path(input_file).name, line_count, len(csv_lines), len(non_matching_lines), blank_lines])

    print("Processing complete.")


if __name__ == "__main__":
    # Check if the input file and output directory are provided as arguments
    if len(sys.argv) < 3:
        print("Please provide the input file, output directory, and optionally the number of fields as "
              "arguments.")
        sys.exit(1)

    input_file = sys.argv[1]
    output_dir = sys.argv[2]

    # Check if the number of fields argument is provided
    num_fields = 15  # Default value
    if len(sys.argv) >= 4:
        num_fields = int(sys.argv[3])

    process_file(input_file, output_dir, num_fields)
