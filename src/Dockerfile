# syntax=docker/dockerfile:1

# This build-specific ARG is named `TARGET`
# to avoid conflict with Django's ENV `ENVIRONMENT`,
# which determines app settings to use.
ARG TARGET=production

# ======================================================================================
# Stage 1: Build Environment
# ======================================================================================

ARG PYTHON_VERSION="3.12.9"
ARG ALPINE_VERSION="3.21"
FROM python:${PYTHON_VERSION}-alpine${ALPINE_VERSION} AS build-stage

LABEL \
    author="Eugene Mwangi" \
    contact="mwangi.em37@gmail.com" \
    version="0.6.0" \
    license="MIT"

ENV BASE=/usr/src/app
WORKDIR $BASE
ENV APP=$BASE/src

# set pkg-manger specific env variables.
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PIP_NO_CACHE_DIR=1
ENV PIP_ROOT_USER_ACTION=ignore

# install app's base runtime dependencies.
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=./requirements/pip.txt,target=./requirements/pip.txt \
    --mount=type=bind,source=./requirements/base.txt,target=./requirements/base.txt \
    python3 -m pip install -r ./requirements/pip.txt \
    && python3 -m pip install -r ./requirements/base.txt

# ======================================================================================
# Least-privilege user mode (inherits from build stage)
# ======================================================================================

ARG UID=1000

FROM build-stage AS local-rootless

RUN <<EOF
export UID=${UID}
adduser \
    --gecos "" \
    --home "/home/appuser" \
    --shell "/bin/sh" \
    --system \
    --uid "${UID}" \
    appuser
EOF

# set user-writeable, pytest cache dir for local target stages.
ENV PYTEST_ADDOPTS="-o cache_dir=/home/appuser/.pytest_cache"

FROM build-stage AS rootless

RUN <<EOF
export UID=${UID}
adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --system \
    --no-create-home \
    --uid "${UID}" \
    appuser
EOF

# ======================================================================================
# Environment: testing (inherits from local rootless)
# ======================================================================================

FROM local-rootless AS env-testing

ENV ENVIRONMENT=testing
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=./requirements/test.txt,target=./requirements/test.txt \
    python3 -m pip install -r ./requirements/test.txt

# ======================================================================================
# Environment: development (inherits from local rootless)
# ======================================================================================

FROM local-rootless AS env-develop

ENV ENVIRONMENT=develop
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=./requirements/dev.txt,target=./requirements/dev.txt \
    python3 -m pip install -r ./requirements/dev.txt

# ======================================================================================
# Environment: production (inherits from rootless)
# ======================================================================================

FROM rootless AS env-production

ENV ENVIRONMENT=production
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=./requirements/prod.txt,target=./requirements/prod.txt \
    python3 -m pip install -r ./requirements/prod.txt

# ======================================================================================
# Final Stage: use build-arg to decide which environment to “bridge”
# ======================================================================================

# hadolint ignore=DL3006
FROM env-${TARGET} AS final-stage

# set python-specific env variables.
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY ./src/ $APP
EXPOSE 8000

# ======================================================================================
# Runtime: application execution (inherits from Final Stage)
# ======================================================================================

FROM final-stage AS local-runtime

# change ownership of src directory to non-root user for local targets.
# hadolint ignore=SC3028
RUN chown -R ${UID} "$APP"

USER appuser
ENTRYPOINT ["python3", "/usr/src/app/src/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]

FROM final-stage AS prod-runtime

USER appuser
ENTRYPOINT ["gunicorn", "config.wsgi:application"]
