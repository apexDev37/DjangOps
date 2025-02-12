"""Gunicorn config.

Optimize Gunicorn to handle HTTP requests efficiently. Leverage multiple workers
and threads for concurrency. Set timeouts for graceful shutdowns, and log to
stdout/stderr.

For more details on this module and available settings, see:
https://docs.gunicorn.org/en/stable/settings.html
"""

import multiprocessing

bind = ["127.0.0.1:8000"]
workers = multiprocessing.cpu_count() * 2 + 1
threads = 3
worker_class = "gthread"
timeout = 120
graceful_timeout = 30
loglevel = "info"
accesslog = "-"
errorlog = "-"
keepalive = 10
preload_app = True
