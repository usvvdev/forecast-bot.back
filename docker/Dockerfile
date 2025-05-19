FROM python:3.11

ENV PROJECT_DIR="/code" \
    # python
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    # pip
    PIP_NO_CHACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # poetry
    POETRY_VERSION=1.8.2 \
    POETRY_VIRTUALENVS_CREATE=false \
    PATH="${PATH}:/root/.poetry/bin"

# Install necessary packages including wget, gnupg, curl, etc.
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    curl \
    unzip \
    apt-transport-https \
    ca-certificates \
    xvfb \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install --upgrade pip==24.0 \
    && pip install poetry==$POETRY_VERSION && poetry --version

# set working directory
WORKDIR $PROJECT_DIR

# copy dependencies only
COPY ./pyproject.toml ./poetry.lock ${PROJECT_DIR}/

# setting up proper permissions
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# copy project
COPY . ${PROJECT_DIR}/

# run contollers
# CMD ["python", "controller.py"]
