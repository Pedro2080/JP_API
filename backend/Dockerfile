FROM python:3.9

RUN apt update
RUN pip3 install --upgrade pip
RUN apt install -y -q build-essential python3-pip python3-dev
RUN pip3 install -U pip setuptools wheel

WORKDIR /jp_app

COPY ./test /app
COPY ./requirements.txt /jp_app/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r /jp_app/requirements.txt
COPY . .
COPY requirements.txt /app/requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
