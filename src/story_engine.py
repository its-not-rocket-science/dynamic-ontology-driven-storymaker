# src/story_engine.py
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from .ontology_manager import OntologyManager

class StoryEngine:
    def __init__(self, ontology_file, model_name="gpt2"):
        self.ontology_manager = OntologyManager(ontology_file)
        self.model = GPT2LMHeadModel.from_pretrained(model_name)
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    def generate_story(self, prompt):
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(inputs["input_ids"], max_length=100, num_return_sequences=1)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

    def update_story(self, user_input):
        # Update ontology based on user input
        self.ontology_manager.add_character("NewCharacter", "Hero")
        self.ontology_manager.add_relationship("NewCharacter", "ExistingCharacter", "allyOf")
        return self.generate_story(user_input)