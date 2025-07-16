from ruamel.yaml import YAML
from subprocess import run

yaml_file = "./test.yaml"

run(["yq", "-i", yaml_file], check=True)
run(["cat", yaml_file])


yaml = YAML()
yaml.width = 4096
yaml.preserve_quotes = True

with open(yaml_file, "r") as f:
    doc = yaml.load(f)

with open(yaml_file, "w+") as f:
    yaml.dump(doc, f)
