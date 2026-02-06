#!/bin/env python

import re
import shutil
import sys


def doit(filename):

    if not filename.endswith(".html"):
        # nothing to do here
        sys.exit(f"skipping {filename}\n")

    alt_define = re.compile(r'.*#\s*alt-text:\s*([^<]+)')
    img_define = re.compile(r'(<img\b[^>]*\balt=")[^"]*(")')
    empty_span = re.compile(r'<\s*span\b[^>]*>\s*</\s*span\s*>')

    # back up the original file
    backup = f"{filename}.backup"
    try:
        shutil.copy(filename, backup)
    except OSError:
        sys.exit(f"unable to work on {filename}\n")

    # now overwrite the original with the new version with the alt
    # text substituted
    with open(backup, encoding='utf-8') as fin, open(filename, "w", encoding='utf-8') as fout:
        current_alt = None
        for line in fin:
            # check if we define an alt?
            if g := alt_define.match(line):
                current_alt = g.group(1)
                print(f"{current_alt=}")

                # now remove the comment
                line = line.replace(f"# alt-text: {current_alt}", "")

                # it the line is now just an empty <span ...></span> then skip
                if empty_span.match(line.strip()):
                    continue

            # check if we are defining an image
            if current_alt:
                line, n = img_define.subn(rf'\g<1>{current_alt}\g<2>', line)
                if n > 0:
                    current_alt = None

            fout.write(line)

        if current_alt:
            # something back happened
            sys.exit("Error: alt text without associated img tag\n")

if __name__ == "__main__":
    filename = sys.argv[1]
    doit(filename)
