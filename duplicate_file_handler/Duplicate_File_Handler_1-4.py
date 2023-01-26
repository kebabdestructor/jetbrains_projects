import sys
import os

args = sys.argv
if len(args) < 2:
   print("Directory is not specified")
else:
    for root, dirs, files in os.walk(args[1], topdown=True):
        for name in files:
            print(os.path.join(root, name))