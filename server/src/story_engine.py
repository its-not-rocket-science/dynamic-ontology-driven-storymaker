"""
Module containing the logic for generating and updating stories
"""
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from .ontology_manager import OntologyManager


class StoryEngine:
    """ Class for generating and updating stories based on user input. """

    def __init__(self, ontology_file, model_name="gpt2"):
        self.ontology_manager = OntologyManager(ontology_file)
        self.model = GPT2LMHeadModel.from_pretrained(model_name)
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        
        self.tokenizer.pad_token = self.tokenizer.eos_token # pylint:disable=no-member
        self.tokenizer.pad_token_id = self.tokenizer.eos_token_id # pylint:disable=no-member

    def generate_story(self, prompt):
        """ Generates sequences of token ids using the user prompt."""
        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=512,
        )
        outputs = self.model.generate(
            inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_length=100,
            num_return_sequences=1,
            pad_token_id=self.tokenizer.pad_token_id
        )
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

    def update_story(self, user_input):
        """ Update ontology based on user input."""
        self.ontology_manager.add_character("NewCharacter", "Hero")
        self.ontology_manager.add_relationship(
            "NewCharacter", "ExistingCharacter", "allyOf")
        return self.generate_story(user_input)

    def visualize_story(self):
        """ Return a JSON representation of the ontology graph."""
        graph_data = {
            "nodes": [],
            "edges": []
        }
        for s, p, o in self.ontology_manager.ontology:
            graph_data["nodes"].append(str(s))
            graph_data["edges"].append(
                {"from": str(s), "to": str(o), "label": str(p)})
        return graph_data
