FROM python:3.11.3-alpine as fastapi-requirements

LABEL author="Thomas Cassan"

RUN pip install -U pip

COPY ./requirements /tmp/requirements

RUN pip install /tmp/requirements/prod.txt


FROM fastapi-requirements

COPY ./src /app

EXPOSE 8000

CMD ["uvicorn", "app.main:app","--host=0.0.0.0", "--port=8000"]