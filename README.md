# Recall Agent

## Purpose
The purpose of this project is to build an agent and specific tools to safely and effectively explore the publicly available [recalls, advisories and safety alers](https://recalls-rappels.canada.ca/en). The dataset is also available on [Open Government](https://open.canada.ca/data/en/dataset/d38de914-c94c-429b-8ab1-8776c31643e3).

## Tech Stack
This project is using [uv](https://docs.astral.sh/uv/) to manage packages. It is also leveraging the [Agent Development Kit (ADK)](https://adk.dev/) to build the agents and its tools.

## Set up
Create a .gitignore file in the parent folder. Add `**/*.env` to the file, to ensure that your gemini key does not get committed.

Once your gemini key is saved in the `.env` file in the root folder, you can start the adk web server by running the following command:
```shell 
uv run --env-file .env adk web
```