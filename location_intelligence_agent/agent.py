import os
import dotenv
from google.adk.agents.llm_agent import Agent

from tools import get_maps_mcp_toolset, get_bigquery_mcp_toolset

dotenv.load_dotenv()

PROJECT_ID = os.getenv('GOOGLE_CLOUD_PROJECT', 'project_not_set')
MAPS_API_KEY = os.getenv('MAPS_API_KEY', 'maps_api_key_not_set')

bigquery_mcp_toolset = get_bigquery_mcp_toolset()
maps_mcp_toolset = get_maps_mcp_toolset(maps_api_key=MAPS_API_KEY)

root_agent = Agent(
    model='gemini-3.1-pro-preview',
    name='root_agent',
    instruction="""Help the user answer questions by strategically combining insights from two sources:
    
    1. **BigQuery toolset:** Access demographic (inc. foot traffic index), product pricing, and historical sales data in the  mcp_bakery dataset. Do not use any other dataset.
    Run all query jobs from project id: {PROJECT_ID}.

    2. **Map Toolset:** User this for real-world location analytics, finding competition/places and calculating necessary travel routes.
    Include a hyperlink to an interactive map in your response where appropriate.
    """,
    tools=[bigquery_mcp_toolset, maps_mcp_toolset]
)
