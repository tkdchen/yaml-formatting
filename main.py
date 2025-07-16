from ruamel.yaml import YAML
from subprocess import run
from pipeline_migration.utils import YAMLStyle, load_yaml, dump_yaml

yaml_file = "./test.yaml"
# ys = YAMLStyle.detect(yaml_file)

run(["yq", "-i", yaml_file], check=True)
run(["cat", yaml_file])


yaml = YAML()
yaml.width = 4096
yaml.preserve_quotes = True

# doc = load_yaml(yaml_file, ys)
# dump_yaml(yaml_file, doc, ys)

with open(yaml_file, "r") as f:
    doc = yaml.load(f)

with open(yaml_file, "w+") as f:
    yaml.dump(doc, f)
