import os
from dotenv import load_dotenv
from fastmcp import FastMCP # type: ignore

# Create the server instance
mcp = FastMCP("weather-server")

# Define a tool (like an API endpoint for the LLM)
@mcp.tool
def get_weather(city: str) -> str:
    """
    Returns fake weather info for a given city.
    Replace this with a real API call if needed.
    """
    if city.lower() == "paris":
        return "It's sunny in Paris with 25°C."
    elif city.lower() == "mumbai":
        return "Heavy rain expected in Mumbai, around 29°C."
    elif city.lower() == "hyderabad":
        return "Heavy rain expected in Hyderabad, around 31°C."
    elif city.lower() == "Delhi":
        return "Heavy rain expected in Delhi, around 25°C."
    else:
        return f"Sorry, I don't have real weather data for {city}."

# Run the MCP server
if __name__ == "__main__":
    mcp.run()
