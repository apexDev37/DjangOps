# ======================================================================================
# Stage 1: Build Environment
# ======================================================================================

ARG PYTHON_VERSION="3.12.4"
ARG ALPINE_VERSION="3.20"
FROM python:${PYTHON_VERSION}-alpine${ALPINE_VERSION} AS build-stage

LABEL \
  author="Eugene Mwangi" \
  contact="mwangi.em37@gmail.com" \
  version="0.2.4" \
  license="MIT"

WORKDIR /usr/src/app

# set python-specific dev env variables.
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

# install app's base runtime dependencies.
COPY ./requirements/base.txt ./requirements/
RUN pip3 --no-cache-dir install -r ./requirements/base.txt

COPY . /usr/src/app

# ======================================================================================
# Stage 2: Runtime environment (inherits from build stage)
# ======================================================================================

FROM build-stage AS final-stage

RUN <<EOF
addgroup -S docker
adduser -S --shell /bin/bash --ingroup docker appuser
EOF

# expose and run django dev server with non-root user.
USER appuser
EXPOSE 8000
ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]

# ======================================================================================
# Environment: devlopment (inherits from final stage)
# ======================================================================================

FROM final-stage AS env-develop
RUN pip3 --no-cache-dir install -r ./requirements/dev.txt
