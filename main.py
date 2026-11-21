#!/usr/bin/env python3
"""Copy the finished front page to /output/entry.png.

The graded program: it writes one image, deterministically, with no
network. The copy is byte-exact, so both graded runs write identical
bytes. The image itself is drawn at build time by render.py (Pillow)
from reporting on Friday 20 November 2026, verified in multiple outlets.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")

os.makedirs(os.path.dirname(DST), exist_ok=True)
shutil.copyfile(SRC, DST)
