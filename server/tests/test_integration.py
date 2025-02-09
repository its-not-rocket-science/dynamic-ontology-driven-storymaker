""" Integration tests for the StoryEngine, UserInteraction, and StoryVisualizer. """
import unittest
from src.story_engine import StoryEngine
from src.user_interaction import UserInteraction
from src.visualization import StoryVisualizer
from rdflib import Graph


class TestIntegration(unittest.TestCase):
    """ Integration tests for the StoryEngine, UserInteraction, and StoryVisualizer. """
    def setUp(self):
        """ Initialize the StoryEngine, UserInteraction, and StoryVisualizer. """
        self.ontology_file = "data/fantasy_ontology.owl"
        self.story_engine = StoryEngine(self.ontology_file)
        self.user_interaction = UserInteraction(self.story_engine)
        self.ontology = Graph()
        self.ontology.parse(self.ontology_file, format="xml")
        self.visualizer = StoryVisualizer(self.ontology)

    def test_story_generation_and_interaction(self):
        """ Test the story generation and user interaction. """
        prompt = "Tell me about Gandalf."
        story = self.story_engine.generate_story(prompt)
        self.assertIsInstance(story, str)
        self.assertGreater(len(story), 0)

        updated_story = self.story_engine.update_story(
            "Gandalf fought a dragon.")
        self.assertIsInstance(updated_story, str)
        self.assertGreater(len(updated_story), 0)

    def test_visualization(self):
        """ Test the visualization of the story ontology. """
        self.visualizer.build_graph()
        self.assertGreater(len(self.visualizer.graph.nodes), 0)


if __name__ == "__main__":
    unittest.main()
