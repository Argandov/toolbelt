# Quick Notetakers

This repository contains two basic notetaking python scripts described below.

Scripts designed for quickly taking notes on the fly, and saving them as Markdown files with a proper Md compliant header generated automatically in a default folder specified in the configfile `config.py`. They can be used for Obsidian or other Markdown local Notetaking applications.

NOTE: Both scripts work independently from each other. I first created stdin-notetaker.py but soon I had the idea of the vim-notetaker.py and decided to just keep both just in case.

How it looks:

```
argv@deb:~$ alias m=python3 /path/to/vim-notetaker.py

argv@deb:~$ m

 - Give the file a name: hello world

    (NEW FILE OPENS IN VIM)

[i] File saved as /home/user/ObsidianFiles/2024-03-18_hello_world.md

```

```
argv@deb:~$ cat /filepath/2024-03-18_hello_world.md

---
title: "2024-03-18_hello_world.md"
date: 2024-03-18
time: 14:54
wordcount: 4
---
Hi!


```

### stdin-notetaker.py
This script captures inputs directly from the console on execution. Terminates by typing "/bye". 
It then prompts the user to name the file (This title will be formatted by the script so spaces or other usual symbols will be trimmed or deleted to form the filename). It finally auto-generates a markdown file based on the user's inputs together with a markdown compliant header. 
The script also includes options (-l or --list) to list all files in the default output directory.

### vim-notetaker.py
It gets an input text as the file's title (This title will be formatted by the script so spaces or other usual symbols will be deleted to form the filename), then opens Vim at the default directory path (As specified in config.py file), and then finally adds additional Markdown headers to it after saving.
The script also includes options (-l or --list) to list all files in the default output directory.

### Usage

- `cp config.py.example config.py`
- Modify the config.py file as desired (All files created by this notetaking script will be saved there)
- just `alias m=python3 /path/to/vim-notetaker.py` for quickly taking notes from wherever we're situated while at the terminal.

Exiting: Ctrl+c at any moment, or inside Vim just `:q` to abort

Note: Type `/bye` when you're done giving your inputs to the memory capture script. Use `--list` flag to list all files in the outfile directory i.e., `python3 vim-notetaker.py --list`
