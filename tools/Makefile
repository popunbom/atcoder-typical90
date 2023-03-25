PYTHON = .venv/bin/python3

init:
	python3 -m venv .venv

add:
	$(PYTHON) -m cli.add $(PROB_NUM)

check:
	$(PYTHON) -m cli.test $(PROJECT_DIR) --only_exec

test:
	$(PYTHON) -m cli.test $(PROJECT_DIR)
