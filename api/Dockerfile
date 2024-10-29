FROM python:3.9

WORKDIR /src

COPY ./requirements.txt /src/requirements.txt
COPY .env /src/.env

RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

COPY ./app /src/app

EXPOSE 8000

CMD ["python", "app/main.py"]