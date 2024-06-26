import string
from itertools import product
from pathlib import Path
from faker import Faker

fake = Faker()

for a, b in product(string.ascii_lowercase, repeat=2):

    file = Path(f"secrets/{a}{b}/secrets.txt")
    file.parent.mkdir(parents=True, exist_ok=True)

    with open(file, "w") as f:
        name = fake.name().lower().split(" ")
        f.write("_".join(name))
