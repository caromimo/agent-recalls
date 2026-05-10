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

## Data

The data used for this project is not included in the current repository. You can download the csv file from [Open Government](https://open.canada.ca/data/en/dataset/d38de914-c94c-429b-8ab1-8776c31643e3) and place it in the `recall_agent/data` folder. This is the structure of the recall_agent directory:

```
recall_agent/
├── data/
│   └── HCRSAMOpenData.csv     <-- Put your csv here!
├── tools/
│   ├── __init__.py
│   └── database_tools.py      <-- Put your duckdb queries here!
├── agent.py                   <-- Only contains the Agent definition
```

## Important Note
Never put your api keys in the code. Ensure they are loaded using the environment variables.
