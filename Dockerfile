# use alpine base image with python build tools.
FROM python:3.12.3-alpine3.19
LABEL \
  author="Eugene Mwangi" \
  contact="mwangi.em37@gmail.com" \
  version="0.2.1" \
  license="MIT"

WORKDIR /usr/src/app

# set python-specific dev env variables.
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PIP_DISABLE_PIP_VERSION_CHECK 1

RUN <<EOF
addgroup -S docker
adduser -S --shell /bin/bash --ingroup docker appuser
EOF

# install app's base runtime dependencies.
COPY ./requirements/base.txt ./
RUN pip3 --no-cache-dir install -r ./base.txt

COPY . /usr/src/app

# expose and run django dev server with non-root user.
USER appuser
EXPOSE 8000
ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
