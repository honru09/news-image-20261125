#!/usr/bin/env python3
"""Copy entrypoint for the news-image-20261125 make.fun entry.

Stdlib only. Copies the bundled ``entry.png`` (which must be a
1024x1024 PNG of at most 1 MiB) into the output directory as
``entry.png``. The output directory defaults to ``/output`` and can be
overridden with the ``MAKEFUN_OUTPUT_DIR`` environment variable.

Before writing, the output directory's existing contents are removed
(the directory itself is never deleted). The source image is validated
first: PNG magic bytes and IHDR dimensions of exactly 1024x1024. Any
failed check exits non-zero without writing an output file.
"""

import os
import shutil
import struct
import sys
import zlib

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1024 * 1024
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    sys.exit(1)


def validate_png(data):
    """Validate the bundled image; exit 1 on the first problem found."""
    if len(data) > MAX_BYTES:
        fail(f"source image is {len(data)} bytes, over the 1 MiB limit")
    if len(data) < 8 or data[:8] != PNG_MAGIC:
        fail("source image does not start with the PNG magic bytes")
    if len(data) < 33:
        fail("source image is too short to contain an IHDR chunk")

    offset = 8
    seen_ihdr = False
    seen_iend = False
    while offset < len(data):
        if offset + 8 > len(data):
            fail("truncated PNG chunk header")
        length = struct.unpack(">I", data[offset:offset + 4])[0]
        chunk_type = data[offset + 4:offset + 8]
        body_start = offset + 8
        body_end = body_start + length
        if body_end + 4 > len(data):
            fail(f"truncated PNG chunk {chunk_type!r}")
        chunk_data = data[body_start:body_end]
        stored_crc = struct.unpack(">I", data[body_end:body_end + 4])[0]
        actual_crc = zlib.crc32(chunk_type)
        actual_crc = zlib.crc32(chunk_data, actual_crc)
        if actual_crc != stored_crc:
            fail(f"PNG chunk {chunk_type.decode('latin-1')} has a bad CRC")
        if chunk_type == b"IHDR":
            if seen_ihdr:
                fail("duplicate IHDR chunk")
            seen_ihdr = True
            if length != 13:
                fail("IHDR chunk has the wrong length")
            width, height = struct.unpack(">II", chunk_data[:8])
            if width != EXPECTED_WIDTH or height != EXPECTED_HEIGHT:
                fail(
                    f"image is {width}x{height}, "
                    f"expected {EXPECTED_WIDTH}x{EXPECTED_HEIGHT}"
                )
        if chunk_type == b"IEND":
            seen_iend = True
            if body_end + 4 != len(data):
                fail("trailing data after IEND chunk")
            break
        offset = body_end + 4
    if not seen_ihdr:
        fail("PNG has no IHDR chunk")
    if not seen_iend:
        fail("PNG has no IEND chunk")


def clear_output_dir(path):
    """Remove everything inside path, leaving path itself in place."""
    os.makedirs(path, exist_ok=True)
    for name in os.listdir(path):
        target = os.path.join(path, name)
        if os.path.isdir(target) and not os.path.islink(target):
            shutil.rmtree(target)
        else:
            os.unlink(target)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    try:
        with open(source, "rb") as handle:
            data = handle.read()
    except OSError as exc:
        fail(f"cannot read bundled entry.png: {exc}")

    validate_png(data)

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    clear_output_dir(output_dir)
    destination = os.path.join(output_dir, "entry.png")
    try:
        with open(destination, "wb") as handle:
            handle.write(data)
        os.chmod(destination, 0o644)
    except OSError as exc:
        fail(f"cannot write output image: {exc}")
    print(f"wrote {destination} ({len(data)} bytes)")


if __name__ == "__main__":
    main()
