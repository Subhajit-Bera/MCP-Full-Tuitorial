from langchain_mcp_adapters.client import MultiServerMCPClient
import os
import asyncio

# Path to the MCP server script
mcp_server_script = os.path.join((os.path.dirname(os.path.abspath(__file__))),"mcp_server_stdio.py")

# Path to the virtual environment
venv_path = os.path.join((os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),".venv")

async def main():
    # Create an instance of the MultiServerMCPClient
    client = MultiServerMCPClient(
    
    # MCP Server Config (JSON)
    {
        "data_process_mcp_stdio" : {
            "transport": "stdio",
            "command": os.path.join(venv_path, "Scripts", "python.exe"), # Use the Python executable from the virtual environment
            "args": [str(mcp_server_script)]  # Use the path to the MCP server script as an argument
        }
    }
    )
    
    # List the tools
    tools = await client.get_tools()
    print("Available tools:", tools)
    
    # Find the specific tool by name
    send_data_tool = next(t for t in tools if t.name == "send_data")
    
    # Invoke it using LangChain's async tool execution
    result = await send_data_tool.ainvoke({"data":"Sending data from the client."})
    print("Send Data Result:", result)
    
    

if __name__ == "__main__":
    asyncio.run(main())