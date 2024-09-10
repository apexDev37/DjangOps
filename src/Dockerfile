# syntax=docker/dockerfile:1

# ======================================================================================
# Stage 1: Build Environment
# ======================================================================================

ARG PYTHON_VERSION="3.12.6"
ARG ALPINE_VERSION="3.20"
FROM python:${PYTHON_VERSION}-alpine${ALPINE_VERSION} AS build-stage

LABEL \
  author="Eugene Mwangi" \
  contact="mwangi.em37@gmail.com" \
  version="0.3.6" \
  license="MIT"

WORKDIR /usr/src/app

# set python-specific env variables.
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
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
# Stage 2: Runtime environment (inherits from build stage)
# ======================================================================================

FROM build-stage AS final-stage

COPY ./src/ /usr/src/app/src

# expose and run django dev server with non-root user.
EXPOSE 8000
ENTRYPOINT ["python3"]
CMD ["src/manage.py", "runserver", "0.0.0.0:8000"]

# ======================================================================================
# Least-priviledge user mode (inherits from final stage)
# ======================================================================================

FROM final-stage AS local-rootless

ARG UID=1000
RUN <<EOF
adduser \
    --gecos "" \
    --home "/home/appuser" \
    --shell "/bin/shell" \
    --system \
    --uid "${UID}" \
    appuser
EOF

# set user-writeable, pytest cache dir for local target stages.
ENV PYTEST_ADDOPTS="-o cache_dir=/home/appuser/.pytest_cache"

FROM final-stage AS rootless

ARG UID=1000
RUN <<EOF
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

USER appuser

# ======================================================================================
# Environment: development (inherits from local rootless)
# ======================================================================================

FROM local-rootless AS env-develop

ENV ENVIRONMENT=develop
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=./requirements/dev.txt,target=./requirements/dev.txt \
    python3 -m pip install -r ./requirements/dev.txt

USER appuser
