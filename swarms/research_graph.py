# swarms/research_graph.py
from neo4j import GraphDatabase
import os

URI = os.getenv("NEO4J_URI","bolt://neo4j:7687")
USER = os.getenv("NEO4J_USER","neo4j")
PASS = os.getenv("NEO4J_PASS","password")

class ResearchGraph:
    def __init__(self, uri=URI, user=USER, password=PASS):
        self.driver = GraphDatabase.driver(uri, auth=(user,password))
    def close(self): self.driver.close()
    def create_schema(self):
        with self.driver.session() as s:
            s.run("CREATE CONSTRAINT IF NOT EXISTS FOR (t:Threat) REQUIRE t.id IS UNIQUE")
            s.run("CREATE CONSTRAINT IF NOT EXISTS FOR (i:Indicator) REQUIRE i.value IS UNIQUE")
    def add_threat(self, tid, desc):
        with self.driver.session() as s:
            s.run("MERGE (t:Threat {id:$id}) SET t.description=$desc", id=tid, desc=desc)
    def link_indicator(self, tid, indicator):
        with self.driver.session() as s:
            s.run("MATCH (t:Threat {id:$tid}) MERGE (i:Indicator {value:$ind}) MERGE (t)-[:HAS_INDICATOR]->(i)", tid=tid, ind=indicator)
    def query_related(self, indicator):
        with self.driver.session() as s:
            res = s.run("MATCH (t:Threat)-[:HAS_INDICATOR]->(i:Indicator {value:$v}) RETURN t.id AS id", v=indicator)
            return [r["id"] for r in res]
