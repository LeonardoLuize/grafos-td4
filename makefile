setup:
	python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	make install
	
install:
	./venv/bin/pip install -r requirements.txt

run:
	./venv/bin/python ./src/main.py