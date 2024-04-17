FROM python:3.9-slim-buster

ENV HTTPS_PROXY=http://ukd-proxy.med.tu-dresden.de:80/
ENV HTTP_PROXY=http://ukd-proxy.med.tu-dresden.de:80/
ENV http_proxy=http://ukd-proxy.med.tu-dresden.de:80/
ENV https_proxy=http://ukd-proxy.med.tu-dresden.de:80/

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY yaml_reader.py .
COPY glossary.yml .

CMD ["python", "yaml_reader.py"]
