# Recall Expert

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
│   └── HCRSAMOpenData.csv          <-- Put your test csv here
├── tests/
│   ├── data/
│   |   └── TestData.csv            <-- Put your test csv here
│   └── test_database_tools.py      <-- Put your duckdb test queries here
├── tools/
│   ├── __init__.py
│   └── database_tools.py           <-- Put your duckdb queries here
├── agent.py                        <-- Define the agent here
```

## Important Note
Never put your api keys in the code. Ensure they are loaded using the environment variables.

## Testing
This project uses `pytest` for unit testing to ensure the reliability of the agent's database tools. 

To execute the test suite, run the following command from the root directory:

```bash
uv run pytest
```

To replicate the test data to ensure the same results from the tests, you can filter the recall dataset to include only recalls related to Drugs, Class Type III, reported between January 1, 2020 and May 9, 2026. Here is the query that can be run in after changing to the directory containing the data:


```bash
uv run duckdb
copy(
    select * from 'TestHCRSAMOpenData.csv' 
    where Category = 'Drugs' 
    and "Recall class" = 'Type III' 
    and "Last updated" > '2019-12-31' 
    and Archived = '0') 
to 'TestData.csv';
```
