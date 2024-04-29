from pathlib import Path
import csv
import os
import re

import pandas as pd
import numpy as np


def parse_file(input_file, output_dir, num_fields=15):
    csv_lines = []
    non_matching_lines = []
    blank_lines = 0
    recovered_detections = 0

    with open(input_file, 'r', encoding='utf-8', errors='replace') as file:
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
                    # If line doesn't match standard format, Try matching to regular expression to
                    # catch detections on lines that have additional garbage text
                    pattern = r'S,\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3},G,(\d{2}:){2}\d{2}\.\d{3},[AW]{1},A\d,[\d_]+,[A-Z\d]+,\d+,\d\.\d,\d+\/\d+,\d+\.\d+,\d+,\d+,\d+'
                    match = re.search(pattern, line)
                    if match:
                        # Get the matching detection text and format it as csv
                        matched_text = line[match.span()[0]: match.span()[1]]
                        fields = matched_text.split(',')
                        csv_lines.append(fields)
                        # Append garbage text to non-matching lines file
                        non_matching_lines.append(line[0: match.span()[0]])
                        recovered_detections += 1
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
        writer.writerow(["file", "lines", "detections", "non_detections", "blanks", "recovered"])
        writer.writerow(
            [Path(input_file).name, line_count, len(csv_lines),
             len(non_matching_lines), blank_lines, recovered_detections])

    print(f'Processing of "{input_file.name}" complete.')


def compile_csv_logs(directory, output_file):
    log_files = [file for file in os.listdir(directory) if file.endswith('_log.csv')]
    if not log_files:
        print("No log files found.")
        return
    log_files.sort()

    with open(Path(directory) / output_file, 'w', newline='') as output_csv:
        writer = csv.writer(output_csv)

        for i, file in enumerate(log_files):
            with open(os.path.join(directory, file), 'r') as input_csv:
                reader = csv.reader(input_csv)
                for j, row in enumerate(reader):
                    if i > 0 and j == 0:  # Skip writing header for files after the first
                        continue
                    writer.writerow(row)

    print(f"CSV logs compiled into {output_file}.")


def combine_data_files(path, l_files, **kwargs):
    """
    Searches a directory for text files, imports as pandas.DataFrames and
    concatenates to a single DataFrame.

    Args:
        path: pathlib.Path object of a directory
        **kwargs: Variable additional arguments pass to the pandas.read_csv function

    Returns: pandas.DataFrame

    """
    # Initialize an empty list to store DataFrames
    l_df = []

    # Loop through files
    for file in l_files:
        # Check if the file starts with the prefix and ends with the suffix
        l_df.append(pd.read_csv(path / file, **kwargs))

    # Concatenate the DataFrames
    df_return = pd.concat(l_df).reset_index(drop=True)

    # Return the concatenated DataFrame
    return df_return


def remove_tags(df, list_tags, tag_field='TAG'):
    """
    Removes tag IDs based on a list of specified tags.
    Parameters
    ----------
    df: DataFrame
    list_tags: List of tag IDs to remove
    tag_field: Field name of tag IDs

    Returns: Filtered DataFrame

    -------

    """
    df_return = df.copy()
    mask_remove = df_return[tag_field].isin(list_tags)
    df_return = df_return[~mask_remove].reset_index(drop=True)

    return df_return


def create_tag_range(base: str, value_range: tuple[int], pad: int = 3):
    """
    Creates a list of tag IDs given a base string and a range of values.
    Parameters
    ----------
    base: Base string of the ID
    value_range: Tuple number range to generate IDs
    pad: Number of digits the value range strings should be. Will pad leading zeros to the number.
        example pad=3 and value of 1 would create "001" for the value to append to the base string.

    Returns List of tag IDs
    -------

    """
    l_tags = [f'{base}{str(s).zfill(pad)}'for s in np.arange(value_range[0], value_range[1]+1)]
    return l_tags


if __name__ == '__main__':
    project_directory = Path(os.getcwd()).parents[1]
    file_list = ['PAL 2023-04-11.txt']
    input_directory = project_directory / 'data/raw/2023'
    output_directory = project_directory / 'data/processed/2023'

    parse_file(input_directory / file_list[0], output_directory, )
