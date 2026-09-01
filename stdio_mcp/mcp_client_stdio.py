import os 
from mcp.client.stdio import stdio_client
from mcp import ClientSession, StdioServerParameters, client
import asyncio


# Path to the MCP server script
mcp_server_script = os.path.join((os.path.dirname(os.path.abspath(__file__))),"mcp_server_stdio.py")

# Create Server Parameters
server_params = StdioServerParameters(
    command="python",
    args=[str(mcp_server_script)],
    env={}
)


# Create a Client Session
async def main():

    async with stdio_client(server_params) as (read,write):
        
        async with ClientSession(read,write) as session:

            await session.initialize()
            # Fetch the tools
            tools = await session.list_tools()
            print("Available tools:", tools)

            # Use the fetch tool
            result = await session.call_tool("send_data",arguments={"data":"Sending data from the client."})
            print("Result:", result)


if __name__ == "__main__":
    asyncio.run(main())