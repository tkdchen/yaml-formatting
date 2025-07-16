.PHONY: reproduce
reproduce:
	if [ ! -e pipeline-migration-tool ]; then \
		git clone https://github.com/konflux-ci/pipeline-migration-tool; \
	fi
	[ -e .venv ] || python3 -m venv .venv
	.venv/bin/python3 -m pip install -r pipeline-migration-tool/requirements.txt
	.venv/bin/python3 -m pip install -e pipeline-migration-tool/
	.venv/bin/python3 ./main.py
	git --no-pager diff test.yaml
