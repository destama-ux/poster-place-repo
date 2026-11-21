#!/usr/bin/env python3
"""SALVORA — a travel poster for a place that does not exist.

The entry program for make.fun's "The Poster for a Place That Isn't There"
bounty. The poster itself (poster.jpg, in this repository's root) shows the
invented bay of Salvora, where golden dunes run down into a turquoise sea
under the beam of a white lighthouse. This program's whole job is the house
contract: verify the poster is a whole JPEG inside the gate limits, then
copy it to entry.png in the output directory.
"""

import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
POSTER = os.path.join(HERE, "poster.jpg")
MAX_BYTES = 1_048_576
MAX_SIDE = 1024


def jpeg_size(path):
    """Return (width, height) of a JPEG by walking its segments."""
    with open(path, "rb") as fh:
        data = fh.read()
    if data[:2] != b"\xff\xd8":
        raise ValueError("not a JPEG file")
    i = 2
    while i + 9 < len(data):
        if data[i] != 0xFF:
            i += 1
            continue
        marker = data[i + 1]
        if marker in (0xC0, 0xC1, 0xC2):
            height, width = struct.unpack(">HH", data[i + 5 : i + 9])
            return width, height
        seg_len = struct.unpack(">H", data[i + 2 : i + 4])[0]
        i += 2 + seg_len
    raise ValueError("no frame header found")


def check_poster(path):
    size = os.path.getsize(path)
    if size == 0 or size > MAX_BYTES:
        raise ValueError(f"poster is {size} bytes, gate allows {MAX_BYTES}")
    width, height = jpeg_size(path)
    if width > MAX_SIDE or height > MAX_SIDE:
        raise ValueError(f"poster is {width}x{height}, gate allows {MAX_SIDE}")
    return width, height, size


def main():
    width, height, size = check_poster(POSTER)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(POSTER, target)
    if os.path.getsize(target) != size:
        raise IOError("copied poster differs in size from the source")
    print(f"entry.png written: SALVORA poster, {width}x{height}, {size} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
