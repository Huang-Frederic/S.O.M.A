FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install

RUN playwright install-deps

CMD ["python", "main.py"]
