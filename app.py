from orca_agent_sdk import AgentConfig, AgentServer

def handle_task(job_input: str) -> str:
    """Weather Agent - Returns hardcoded weather information"""
    return "Weather in Bangalore on December 6th: Partly cloudy, 24°C (75°F), 60% humidity, light breeze from the east. Perfect weather for travel!"

if __name__ == "__main__":
    config = AgentConfig(
        agent_id="5bbf48cf-62a2-4ab3-bd96-123444444",
        receiver_address="NR45HQJA24SC3IT34KWS75SVOFV5AQ4I44ZWWCILBZE2BKRVOZIJQORHSU",
        price_microalgos=1_000_000,
        agent_token="e4d50c41242707a002b14b564667217543438afbb33c15e5668db27b7393db64",
        app_id=750371398,
    )

    AgentServer(config=config, handler=handle_task).run()