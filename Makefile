.PHONY: install run build clean venv

venv:
	python3 -m venv .venv

install: venv
	.venv/bin/python -m pip install -r requirements.txt

run:
	.venv/bin/python src/pdf_splitter.py

build:
	.venv/bin/python src/build.py

clean:
	rm -rf dist build *.spec __pycache__