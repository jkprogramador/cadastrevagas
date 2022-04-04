FROM python:3.10.4-slim-buster
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
WORKDIR /usr/src/app
COPY Pipfile Pipfile.lock ./
RUN pip install pipenv && pipenv install --system
COPY ./src ./
ENTRYPOINT [ "python" ]
CMD [ "manage.py", "runserver", "0.0.0.0:8000" ]
