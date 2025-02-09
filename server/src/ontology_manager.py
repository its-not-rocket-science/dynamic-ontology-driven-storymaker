""" Module for managing the ontology graph. """
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF


class OntologyManager:
    """ Class for managing the ontology graph. """

    def __init__(self, ontology_file):
        self.ontology = Graph()
        self.ontology.parse(ontology_file, format="xml")
        self.ns = Namespace("http://example.org/ontology#")

    def add_character(self, name, role):
        """ Add a character to the ontology. """
        character_uri = self.ns[name]
        self.ontology.add((character_uri, RDF.type, self.ns.Character))
        self.ontology.add((character_uri, self.ns.hasRole, Literal(role)))

    def add_relationship(self, entity1, entity2, relationship):
        """ Add a relationship between two entities. """
        entity1_uri = self.ns[entity1]
        entity2_uri = self.ns[entity2]
        self.ontology.add((entity1_uri, self.ns[relationship], entity2_uri))

    def save_ontology(self, output_file):
        """ Save the ontology to a file. """
        self.ontology.serialize(destination=output_file, format="xml")
