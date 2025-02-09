""" Unit tests for the UserInteraction class. """
import unittest
from src.user_interaction import UserInteraction
from src.story_engine import StoryEngine


class TestUserInteraction(unittest.TestCase):
    """ Unit tests for the UserInteraction class. """
    def setUp(self):
        """ Initialize the UserInteraction with a mock StoryEngine. """
        self.ontology_file = "data/fantasy_ontology.owl"
        self.story_engine = StoryEngine(self.ontology_file)
        self.user_interaction = UserInteraction(self.story_engine)

    def test_start_story(self):
        """ Test starting a story with a valid prompt. """
        prompt = "Tell me about Gandalf."
        story = self.user_interaction.start_story(prompt)
        self.assertIsInstance(story, str)  # Ensure the output is a string
        self.assertGreater(len(story), 0)  # Ensure the output is not empty

    def test_make_choice(self):
        """ Test making a choice to update the story. """
        self.user_interaction.start_story("Once upon a time...")
        updated_story = self.user_interaction.make_choice(
            "Gandalf fought a dragon.")
        # Ensure the output is a string
        self.assertIsInstance(updated_story, str)
        # Ensure the output is not empty
        self.assertGreater(len(updated_story), 0)

    def test_empty_prompt(self):
        """ Test starting a story with an empty prompt. """
        prompt = ""
        story = self.user_interaction.start_story(prompt)
        # Ensure empty prompts are handled
        self.assertEqual(
            story, "Generated text does not conform to the ontology.")


if __name__ == "__main__":
    unittest.main()
