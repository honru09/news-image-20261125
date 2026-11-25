"""news-image-20261125 -- copy the bundled picture to the output folder.

The entry image lives in this repository next to this script. This
program does one job: check that image thoroughly, then place an exact
copy at <output>/entry.png. It never draws, downloads, or changes the
pixels -- the copy is byte-for-byte the file that was reviewed.

Run it with no arguments. The destination defaults to /output and can
be pointed elsewhere with MAKEFUN_OUTPUT_DIR, which the harness uses
when it runs the program twice to confirm both runs agree.
"""

import os
import shutil
import struct
import sys
import zlib

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
WANTED_WIDTH = 1024
WANTED_HEIGHT = 1024
MAX_BYTES = 1024 * 1024
CHUNK_HEADER = 8  # 4 bytes length + 4 bytes type
CHUNK_FOOTER = 4  # 4 bytes CRC


def fail(message):
    """Report a problem on stderr and stop with a failure exit code."""
    print("error: " + message, file=sys.stderr)
    return 1


def read_source(path):
    """Load the bundled picture, failing loudly if anything is off."""
    try:
        with open(path, "rb") as handle:
            blob = handle.read()
    except OSError as exc:
        return None, "cannot read bundled image %s: %s" % (path, exc)
    if len(blob) > MAX_BYTES:
        return None, "bundled image is %d bytes, over the 1 MiB limit" % len(blob)
    if len(blob) < len(PNG_MAGIC) or blob[: len(PNG_MAGIC)] != PNG_MAGIC:
        return None, "bundled image does not start with the PNG signature"
    return blob, None


def check_chunks(blob):
    """Walk every PNG chunk, checking its CRC, up to and including IEND."""
    offset = len(PNG_MAGIC)
    seen_image_header = False
    seen_end = False
    while offset < len(blob):
        if offset + CHUNK_HEADER + CHUNK_FOOTER > len(blob):
            return "truncated chunk header at byte %d" % offset
        (length,) = struct.unpack(">I", blob[offset : offset + 4])
        kind = blob[offset + 4 : offset + 8]
        body_start = offset + CHUNK_HEADER
        body_end = body_start + length
        crc_end = body_end + CHUNK_FOOTER
        if crc_end > len(blob):
            return "chunk %r runs past the end of the file" % kind.decode(
                "latin-1", "replace"
            )
        (stored_crc,) = struct.unpack(">I", blob[body_end:crc_end])
        actual_crc = zlib.crc32(kind)
        actual_crc = zlib.crc32(blob[body_start:body_end], actual_crc)
        if (actual_crc & 0xFFFFFFFF) != stored_crc:
            return "chunk %r fails its CRC32 check" % kind.decode(
                "latin-1", "replace"
            )
        if kind == b"IHDR":
            if length != 13:
                return "IHDR chunk has the wrong length"
            width, height = struct.unpack(">II", blob[body_start : body_start + 8])
            if width != WANTED_WIDTH or height != WANTED_HEIGHT:
                return "image is %dx%d, expected %dx%d" % (
                    width,
                    height,
                    WANTED_WIDTH,
                    WANTED_HEIGHT,
                )
            seen_image_header = True
        if kind == b"IEND":
            seen_end = True
            if crc_end != len(blob):
                return "trailing bytes after the IEND chunk"
            break
        offset = crc_end
    if not seen_image_header:
        return "no IHDR chunk found in the PNG"
    if not seen_end:
        return "no IEND chunk found in the PNG"
    return None


def empty_folder(path):
    """Remove everything inside a folder, leaving the folder itself."""
    for name in os.listdir(path):
        target = os.path.join(path, name)
        if os.path.isdir(target) and not os.path.islink(target):
            shutil.rmtree(target)
        else:
            os.unlink(target)


def run():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    blob, problem = read_source(source)
    if problem is not None:
        return fail(problem)
    problem = check_chunks(blob)
    if problem is not None:
        return fail(problem)

    destination_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(destination_dir, exist_ok=True)
        empty_folder(destination_dir)
        destination = os.path.join(destination_dir, "entry.png")
        shutil.copyfile(source, destination)
        os.chmod(destination, 0o644)
    except OSError as exc:
        return fail("cannot write output: %s" % exc)
    print("wrote %s (%d bytes)" % (destination, len(blob)))
    return 0


if __name__ == "__main__":
    sys.exit(run())

# Notes for anyone re-running this entry
#
# Exit codes: 0 means the copy landed and passed every check; 1 means
# something failed and nothing was written to the output folder. The
# source image is validated before the output folder is touched, so a
# bad source can never leave a half-written or stale file behind.
#
# Determinism: the program only copies bytes, so two runs always
# produce the same file. Running it twice and comparing the hashes of
# the two outputs is a quick way to confirm that.
#
# Limits enforced here, matching the competition rules: PNG only,
# exactly 1024 by 1024 pixels, at most 1 MiB, every chunk CRC-checked.
