import yaml
from pathlib import Path

testyaml = Path(__file__).parent / "../tests/notes.yaml"

with open(testyaml, "r") as stream:
    try:
        print(yaml.safe_load(stream))
        print("Complete.")
    except yaml.YAMLError as exc:
        print(exc)
