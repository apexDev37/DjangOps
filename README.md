# DjangOps
<!-- markdownlint-disable MD013 -->
[![Inline docs](https://inch-ci.org/github/dwyl/hapi-auth-jwt2.svg?branch=master)](https://github.com/apexDev37/DjangOps/blob/main/README.md) [![Python version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue?style=flat&logo=python&logoColor=yellow)](https://github.com/apexDev37/DjangOps/blob/main/tox.ini#L5) [![docker](https://img.shields.io/badge/docker-enabled-blue?style=flat&logo=docker&labelColor=white)](https://www.docker.com/products/docker-desktop/) [![Known Vulnerabilities](https://snyk.io/test/github/apexDev37/DjangOps/main/badge.svg)](https://snyk.io/test/github/apexDev37/DjangOps) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-blue.svg)](http://makeapullrequest.com) [![Activity](https://img.shields.io/badge/status-active-brightgreen)](https://github.com/apexDev37/DjangOps/commits/main) [![Versioning](https://img.shields.io/badge/versioning-semver-black?logo=semver)](https://semver.org/) [![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit) [![Linter: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff) [![Style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
<!-- markdownlint-enable MD013 -->

> A simple devops-inspired template for Django applications setup with compose.

<!-- markdownlint-disable MD033 -->
<img src="./resources/docs/images/django.png" style="width:25%;" alt="Django™"/>
<img src="./resources/docs/images/docker.png" style="width:29%;" alt="Docker™"/>
<!-- markdownlint-disable MD033 -->

## Introduction

If you need a quick start with Django and Compose, you're in the right place.
DjangOps is a dev-ops-inspired template for perfectionists with deadlines,
who also happen to love Django and compose! Spin up a local dev environment
with modular custom settings in a few steps and focus on the value you want to
build. All comments, feedback, and contributions are highly encouraged.
I always love to hear and learn from the community❤

Learn more about the Django framework from the official [documentation].

## Installing / Getting started

This is an overview of the minimal setup needed to get started.

### Prerequisites

- [Git]
- [Docker Desktop] (latest version)
- IDE/Code/Text editor ([PyCharm], [VScode], [Vim], etc)

Follow these tutorials to set up Docker and Compose on either [Mac]
or [Linux].  
I'd recommend Microsoft's documentation to set up [Docker on WSL2] if you're on Windows.

### Local Setup

> The following setup was run on Ubuntu focal (20.04.6 LTS)

You can clone this repo with the following command.

- Clone repository

```bash
# cd your/desired/target/dir
git clone git@github.com:apexDev37/DjangOps.git my-project
cd my-project
```

> 🛈 This will clone the repository to a target dir on your host machine with
 a custom name `my-project/` and navigate into its root dir.

### Configuration

> The following commands assume execution occurs at the project root.

Before running your application with Compose, configure [environment] variables
and [secrets] expected by the Compose app model. Sample `env` and `secret`
files are provided to configure the following services: `web` and `db`. You can
create the required config files with the following `make` target commands.
After the config files are created, replace the placeholders and empty `txt`
files with your custom values.

> 🛈 `secret` files should store sensitive or confidential data, whereas `env`
files can contain other environment-related config.  

- Create required config files

```bash
make envs && make secrets  # idempotent operations.
```

> 🛈 This will create and output all config files generated from available
sample files in their target directory
(ie. `django.env.example` -> `django.env`).  

- Update placeholder config values  

> 💡 `secret` files intended to store keys or passwords are auto-populated with
> a random, cryptographic, base64-encoded value.

### Launch

You're all set to run your Django application.
Spin up your Django and Postgres instances with the following command.

- Spin up containers

```bash
docker compose down
docker compose up -d
```

> 🛈 This will create and start the Django and Postgres instances in the same
network defined in the base `compose` file.

Once the containers have been created and started, you can access the
application at <http://localhost:8000>
<img
src="./resources/docs/images/successful-django-install.PNG"
alt="Successful Django Install Page"
/>

## Development

This is an overview to prepare working with this repo locally.

### Virtual Environment

You can use any tool of your choice to create a [PEP 405 compliant] virtual
environment. The following example uses `virtualenvwrapper` to create and
manage virtual environments.

- Create a virtual environment

```bash
mkvirtualenv -p python3.12 djangops-py312
```

> 🛈 This will create a fully managed venv and activate the virtual environment
by default.

If your environment is not activated from the above command or you encounter
any issue, manually activate it with the following command.

- Activate the virtual environment

```bash
workon djangops-py312
```

### Dependencies

> ⚠ All following commands assume execution occurs with an active virtual env
at the project root.

- Install requirements for development.

```bash
make requirements
```

> 🛈 This will install and sync the active environment with the
pinned versions for your development dependencies, `requirements/dev.txt`.

- Set up `pre-commit` hooks

```bash
pre-commit install --install-hooks
```

> 🛈 This one time setup installs the `pre-commit` script in your hidden
`git/hooks` directory and installs all hook environments defined in the config
file.

### Runtime

Run the process for the Django development server in the `web` service. You can
use the following `make` target command to run the `develop` compose override
model, which supports _hot-reload_ by watching and syncing your local files
into the container.

- Run Compose services in watch (develop) mode.

```bash
make -f compose.Makefile watch.dev
```

You can also choose to spin up a more light-weight `web` service to handle only
test-related concerns.

- Run Compose services in watch (testing) mode.

```bash
make -f compose.Makefile watch.test
```

## Licensing

To make a repository open source, you must license it so that others may freely
use, modify, and distribute the software. Using the [MIT license], this project
ensures this. The full original text version of the license may be seen [here].

[//]: # "These are reference links used in the body of this note and get stripped out when the markdown processor does
its job. There is no need to format nicely because it shouldn't be seen.
Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax"

<!-- Introduction links -->

[documentation]: https://docs.djangoproject.com/en/

<!-- Installing / Getting Started links -->

[Git]: https://git-scm.com/
[Docker Desktop]: https://www.docker.com/products/docker-desktop/
[Mac]: https://docs.docker.com/desktop/install/mac-install/
[Linux]: https://docs.docker.com/desktop/install/linux-install/
[Docker on WSL2]: https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-containers/
[PyCharm]: https://www.jetbrains.com/pycharm/
[VScode]: https://code.visualstudio.com/
[Vim]: https://www.vim.org/
[environment]: https://docs.docker.com/compose/environment-variables/set-environment-variables/
[secrets]: https://docs.docker.com/compose/use-secrets/

<!-- Developing -->
[PEP 405 compliant]: https://peps.python.org/pep-0405/#specification

<!-- Licensing links -->

[MIT license]: https://en.wikipedia.org/wiki/MIT_License
[here]: https://choosealicense.com/licenses/mit/
