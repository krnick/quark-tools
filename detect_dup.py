import json
import os
from _collections import defaultdict

result = defaultdict(str)

rev_multidict = {}

for item in os.listdir("."):
    if item.endswith(".json"):
        filename = item
        with open(item, "r") as f:
            data = json.loads(f.read())
            first_api = data["x2n3n4_comb"][0]["class"] + data["x2n3n4_comb"][0]["method"] + data["x2n3n4_comb"][0][
                "descriptor"]
            second_api = data["x2n3n4_comb"][1]["class"] + data["x2n3n4_comb"][1]["method"] + data["x2n3n4_comb"][1][
                "descriptor"]
            result[filename] = first_api + second_api

for key, value in result.items():
    rev_multidict.setdefault(value, set()).add(key)

# find dup values
print([key for key, values in rev_multidict.items() if len(values) > 1])
# find dup key
print([values for key, values in rev_multidict.items() if len(values) > 1])
