#!/bin/bash

# Set up the project environment

# Create a virtual environment
echo "Creating a virtual environment..."
python -m venv venv

# Activate the virtual environment
echo "Activating the virtual environment..."
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Download the pre-trained model
echo "Downloading the pre-trained model..."
python -c "from transformers import GPT2LMHeadModel, GPT2Tokenizer; GPT2LMHeadModel.from_pretrained('gpt2'); GPT2Tokenizer.from_pretrained('gpt2')"

# Set up the data directory
echo "Setting up the data directory..."
mkdir -p data

# Download or create the ontology files
echo "Downloading or creating ontology files..."
if [ ! -f "data/fantasy_ontology.owl" ]; then
    echo "Creating fantasy_ontology.owl..."
    cat <<EOL > data/fantasy_ontology.owl
<rdf:RDF
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:owl="http://www.w3.org/2002/07/owl#"
    xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
    xmlns:fantasy="http://example.org/fantasy#">

    <!-- Classes -->
    <owl:Class rdf:about="http://example.org/fantasy#Character"/>
    <owl:Class rdf:about="http://example.org/fantasy#Race"/>
    <owl:Class rdf:about="http://example.org/fantasy#Location"/>
    <owl:Class rdf:about="http://example.org/fantasy#MagicSystem"/>

    <!-- Properties -->
    <owl:ObjectProperty rdf:about="http://example.org/fantasy#hasRace">
        <rdfs:domain rdf:resource="http://example.org/fantasy#Character"/>
        <rdfs:range rdf:resource="http://example.org/fantasy#Race"/>
    </owl:ObjectProperty>

    <owl:ObjectProperty rdf:about="http://example.org/fantasy#livesIn">
        <rdfs:domain rdf:resource="http://example.org/fantasy#Character"/>
        <rdfs:range rdf:resource="http://example.org/fantasy#Location"/>
    </owl:ObjectProperty>

    <owl:ObjectProperty rdf:about="http://example.org/fantasy#usesMagic">
        <rdfs:domain rdf:resource="http://example.org/fantasy#Character"/>
        <rdfs:range rdf:resource="http://example.org/fantasy#MagicSystem"/>
    </owl:ObjectProperty>

    <!-- Instances -->
    <fantasy:Character rdf:about="http://example.org/fantasy#Aragorn">
        <fantasy:hasRace rdf:resource="http://example.org/fantasy#Human"/>
        <fantasy:livesIn rdf:resource="http://example.org/fantasy#Gondor"/>
    </fantasy:Character>

    <fantasy:Race rdf:about="http://example.org/fantasy#Elf"/>
    <fantasy:Race rdf:about="http://example.org/fantasy#Human"/>
    <fantasy:Race rdf:about="http://example.org/fantasy#Dwarf"/>

    <fantasy:Location rdf:about="http://example.org/fantasy#Gondor"/>
    <fantasy:Location rdf:about="http://example.org/fantasy#Rivendell"/>

    <fantasy:MagicSystem rdf:about="http://example.org/fantasy#ElementalMagic"/>
</rdf:RDF>
EOL
fi

echo "Setup complete! Run 'source venv/bin/activate' to activate the virtual environment."