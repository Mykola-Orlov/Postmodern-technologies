FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /project

COPY app /project/app
COPY tests /project/tests
COPY requirements.txt /project/

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install pytest

ENV PYTHONPATH=/project

LABEL org.opencontainers.image.source="https://github.com/Mykola-Orlov/Postmodern-technologies"

CMD ["pytest"]