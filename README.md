```bash
git clone https://github.com/konflux-ci/pipeline-migration-tool
pushd pipeline-migration-tool
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 -m pip install -e .
popd
python3 main.py
git diff
```
