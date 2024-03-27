#!/usr/bin/env python3

from datetime import datetime
import subprocess
import argparse
import os
import sys
from config import FILEPATH

"""

    FILEPATH: File path specified in config.py for this script to write newly created files in

"""

def display_files(FILEPATH):
    file_list = os.listdir(FILEPATH)
    print("Available files:")
    for idx, filename in enumerate(file_list, start=1):
        print(f"[ {idx} ] - {filename}")

    while True:
        try:
            choice = int(input("Enter the number of the file you want to choose: "))
            if 1 <= choice <= len(file_list):
                chosen_file = file_list[choice - 1]
                #filepath = os.path.join(FILEPATH, chosen_file)
                return chosen_file
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter a valid number.")

def list_files_in_directory(FILEPATH):
    print(f"[+] Listing files at: {FILEPATH}")
    print("---"*30)
    try:
            # List all entries in the directory given by "directory_path"
        files = sorted(os.listdir(FILEPATH), key=lambda x: os.path.getmtime(os.path.join(FILEPATH, x)))
        for file in files:
            print(file)
    except Exception as e:
        print(f"[X] Error: {e}")
        return []

def vim(filepath, filename):
    if filepath.endswith("/"):
        full_filepath = filepath + filename
    else:
        full_filepath = filepath + "/" + filename
    try:
        subprocess.run(["vim", full_filepath])
        if not os.path.exists(full_filepath):
            print("Aborted by user")
            sys.exit(1)
    except Exception as e:
        print(f"[X] Error: {e}")
        sys.exit(1)
    return full_filepath

def update_file_headers(filename, filepath, timestamp):
    current_time = datetime.now()
    time_of_day = current_time.strftime("%H:%M")

    with open(filepath, "r") as raw_text:
        raw_text = raw_text.read()
        wordcount = len(raw_text)
    with open(filepath, "w") as final_text:
        md_headers = "\n".join([
        "---",
        f'title: "{filename}"',
        f"date: {timestamp}",
        f"time: {time_of_day}",
        f"wordcount: {wordcount}",
        "---"
        "\n"
         ])
        final_text.write(md_headers + raw_text)

    print(f"[i] File saved as {filepath}")


def refine_filename(raw_filename):
    timestamp = datetime.now().strftime("%Y-%m-%d")
    # Concatenate this timestamp with your desired filename
    refined_text = raw_filename.lower().replace(" ", "_")
        # Convenience: eliminate any common symbol from the filename
    symbols = "?¡¿',¡!"
    for symbol in symbols:
        if symbol in refined_text:
            refined_text = refined_text.replace(symbol, '')
    final_filename = f"{timestamp}_{refined_text}.md"
    return final_filename, timestamp

def init():
    try:
        raw_filename = input(" - Give the file a name: ")
        while not raw_filename:
            print("[X] Title cannot be empty. Assign a title to the file.\nIt can contain spaces, symbols, etc.")
            raw_filename = input(" - Give the file a name: ")
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(f"[!] Error: {e}")
        sys.exit(1)
    return raw_filename

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List default directory files")
    parser.add_argument("-l", "--list", nargs='?', const=True, default=None, help="List the default directory files")
    parser.add_argument("-e", "--edit", nargs='?', const=True, default=None, help="Edit selected files")
    args = parser.parse_args()
    if args.list:
        list_files_in_directory(FILEPATH)
        sys.exit(0)
    if args.edit:
        file = display_files(FILEPATH)
        print(f"Editing: {file}")
        vim(FILEPATH, file)
        sys.exit(0)
    raw_filename = init()
    final_filename, timestamp = refine_filename(raw_filename)
    full_filepath = vim(FILEPATH, final_filename)
    update_file_headers(final_filename, full_filepath, timestamp)
