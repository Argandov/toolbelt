#!/usr/bin/env python3

from datetime import datetime
from config import FILEPATH
import argparse
import sys
import os

"""

    FILEPATH: File path specified in config.py for this script to write newly created files in

"""

def list_files_in_directory(outfile_path):
    print(f"[+] Listing files at: {outfile_path}")
    print("---"*30)
    try:
        # List all entries in the directory given by "directory_path"
        entries = os.listdir(outfile_path)
        files = [entry for entry in entries if os.path.isfile(os.path.join(outfile_path, entry))]
        for file in files:
            print(file)
    except Exception as e:
        print(f"[X] Error: {e}")
        return []

def capture_memories():
    print("Type /bye to save & close or Ctrl+C to exit.")
    print("---"*30)
    lines = []
    try:
        while True:

            line = input()
                # Out Phrase:
            if line == "/bye":
                break
            lines.append(line)
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(f"[!] Error: {e}")
        sys.exit(1)
    text = "\n".join(lines)
    print("----"*8)
    raw_filename = input("> Give the file a name:")
    while not raw_filename:
        raw_filename = input("[X] Title cannot be empty. Give the file a name:")
    return raw_filename, text

def count_words(text):
    wordslist = text.split()
    wordcount = len(wordslist)
    return wordcount

def write_file_headers(wordcount, raw_filename, timestamp):
    # Here we write a Markdown syntax header section to the outfile; like a "metadata" section

        # Get & Format the time in a 24-hour format (HH:MM)
    current_time = datetime.now()
    time_of_day = current_time.strftime("%H:%M")

    markdown_header = "\n".join([
    "---",
    f'title: "{raw_filename}"',
    f"date: {timestamp}",
    f"time: {time_of_day}",
    f"wordcount: {wordcount}",
    "---"
    "\n"
    ])

    return markdown_header

def define_outfile_headers(raw_filename):
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

def write_to_file(outfile_path, markdown_header, final_filename, text):
    full_filepath = f"{outfile_path}/{final_filename}"
    try:
        with open(full_filepath, 'w') as outfile:
            outfile.write(markdown_header)
            outfile.write("\n")
            outfile.write(text)
            print(f"[i] Ok. File saved as {full_filepath}")
    except Exception as e:
        print(f"[X] Error: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List default directory files")
    parser.add_argument("-l", "--list", nargs='?', const=True, default=None, help="List the default directory files")
    args = parser.parse_args()
    if args.list:
        list_files_in_directory(FILEPATH)
    else:
        raw_filename, text = capture_memories()
        final_filename, timestamp = define_outfile_headers(raw_filename)
        wordcount = count_words(text)
        markdown_header = write_file_headers(wordcount, raw_filename, timestamp)
        write_to_file(FILEPATH, markdown_header, final_filename, text)
