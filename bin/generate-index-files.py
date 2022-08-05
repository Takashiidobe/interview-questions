#!/usr/bin/env python3

from pathlib import Path

folders = [f for f in Path('./src').glob('**/**') if f.is_dir()]

for folder in folders:
    contents = """# Index

"""
    md_files = list(Path(folder).glob("*.md"))
    for md_file in sorted(md_files):
        if md_file.name == "index.md":
            continue
        contents += f"- [{md_file.stem}]({md_file.name})\n"
    with open(f"{folder}/index.md", "w+") as f:
        f.write(contents)

# for each folder, iterate through and set the link in index
index_file_contents = """# Index

"""
index_folders = [f for f in Path('./src').glob('*') if f.is_dir()]

for f in sorted(index_folders):
    index_file_contents += f"- [{f.stem}]({f.stem}/index.md)\n"

with open("./src/index.md", "w+") as f:
    f.write(index_file_contents)
