"""Gunicorn config.

Optimize Gunicorn to handle HTTP requests efficiently. Leverage multiple workers
and threads for concurrency. Set timeouts for graceful shutdowns, and log to
stdout/stderr.

Note:
    - Set module-wide ENV casting and defaults.
    - We define the casting here and not in `settings` for portability reasons
      (ie. when Gunicorn config is located elsewhere, like `/etc/gunicorn/`).

For more details on this module and available settings, see:
https://docs.gunicorn.org/en/stable/settings.html
"""

import multiprocessing
from typing import TypeAlias

import environ  # type: ignore[import-not-found]

NUM_CORES: int = multiprocessing.cpu_count()

env = environ.Env(  # type: ignore[misc]
    GUNICORN_BIND=(list, ["0.0.0.0:8000"]),
    # By default, allocate workers to CPU cores in a 1:1 ratio.
    GUNICORN_WORKERS=(int, NUM_CORES),
    GUNICORN_THREADS=(int, 2 * NUM_CORES),
    GUNICORN_WORKER_CLASS=(str, "gthread"),
    # For non-sync workers, `timeout` is not directly tied to the length of a
    # single request. Workers responding to master process `check-ins` won't
    # be killed due to a timeout.
    GUNICORN_TIMEOUT=(int, 90),
    GUNICORN_GRACEFUL_TIMEOUT=(int, 30),
    GUNICORN_LOG_LEVEL=(lambda v: str(v).lower(), "info"),  # type: ignore[misc]
    # Absolute path to log files.
    # Examples: `/var/log/gunicorn/access.log`, `/var/log/gunicorn/error.log`
    GUNICORN_ACCESS_LOG=(str, "-"),
    GUNICORN_ERROR_LOG=(str, "-"),
    # Match or exceed LB `keepalive` to upstream Gunicorn pm.
    # Tune based on infra design, traffic patterns, and connection pool needs.
    GUNICORN_KEEPALIVE=(int, 10),
    GUNICORN_PRELOAD_APP=(bool, True),
)

# == Logging ===================================================================

File: TypeAlias = str

accesslog: File = env("GUNICORN_ACCESS_LOG")
errorlog: File = env("GUNICORN_ERROR_LOG")
loglevel: str = env("GUNICORN_LOG_LEVEL")

# == Server (Mechanics) ========================================================
bind: list[str] = env("GUNICORN_BIND")

# == Server (Socket) ===========================================================
preload_app: bool = env("GUNICORN_PRELOAD_APP")

# == Workers ===================================================================
workers: int = env("GUNICORN_WORKERS")
worker_class: str = env("GUNICORN_WORKER_CLASS")
threads: int = env("GUNICORN_THREADS")
timeout: int = env("GUNICORN_TIMEOUT")
graceful_timeout: int = env("GUNICORN_GRACEFUL_TIMEOUT")
keepalive: int = env("GUNICORN_KEEPALIVE")
