#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as hid
    filtered = []
    unfiltered = dir(hid)
    filtered = [name for name in unfiltered if not name.startswith('__')]
    filtered.sort()
    for name in filtered:
        print("{:s}".format(name))
