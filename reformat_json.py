import json
import os
from _collections import defaultdict

for item in os.listdir("."):
    if item.endswith(".json"):
        filename = item
        with open(item, "r") as f:
            data = json.loads(f.read())

            print(data)

            newdata = {
                "crime": data["crime"],
                "x1_permission": data["x1_permission"],
                "x2n3n4_comb": data["x2n3n4_comb"],
                "yscore": data["yscore"],
                "label": data["label"]
            }

            with open(f"{filename}", 'w', encoding='utf-8') as f:
                json.dump(newdata, f, indent=4)
