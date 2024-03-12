#!/usr/bin/env python3

import tiktoken
import sys

base = "cl100k_base"

def num_tokens_from_string(string: str, encoding_name: str) -> int:

    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

if not sys.stdin.isatty():
    stdin_stream = []
    for l in sys.stdin:
        stdin_stream.append(l.strip())
    raw_text = '\n'.join(stdin_stream)
    total_tokens = num_tokens_from_string(raw_text, base)
    print(total_tokens)
else:
    print("[!] Input data must be from stdin")


