FROM python:3.11.4-slim-bullseye
LABEL \
  author="Eugene Mwangi" \
  contact="mwangi.em37@gmail.com" \
  version="0.1.0" \
  license="MIT"

WORKDIR /usr/src/app
EXPOSE 8000

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install -r requirements/pip.txt --no-cache-dir
COPY ./requirements/base.txt ./
RUN pip install -r ./base.txt --no-cache-dir

COPY . ./

ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
