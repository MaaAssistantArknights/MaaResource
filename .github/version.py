import json
import sys

if len(sys.argv) <= 1:
  exit(1)

version_file = sys.argv[1]
j = json.load(version_file)

if j["activity"]["time"] < j["gacha"]["time"]:
  display = j["gacha"]["pool"]
else:
  display = j["activity"]["name"]

display = display + " " + j["last_updated"]
print(display)
