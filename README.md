Overview
- Conversational AI assistant that coordinates drone operations (pilots, drones, missions) for Skylark Drones using structured data derived from pilot_roster.csv, drone_fleet.csv, and missions.csv.

Core Logic
- Implemented in a DroneAgent class in agent.py, which loads pilot, drone, and mission tables into pandas.

- Supports querying pilot availability, filtering drones by capability and weather resistance, calculating pilot cost for a mission, matching pilots to missions by skills/certifications/location, and running simple conflict and risk checks such as budget and weather suitability.

User Interface
- A Streamlit app in app.py exposes a chat-style web interface where users type prompts like pilots available bangalore, match PRJ001, drones thermal, or assign P001 PRJ001 and receive structured JSON-style results or confirmation messages in the browser.

Data Storage Options
- Works with local CSV files generated via setup_data.py for quick offline testing.

- Can also connect to Google Sheets using a service account and credentials.json, allowing pilot status and assignments to sync back to online sheets while reusing the same agent logic.

Running the App
- Installed dependencies, ensure the pilot, drone, and mission tables are available (CSV or Google Sheets), then start the interface with streamlit run app.py and drive all interactions through the chat.

