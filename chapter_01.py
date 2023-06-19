#!/usr/bin/env python3

from pathlib import Path

print(Path("/etc"))
print(f"home: {Path.home()}")
print(f"cwd: {Path.cwd()}")
