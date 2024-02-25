from pyld import jsonld
import json

# Read the JSON-LD document from a file
with open('cerkoryn-drep.json', 'r') as file:
    document = json.load(file)

# Canonize the document using the RDF Dataset Normalization Algorithm (URDNA2015)
normalized_document = jsonld.normalize(
    document, {'algorithm': 'URDNA2015', 'format': 'application/n-quads'}
)

# Write the canonized document to a file
with open('cerkoryn-drep-normalized.rdf', 'w') as file:
    file.write(normalized_document)
