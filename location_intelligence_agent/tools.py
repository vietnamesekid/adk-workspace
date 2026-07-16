from google.adk.tools.mcp_tool import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams
import google.auth
import google.auth.transport.requests

MAPS_MCP_URL = "https://mapstools.googleapis.com/mcp"
BIGQUERY_MCP_URL = "https://bigquery.googleapis.com/mcp"

CONNECTION_TIMEOUT = 30.0
SSE_READ_TIMEOUT = 300.0


def get_maps_mcp_toolset(maps_api_key: str):
    return MCPToolset(
        connection_params=StreamableHTTPConnectionParams(
            url=MAPS_MCP_URL,
            timeout=CONNECTION_TIMEOUT,
            sse_read_timeout=SSE_READ_TIMEOUT,
            headers={
                'X-Goog-Api-Key': maps_api_key
            }
        )
    )


def get_bigquery_mcp_toolset():
    credentials, project_id = google.auth.default(
        scopes=["https://www.googleapis.com/auth/bigquery"]
    )

    credentials.refresh(google.auth.transport.requests.Request())
    oauth_token = credentials.token

    return MCPToolset(
        connection_params=StreamableHTTPConnectionParams(
            url=BIGQUERY_MCP_URL,
            timeout=CONNECTION_TIMEOUT,
            sse_read_timeout=SSE_READ_TIMEOUT,
            headers={
                'Authorization': f'Bearer {oauth_token}',
                'x-goog-user-project': project_id
            }
        )
    )
