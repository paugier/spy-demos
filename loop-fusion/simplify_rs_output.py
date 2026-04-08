#!/usr/bin/env python3

import sys

from pathlib import Path

content = Path(sys.argv[1]).read_text()

start = content.split("::", 1)[0]

print(start)

name = start.split("`")[1]

print(name)

content = content.replace(name + "::", "").replace("::Self", "").replace(str(Path.home()), "~")

print(content)