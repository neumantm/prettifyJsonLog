#!/usr/bin/env python3
from typing import Dict, List, Any, Tuple, Optional

from itertools import islice

import sys
import os
import json
import fileinput
import shutil

HEADER_COLUMNS = [["time", "timestamp"],["level", "severity"],["message", "msg"]]
HEADER_DELIMITER= " "

def print_string(string: str, indent: int, continued_add_indent: int = 4):
    remaining_string = string
    effective_indent = indent
    effective_term_width = term_width
    while len(remaining_string) > 0:
        if effective_indent > effective_term_width - 10:
            effective_term_width += 10
        data_width = effective_term_width - effective_indent
        string_part = remaining_string[0:data_width]
        remaining_string = remaining_string[data_width:]
        print(" "*effective_indent + string_part)
        if effective_indent == indent:
            effective_indent += continued_add_indent

def get_header_value(entry: Dict[str,Any], col_idx: int) -> Tuple[Optional[str], str]:
    """Return consumed key and header value"""
    for col_name in HEADER_COLUMNS[col_idx]:
        if col_name in entry:
            return col_name, str(entry[col_name])
    return None, ""

def print_header(entry: Dict[str,Any]) -> List[str]:
    """Print the header for the entry and return the consumed keys."""
    consumed_keys = []
    header_values = []
    for col in range(0, len(HEADER_COLUMNS)):
        key, value = get_header_value(entry, col)
        header_values.append(value)
        if key is not None:
            consumed_keys.append(key)
    header_str = HEADER_DELIMITER.join(header_values)
    print_string(header_str, 0)
    return consumed_keys

def _print_attributes_list(attributes: List[Any], indent: int, prefix=""):
    first = True
    for attribute in attributes[0:30]:
        if first:
            print_attributes(attribute, indent, prefix + "- ")
            first = False
        else:
            print_attributes(attribute, indent + len(prefix), "- ")
    if len(attributes) > 30:
        print_string(f"[... {len(attributes)-30} more items]", indent + len(prefix))

def _print_attributes_dict(attributes: Dict[str, Any], indent: int, prefix=""):
    key_length = 0
    for key in attributes:
        k_l = len(key)
        if(k_l > term_width/4):
            continue
        if k_l > key_length:
            key_length = k_l

    first = True
    for key, value in islice(attributes.items(), 30):
        padded_key = key.ljust(key_length) + ": "
        if first:
            if(len(key) > term_width/4):
                print_string(prefix + padded_key, indent)
                print_attributes(value, indent + 2)
            else:
                print_attributes(value, indent, prefix + padded_key)
            first = False
        else:
            if(len(key) > term_width/4):
                print_string(padded_key, indent + len(prefix))
                print_attributes(value, indent + len(prefix) + 2)
            else:
                print_attributes(value, indent + len(prefix), padded_key)
    if len(attributes.keys()) > 30:
        print_string(f"[... {len(attributes.keys())-30} more items]", indent + len(prefix))

def print_attributes(attributes: Any, indent: int = 2, prefix=""):
    if isinstance(attributes, list):
        _print_attributes_list(attributes, indent, prefix)
    elif isinstance(attributes, dict):
        _print_attributes_dict(attributes, indent, prefix)
    else:
        print_string(prefix + str(attributes), indent, len(prefix))

def print_entry(entry: Dict[str,Any]):
    counsumed_keys = print_header(entry)
    remaining_entry = {k:v for k,v in entry.items() if k not in counsumed_keys}
    print_attributes(remaining_entry)


def main():
    global term_width
    term_width = shutil.get_terminal_size((80, 20)).columns

    for line in fileinput.input():
        try:
            data = json.loads(line)
        except:
            print(f"Failed to load line as json: {line}")
            continue
        print_entry(data)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)
