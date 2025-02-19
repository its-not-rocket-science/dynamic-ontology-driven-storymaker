""" Unit tests for the StoryEngine class. """

import unittest
from src.story_engine import StoryEngine


class TestStoryEngine(unittest.TestCase):
    """ Unit tests for the StoryEngine class. """
    def setUp(self):
        """ Initialize the StoryEngine with a mock ontology file """
        self.ontology_file = "data/fantasy_ontology.owl"
        self.story_engine = StoryEngine(self.ontology_file)

    def test_generate_story(self):
        """ Test story generation with a valid prompt. """
        prompt = "Once upon a time in a land far, far away..."
        story = self.story_engine.generate_story(prompt)
        self.assertIsInstance(story, str)  # Ensure the output is a string
        self.assertGreater(len(story), 0)  # Ensure the output is not empty

    def test_update_story(self):
        """ Test updating the story with user input. """
        user_input = "Gandalf fought a dragon."
        updated_story = self.story_engine.update_story(user_input)
        # Ensure the output is a string
        self.assertIsInstance(updated_story, str)
        # Ensure the output is not empty
        self.assertGreater(len(updated_story), 0)

    def test_ontology_update_after_story_generation(self):
        """ Test if the ontology is updated after generating a story. """
        initial_characters = list(self.story_engine.ontology_manager.ontology.subjects(
            predicate=self.story_engine.ontology_manager.ns.hasRole))
        self.story_engine.update_story("A new character named Frodo appeared.")
        updated_characters = list(self.story_engine.ontology_manager.ontology.subjects(
            predicate=self.story_engine.ontology_manager.ns.hasRole))
        self.assertGreater(len(updated_characters), len(
            initial_characters))  # Ensure a new character was added

    def test_visualize_story(self):
        """ Test the visualization of the story ontology. """
        graph_data = self.story_engine.visualize_story()
        self.assertIsInstance(graph_data, dict)
        self.assertIn("nodes", graph_data)
        self.assertIn("edges", graph_data)


if __name__ == "__main__":
    unittest.main()
