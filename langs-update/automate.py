"""
# CREATE DIRS

import os
dirs = os.listdir("../docs")
for i in dirs:
    if len(i) == 2:
        with open(f"{i}.md", "w") as f:
            print("done")

"""