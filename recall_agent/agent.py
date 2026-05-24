from google.adk.agents.llm_agent import Agent
from .tools.database_tools import Tool


# Instantiate the database tool with the default production path
tools = Tool()

# Define the agent
root_agent = Agent(
    model='gemini-2.5-flash',
    name='recall_agent',
    description='A helpful assistant to explore the recalls, advisories and safety alerts from Health Canada.',
    instruction='Answer user questions using the tools provided to you. If you do not have the tools to answer the question, politely let the user know that you cannot answer the question.',
    tools=[tools.count_recalls_by_month_and_year, tools.search_recalls_by_keyword],
)