# backend/tests/test_knowledge_graph.py

import sys
import os

# Add the backend directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import unittest
from models.knowledge_graph import build_knowledge_graph

class TestKnowledgeGraph(unittest.TestCase):

    def test_build_knowledge_graph(self):
        entities = [("John", "PERSON"), ("Acme Corp", "ORG")]
        relations = [("John", "is", "CEO"), ("John", "joined", "company")]
        graph = build_knowledge_graph(entities, relations)

        self.assertTrue(graph.has_node("John"))
        self.assertTrue(graph.has_node("Acme Corp"))
        self.assertTrue(graph.has_edge("John", "CEO"))
        self.assertTrue(graph.has_edge("John", "company"))

if __name__ == '__main__':
    unittest.main()