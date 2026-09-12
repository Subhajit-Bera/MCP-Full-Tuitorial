from fastmcp import FastMCP

# Create an instance of FastMCP
mcp = FastMCP()

@mcp.tool
async def fetch_data_streamable_http():
    '''Used to fetch data from the server. '''
    
    return {'data': 'Data fetched successfully'}


@mcp.tool
async def send_data_streamable_http(data:str):
    '''Used to send data to the server. '''
    
    return {'data': f"Data sent to server: {data}"}



if __name__ == "__main__":
    mcp.run(transport='streamable-http',host="0.0.0.0",port=8080)