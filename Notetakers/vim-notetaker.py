#!/usr/bin/env python3

from datetime import datetime
import subprocess
import os
import sys
from config import FILEPATH

"""

    FILEPATH: File path specified in config.py for this script to write newly created files in

"""

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
    symbols = "?¡¿',"
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

raw_filename = init()
final_filename, timestamp = refine_filename(raw_filename)
full_filepath = vim(FILEPATH, final_filename)
update_file_headers(final_filename, full_filepath, timestamp)
