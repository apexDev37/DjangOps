FROM python:3.11.4-slim-bullseye

WORKDIR /usr/src/app
EXPOSE 8000

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN pip3 install --upgrade pip
COPY ./requirements/requirements.txt .
RUN pip3 install -r ./requirements.txt --no-cache-dir

COPY . . 

ENTRYPOINT ["python3"] 
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
