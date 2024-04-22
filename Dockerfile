FROM python:3.12-bullseye

ARG proxy

ENV HTTPS_PROXY=${proxy}
ENV HTTP_PROXY=${proxy}
ENV http_proxy=${proxy}
ENV https_proxy=${proxy}

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY yaml_reader.py .
COPY glossary.yml .

CMD ["python", "yaml_reader.py"]
