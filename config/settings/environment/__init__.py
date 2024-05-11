"""Environment settings for Django project.

This module hosts all configuration settings for the project
that preferably should be part of the environment.

Note:
    Discover app env vars that can be set in `BASE_DIR/.envs`.

Candidate settings:
    - App name and versioning.
    - Sensitive or confidential information.
    - DB connection settings, Backend services, Security, Logging, etc.
    - Dynamic or varying settings likely to vary between deploys.

12-factor Compliant:
See: https://12factor.net/config
"""
