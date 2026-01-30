import json

import pyperclip

test = ""

print(json.dumps(test.split(", ")))

pyperclip.copy(json.dumps(test.split(", ")))