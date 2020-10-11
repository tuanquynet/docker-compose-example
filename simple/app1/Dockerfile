FROM python:3.7

RUN mkdir -p /usr/src/app/src
WORKDIR /usr/src/app/src
COPY src/ /usr/src/app/src/
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /usr/src/app/src

CMD ["python", "-u", "index.py"]
