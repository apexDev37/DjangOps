# syntax=docker/dockerfile:1

# This build-specific ARG is named `TARGET`
# to avoid conflict with Django's ENV `ENVIRONMENT`,
# which determines app settings to use.
ARG TARGET=production

# ======================================================================================
# Stage 1: Build Environment
# ======================================================================================

ARG PYTHON_VERSION="3.12.11"
ARG ALPINE_VERSION="3.22"
FROM python:${PYTHON_VERSION}-alpine${ALPINE_VERSION} AS build-stage

LABEL \
    author="Eugene Mwangi" \
    contact="mwangi.em37@gmail.com" \
    version="0.6.7" \
    license="MIT"

# set global directories for src to live across all stages.
ENV BASE=/usr/src/app
WORKDIR $BASE
ENV APP=$BASE/src

# set pkg-manger specific env variables.
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_ROOT_USER_ACTION=ignore

# install app's base runtime dependencies.
ENV PIP_INSTALL="python3 -m pip install -r"
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=./requirements/pip.txt,target=./requirements/pip.txt \
    --mount=type=bind,source=./requirements/base.txt,target=./requirements/base.txt \
    ${PIP_INSTALL} ./requirements/pip.txt \
    && ${PIP_INSTALL} ./requirements/base.txt

# set shareable user and home arguments across stages.
# this comes last so that custom user args don't force a reinstall of base deps.
ARG UID=1000 APPUSER=appuser
ENV UID=${UID} APPUSER=${APPUSER}

# ======================================================================================
# Least-privilege user mode (inherits from build stage)
# ======================================================================================

FROM build-stage AS local-rootless

ENV APPUSER_HOME="/home/${APPUSER}"

# hadolint ignore=SC3028
RUN adduser \
    --gecos "" \
    --home "${APPUSER_HOME}" \
    --shell "/bin/sh" \
    --system \
    --uid "${UID}" \
    "${APPUSER}"

FROM build-stage AS rootless

# hadolint ignore=SC3028
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --system \
    --no-create-home \
    --uid "${UID}" \
    "${APPUSER}"

# ======================================================================================
# Environment: testing (inherits from local rootless)
# ======================================================================================

FROM local-rootless AS env-testing

ENV ENVIRONMENT=testing
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=./requirements/test.txt,target=./requirements/test.txt \
    ${PIP_INSTALL} ./requirements/test.txt

# ======================================================================================
# Environment: development (inherits from local rootless)
# ======================================================================================

FROM local-rootless AS env-develop

ENV ENVIRONMENT=develop
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=./requirements/dev.txt,target=./requirements/dev.txt \
    ${PIP_INSTALL} ./requirements/dev.txt

# ======================================================================================
# Environment: production (inherits from rootless)
# ======================================================================================

FROM rootless AS env-production

ENV ENVIRONMENT=production
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=./requirements/prod.txt,target=./requirements/prod.txt \
    ${PIP_INSTALL} ./requirements/prod.txt

# ======================================================================================
# Final Stage: use build-arg to decide which environment to “bridge”
# ======================================================================================

# hadolint ignore=DL3006
FROM env-${TARGET} AS final-stage

# set python-specific env variables.
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

COPY ./src/ "${APP}"
WORKDIR "${APP}"
EXPOSE 8000

# ======================================================================================
# Runtime: application execution (inherits from Final Stage)
# ======================================================================================

FROM final-stage AS local-runtime

# set user-writeable, pytest cache dir for local target stages.
ENV PYTEST_ADDOPTS="-o cache_dir=${APPUSER_HOME}/.cache/pytest/.pytest_cache"

# change ownership of src directory to non-root user for local targets.
# hadolint ignore=SC3028
RUN chown -R ${UID} "${APP}"

USER ${APPUSER}
ENTRYPOINT ["python3", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]

FROM final-stage AS prod-runtime

USER ${APPUSER}
ENTRYPOINT ["gunicorn", "--config", "gunicorn.conf.py", "config.wsgi:application"]
