FROM python:3.10.6-alpine3.16
RUN apk add git build-base linux-headers libffi-dev
WORKDIR /e_commerce


COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .



CMD ["python","manage.py", "runserver"]
