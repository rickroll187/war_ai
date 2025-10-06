# WAR AI — Local/Docker Prototype

## Quickstart (local)
1. Copy `.env.template` -> `.env` and edit keys
2. `chmod +x setup.sh && ./setup.sh`
3. `make start`
4. API: http://localhost:8000
5. Dashboard: http://localhost:8501
6. Neo4j Browser: http://localhost:7474 (user: neo4j / pass: password)

## Safety
- Red-team disabled by default. To enable, set RED_TEAM_ENABLED=true and create an approval token file at path in `RED_TEAM_APPROVAL_FILE`.

## Structure
See the tree in the repo root. Extend agent calls in `utils/agent_client.py`.
