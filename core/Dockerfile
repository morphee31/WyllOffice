FROM python:3.11.3-alpine as fastapi-requirements

LABEL author="Thomas Cassan"

RUN pip install -U pip

COPY . /app

RUN pip install -r /app/requirements/prod.txt

RUN rm -r /app/requirements/prod.txt

FROM fastapi-requirements

WORKDIR /app/src

EXPOSE 8000

CMD ["uvicorn", "main:app","--host=0.0.0.0", "--port=8000"]
