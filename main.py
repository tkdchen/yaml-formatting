#!/usr/bin/env python3

import argparse
from ruamel.yaml import YAML
from subprocess import run

parser = argparse.ArgumentParser(description="Hacking on YAML formatting")
parser.add_argument("--yq-in-advance", action="store_true", help="Run yq before loading test YAML file.")
args = parser.parse_args()

yaml_file = "./test.yaml"

if args.yq_in_advance:
    run(["yq", "-i", yaml_file], check=True)
    run(["cat", yaml_file])

yaml = YAML()
yaml.width = 4096
yaml.preserve_quotes = True

with open(yaml_file, "r") as f:
    doc = yaml.load(f)

with open(yaml_file + ".modified", "w+") as f:
    yaml.dump(doc, f)
