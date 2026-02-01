"""
The MIT License (MIT)

Copyright (c) 2023-Present cxdzc

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import sys
import platform
import importlib.metadata
import argparse

from . import __version__, __patch__

def main() -> None:
    parser = argparse.ArgumentParser(prog="TornAPIWrapper", allow_abbrev=False)
    parser.add_argument("-v", "--version", action="store_true")
    args = parser.parse_args()

    if not args.version:
        return

    v = sys.version_info
    print(f"- Python v{v.major}.{v.minor}.{v.micro}-{v.releaselevel}")
    print(f"- TornAPIWrapper v{__version__}")
    print(f"- Patch v{__patch__}")
    print(f"- requests v{importlib.metadata.version('requests')}")
    u = platform.uname()
    print(f"- system info: {u.system} {u.release} {u.version}")

if __name__ == "__main__":
    main()