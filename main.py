from subprocess import run
from pipeline_migration.utils import YAMLStyle, load_yaml, dump_yaml

yaml_file = "./test.yaml"
ys = YAMLStyle.detect(yaml_file)

run(["yq", "-i", yaml_file], check=True)
run(["cat", yaml_file])

doc = load_yaml(yaml_file, ys)
dump_yaml(yaml_file, doc, ys)
