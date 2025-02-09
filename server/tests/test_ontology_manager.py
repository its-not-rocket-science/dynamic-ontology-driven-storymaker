""" Unit tests for the OntologyManager class. """
import unittest
from src.ontology_manager import OntologyManager
from rdflib import Graph


class TestOntologyManager(unittest.TestCase):
    """ Unit tests for the OntologyManager class. """

    def setUp(self):
        """ Initialize the OntologyManager with a mock ontology file. """
        self.ontology_file = "data/fantasy_ontology.owl"
        self.ontology_manager = OntologyManager(self.ontology_file)

    def test_add_character(self):
        """ Test adding a new character to the ontology. """
        self.ontology_manager.add_character("Gandalf", "Wizard")
        characters = list(self.ontology_manager.ontology.subjects(
            predicate=self.ontology_manager.ns.hasRole))
        # Ensure the character was added
        self.assertIn(self.ontology_manager.ns["Gandalf"], characters)

    def test_add_relationship(self):
        """ Test adding a relationship between two entities. """
        self.ontology_manager.add_relationship("Gandalf", "Frodo", "mentorOf")
        relationships = list(self.ontology_manager.ontology.triples(
            (self.ontology_manager.ns["Gandalf"], self.ontology_manager.ns["mentorOf"], self.ontology_manager.ns["Frodo"])))
        self.assertTrue(relationships)  # Ensure the relationship was added

    def test_save_ontology(self):
        """ Test saving the ontology to a file. """
        output_file = "data/test_output.owl"
        self.ontology_manager.save_ontology(output_file)
        saved_ontology = Graph()
        saved_ontology.parse(output_file, format="xml")
        # Ensure the saved ontology is not empty
        self.assertGreater(len(saved_ontology), 0)


if __name__ == "__main__":
    unittest.main()
