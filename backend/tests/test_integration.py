# backend/tests/test_nlp_processing.py

import unittest
import string
from models.nlp_processing import extract_entities_and_relations

def normalize_entity(entity):
    """Remove punctuation from entity names for consistent comparison."""
    return entity.translate(str.maketrans('', '', string.punctuation + ' '))  # Added space to handle trailing spaces

class TestNLPProcessing(unittest.TestCase):

    def test_extract_entities_and_relations(self):
        text = "John is the CEO of Acme Corp. He joined the company in 2010."
        entities, relations = extract_entities_and_relations(text)
        
        # Normalize entities for comparison
        normalized_entities = [(normalize_entity(ent[0]), ent[1]) for ent in entities]
        expected_entities = [("John", "PERSON"), ("Acme Corp", "ORG"), ("2010", "DATE")]
        normalized_expected_entities = [(normalize_entity(ent[0]), ent[1]) for ent in expected_entities]

        expected_relations = [("He", "joined", "company")]

        self.assertEqual(normalized_entities, normalized_expected_entities)
        self.assertEqual(relations, expected_relations)

if __name__ == '__main__':
    unittest.main()