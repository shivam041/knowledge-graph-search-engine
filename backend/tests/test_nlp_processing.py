# backend/tests/test_nlp_processing.py

import sys
import os
import string

# Add the backend directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import unittest
from models.nlp_processing import extract_entities_and_relations

def normalize_entity(entity):
    """Remove punctuation from entity names for consistent comparison."""
    return entity.rstrip(string.punctuation + ' ')  # Remove trailing punctuation and spaces

class TestNLPProcessing(unittest.TestCase):

    def test_extract_entities_and_relations(self):
        text = "John is the CEO of Acme Corp. He joined the company in 2010."
        entities, relations = extract_entities_and_relations(text)
        
        expected_entities = [("John", "PERSON"), ("Acme Corp", "ORG"), ("2010", "DATE")]
        expected_relations = [("John", "is", "CEO"), ("He", "joined", "company")]

        self.assertEqual(entities, expected_entities)
        self.assertEqual(relations, expected_relations)

if __name__ == '__main__':
    unittest.main()