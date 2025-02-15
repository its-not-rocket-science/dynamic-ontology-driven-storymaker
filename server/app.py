""" Main application file for the Flask server. """
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from src.story_engine import StoryEngine

app = Flask(__name__)
CORS(app)

# Initialize the StoryEngine with the fantasy ontology
fantasy_ontology_path = os.getenv(
    "FANTASY_ONTOLOGY", "data/fantasy_ontology.owl")
story_engine = StoryEngine(fantasy_ontology_path)


@app.route("/generate", methods=["POST"])
def generate_story():
    """
    Endpoint to generate a story based on a user prompt.
    """
    data = request.json
    prompt = data.get("prompt", "")
    story = story_engine.generate_story(prompt)
    return jsonify({"story": story})


@app.route("/update", methods=["POST"])
def update_story():
    """
    Endpoint to update the story based on user input.
    """
    data = request.json
    user_input = data.get("input", "")
    updated_story = story_engine.update_story(user_input)
    return jsonify({"story": updated_story})


@app.route("/visualize", methods=["GET"])
def visualize_story():
    """
    Endpoint to generate a visual map of the story's structure.
    """
    # This could return a JSON representation of the ontology graph
    graph_data = story_engine.visualize_story()
    return jsonify(graph_data)


if __name__ == "__main__":
    host = os.getenv("FLASK_RUN_HOST", "0.0.0.0")
    port = int(os.getenv("FLASK_RUN_PORT", "5000"))
    debugger = bool(os.getenv("FLASK_RUN_DEBUGGER", "False"))
    app.run(host=host, port=port, debug=debugger)
