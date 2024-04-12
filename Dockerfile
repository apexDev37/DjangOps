FROM python:3.12.3-alpine3.19
LABEL \
  author="Eugene Mwangi" \
  contact="mwangi.em37@gmail.com" \
  version="0.2.0" \
  license="MIT"

WORKDIR /usr/src/app
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements/base.txt ./
RUN pip3 --no-cache-dir install -r ./base.txt

COPY . /usr/src/app

EXPOSE 8000
ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
