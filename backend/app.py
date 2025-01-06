# backend/app.py

import warnings

# Suppress specific FutureWarning from PyTorch
warnings.filterwarnings("ignore", category=FutureWarning, message=r"torch.load")

from flask import Flask, request, jsonify
from flask_cors import CORS
from models.nlp_processing import extract_entities_and_relations
from models.knowledge_graph import build_knowledge_graph
from utils.graph_visualization import visualize_graph

app = Flask(__name__)
CORS(app)

@app.route('/search', methods=['POST'])
def search():
    text = request.json.get('text')
    entities, relations = extract_entities_and_relations(text)
    graph = build_knowledge_graph(entities, relations)
    visualize_graph(graph)
    return jsonify({'entities': entities, 'relations': relations})

if __name__ == '__main__':
    app.run(debug=True)