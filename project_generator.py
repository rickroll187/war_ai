# project_generator.py
"""
Creates baseline folder structure & placeholder files.
Run once if you want automatic scaffolding before pasting real files.
"""
import os

FILES = [
"main.py","docker-compose.yml","Dockerfile","requirements.txt","setup.sh","Makefile",".env.template",
"config/config.py",
"utils/agent_client.py",
"blockchain/ethereum.py","blockchain/solana.py",
"blockchain/hardhat/contracts/ThreatLogger.sol",
"blockchain/hardhat/contracts/CTISharing.sol",
"blockchain/hardhat/contracts/IncidentResponse.sol",
"blockchain/hardhat/scripts/deploy.js",
"blockchain/hardhat/hardhat.config.js",
"cybersecurity/threat_detection.py","cybersecurity/threat_intel.py",
"red_team/operations.py","red_team/authorization.py",
"blue_team/incident_response.py",
"crypto_monitoring/wallet_tracker.py","crypto_monitoring/watchlist.py",
"swarms/github_triage.py","swarms/research.py","swarms/research_graph.py","swarms/observability.py",
"websocket_server.py","websocket_client.py",
"api_server.py","api/marketplace.py",
"dashboard/main_dashboard.py","dashboard/traces_ui.py",
"database/models.py",
"tests/test_all.py",
"README.md","USAGE_GUIDE.md"
]

def main():
    for p in FILES:
        d = os.path.dirname(p)
        if d and not os.path.exists(d): os.makedirs(d, exist_ok=True)
        if not os.path.exists(p):
            with open(p,"w") as f:
                f.write(f"# placeholder: {p}\n")
    print("Scaffold created. Edit files with content from repository.")

if __name__=="__main__":
    main()
