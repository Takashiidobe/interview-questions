#!/usr/bin/env python3

from pathlib import Path
import os

p = Path('./src')

folders = [f for f in p.iterdir() if f.is_dir()]

# for each folder, iterate through and set the link in index

index_file_contents = """# Index

"""

for f in sorted(folders):
    index_file_contents += f"- [{f.stem}]({f.stem}/index.md)\n"

with open("./src/index.md", "w+") as f:
    f.write(index_file_contents)

for f in folders:
    contents = """# Index

"""
    md_files = list(Path(f).glob("*.md"))
    for md_file in sorted(md_files):
        if md_file.name == "index.md":
            continue
        contents += f"- [{md_file.stem}]({md_file.name})\n"
    with open(Path(f)/"index.md", "w+") as f:
        f.write(contents)
