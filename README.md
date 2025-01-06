# Knowledge Graph Search Engine

A web-based Knowledge Graph Search Engine that constructs a knowledge graph from text documents and provides contextual answers to user queries. The system uses natural language processing (NLP) for text analysis and entity extraction, and visualizes relevant portions of the knowledge graph for each query result.

## Features

- **Knowledge Graph Construction:** Builds and maintains a knowledge graph using text documents as input.
- **NLP for Entity Extraction:** Utilizes spaCy for advanced text analysis and entity extraction.
- **Relation Detection:** Implements logic to determine relationships between entities.
- **Search Interface:** Accepts user queries and returns contextual answers.
- **Graph Visualization:** Interactive graph visualization with nodes and edges representing entities and relationships.

## UI/Style

- Sleek, minimalist interface with a focus on search and results.
- Interactive graph visualization with color-coded entities and relationships for easy distinction.

## Technologies and Libraries Used

### Languages

- **Python:** Used for backend development and NLP processing.
- **JavaScript:** Used for frontend development with React.

### Backend Libraries

- **Flask:** A lightweight WSGI web application framework for Python.
- **spaCy:** An open-source library for advanced NLP in Python.
- **NetworkX:** A Python package for the creation, manipulation, and study of complex networks.
- **Matplotlib:** A plotting library for Python, used for graph visualization.
- **Flask-CORS:** A Flask extension for handling Cross-Origin Resource Sharing (CORS).

### Frontend Libraries

- **React:** A JavaScript library for building user interfaces.
- **Cytoscape.js:** A graph theory library for visualization and analysis.

### Other Tools

- **Node.js and npm:** Used for managing frontend dependencies and running the development server.
- **pytest:** A testing framework for Python.
