# swarms/research.py
from .research_graph import ResearchGraph
import os, json, time

def run_query(query="ICS threat actor TTPs"):
    neo4j_uri = os.getenv("NEO4J_URI", "bolt://neo4j:7687")
    neo_user = os.getenv("NEO4J_USER", "neo4j")
    neo_pass = os.getenv("NEO4J_PASS", "password")
    g = ResearchGraph(neo4j_uri, neo_user, neo_pass)
    g.create_schema()
    node = f"threat_{int(time.time())}"
    g.add_threat(node, f"Auto summary for {query}")
    g.link_indicator(node, "indicator:example")
    g.close()
    return {"node": node}
