.PHONY: install run build clean venv

# Cross-platform venv python/pip paths
ifeq ($(OS),Windows_NT)
VENV_PY=.venv\\Scripts\\python.exe
RM=rd /s /q
else
VENV_PY=.venv/bin/python
RM=rm -rf
endif

venv:
	python -m venv .venv

install: venv
	$(VENV_PY) -m pip install -r requirements.txt

run:
	$(VENV_PY) src/pdf_splitter.py

build:
	$(VENV_PY) src/build.py

clean:
	$(RM) dist build *.spec __pycache__