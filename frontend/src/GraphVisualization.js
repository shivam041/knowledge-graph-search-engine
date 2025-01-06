// frontend/src/components/GraphVisualization.js

import React, { useEffect } from 'react';
import cytoscape from 'cytoscape';

function GraphVisualization({ elements }) {
  useEffect(() => {
    cytoscape({
      container: document.getElementById('cy'),
      elements: elements,
      style: [
        {
          selector: 'node',
          style: {
            'background-color': '#007bff',
            label: 'data(label)',
          },
        },
        {
          selector: 'edge',
          style: {
            width: 3,
            'line-color': '#ccc',
            'target-arrow-color': '#ccc',
            'target-arrow-shape': 'triangle',
            'curve-style': 'bezier',
          },
        },
      ],
      layout: {
        name: 'grid',
        rows: 1,
      },
    });
  }, [elements]);

  return <div id="cy" style={{ width: '600px', height: '400px' }} />;
}

export default GraphVisualization;