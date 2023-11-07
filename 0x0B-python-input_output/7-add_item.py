#!/usr/bin/python3
"""Adds all arguments to a list and save them to a file."""
if __name__ == "__main__":
    from sys import argv
    save = __import__('5-save_to_json_file').save_to_json_file
    load = __import__('6-load_from_json_file').load_from_json_file

    try:
        my_list = load("add_item.json")
    except FileNotFoundError:
        my_list = []

    for i in range(1, len(argv)):
        my_list.append(argv[i])

    save(my_list, "add_item.json")
