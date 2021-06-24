FROM python:3.9.5

WORKDIR /app

COPY src .
COPY requirements.txt .
COPY README.md .

RUN pip install -r requirements.txt

CMD ["python3", "calcmachine.py"]