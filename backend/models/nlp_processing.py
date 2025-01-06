# backend/models/nlp_processing.py

import spacy
import string

def normalize_entity(entity):
    """Remove punctuation from entity names for consistent comparison."""
    return entity.rstrip(string.punctuation + ' ')  # Remove trailing punctuation and spaces

def extract_entities(text):
    """Extract entities from the text using spaCy."""
    nlp = spacy.load("en_core_web_trf")
    doc = nlp(text)
    extracted_entities = [(ent.text, ent.label_) for ent in doc.ents]  # Extract entities and their types
    return extracted_entities

def extract_entities_and_relations(text):
    nlp = spacy.load("en_core_web_trf")  # Initialize nlp here
    extracted_entities = extract_entities(text)  # Call the new extract_entities function
    doc = nlp(text)
    entities = [(normalize_entity(entity), entity_type) for entity, entity_type in extracted_entities]
    relations = []

    for sent in doc.sents:
        for token in sent:
            # Capture relations where the verb is "is" and has an attribute
            if token.dep_ == "attr" and token.head.pos_ == "VERB":
                subj = [child for child in token.head.children if child.dep_ in ("nsubj", "nsubjpass")]
                for s in subj:
                    relations.append((normalize_entity(s.text), token.head.text, normalize_entity(token.text)))

            # Example rule: If a token is a verb and has two noun children, consider it a relation
            if token.pos_ == "VERB":
                subjects = [child for child in token.children if child.dep_ in ("nsubj", "nsubjpass")]
                objects = [child for child in token.children if child.dep_ in ("dobj", "pobj")]
                for subj in subjects:
                    for obj in objects:
                        relations.append((normalize_entity(subj.text), token.text, normalize_entity(obj.text)))

    return entities, relations

# Example usage
text = "John is the CEO of Acme Corp. He joined the company in 2010."
entities, relations = extract_entities_and_relations(text)
print("Entities:", entities)
print("Relations:", relations)