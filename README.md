# taskbuilder

[![Check and Build](https://github.com/emp7yhead/taskbuilder/actions/workflows/CI.yml/badge.svg)](https://github.com/emp7yhead/taskbuilder/actions/workflows/CI.yml)
[![codecov](https://codecov.io/gh/emp7yhead/taskbuilder/branch/main/graph/badge.svg?token=RvuYDLaMEb)](https://codecov.io/gh/emp7yhead/taskbuilder)
[![Maintainability](https://api.codeclimate.com/v1/badges/11d87ec3ec61a945b6e9/maintainability)](https://codeclimate.com/github/emp7yhead/taskbuilder/maintainability)
![Docker Image Size (tag)](https://img.shields.io/docker/image-size/emptyhead/taskbuilder/latest)

Build system to automate and speed up routine processes

API documentation can be found [here](https://taskbuilder-production.up.railway.app/docs)

## Requirements

- Mac / Linux
- Docker version 23.0.5
- Docker Compose version v2.17.3
- GNU Make

## Main Dependencies

- python = "^3.11"
- fastapi = "^0.99.1"
- pydantic = "^1.10.9"
- PyYAML = "^6.0"
- uvicorn = "^0.22.0"

## Installation

- Clone repository

    ```bash
    git clone git@github.com:emp7yhead/taskbuilder.git
    ```

- You could fill the `.env` file:

  - `builds_dir` - directory for builds files. Default is `builds`.
  - `builds_file` - file with builds. Default is `builds.yml`
  - `tasks_file` - file with tasks dependecies. Default is `tasks.yml`

- Install all dependencies and start app by executing command:

    ```bash
    make run
    ```

- Go to 0.0.0.0:5000

### Docker

You always can use docker image for:

- installation

  ```bash
  docker pull emptyhead/taskbuilder --platform linux/x86_64
  ```

- run app

  ```bash
  docker run -ti -p 5000:5000 emptyhead/taskbuilder
  ```

## Functionality

- Get build tasks and it dependecies by sending POST request on `/tasks`

  Example request:

  ```bash
  curl -X 'POST' \
    'http://0.0.0.0:5000/tasks/' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
    "build": "write_beautiful"
  }'
  ```

- Get available builds by sending GET request on `/builds`

  Example request:

  ```bash
  curl -X 'GET' \
    'http://0.0.0.0:5000/builds/' \
    -H 'accept: application/json'
  ```

- Check build tasks GET request on `/builds/{build_name}`

  Example request:

  ```bash
  curl -X 'GET' \
    'http://0.0.0.0:5000/builds/front_arm' \
    -H 'accept: application/json'
  ```

- Healtcheck of service by sending GET request in `/healtcheck`

