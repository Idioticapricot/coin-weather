from orca_agent_sdk import AgentConfig, AgentServer

def handle_task(job_input: str) -> str:
    """Weather Agent - Returns hardcoded weather information"""
    return "Weather in Bangalore on December 6th: Partly cloudy, 24°C (75°F), 60% humidity, light breeze from the east. Perfect weather for travel!"

if __name__ == "__main__":
    config = AgentConfig(
        agent_id="5bbf48cf-62a2-4ab3-bd96-12344",
        receiver_address="CNZPCKCXOYLHTETIDFVNHTYJ76GP2A6EHQ2AMFYATWLBMK5NDVDECCR2OM",
        price_microalgos=1_000_000,
        agent_token="6a2235a5fcac88463ed27ead315e619e8c52ffb0f6e72a117b2504639418d704",
        remote_server_url="http://localhost:3000/api/agent/access",
        app_id=750368769,
    )

    AgentServer(config=config, handler=handle_task).run()