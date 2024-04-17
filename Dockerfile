FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY yaml_reader.py .
COPY glossary.yaml .

CMD ["python", "yaml_reader.py"]
