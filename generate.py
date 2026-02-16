import random
import json
from datetime import datetime

data = {
    "timestamp": datetime.utcnow().isoformat(),
    "random_number": random.randint(1, 1000)
}

with open("output.json", "w") as f:
    json.dump(data, f, indent=2)

print("Generated:", data)
