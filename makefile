setup:
	python3 -m venv venv
	./venv/Scripts/pip install --upgrade pip
	make install
	
install:
	./venv/Scripts/pip install -r requirements.txt

run:
	./venv/Scripts/python ./src/main.py

run-dev:
	./venv/Scripts/python -m uvicorn app.main:app --reload