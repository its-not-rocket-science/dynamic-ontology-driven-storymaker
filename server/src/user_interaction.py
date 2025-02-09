""" Module to handle user interaction with the story engine. """


class UserInteraction:
    """ Class to handle user interaction with the story engine. """
    def __init__(self, story_engine):
        self.story_engine = story_engine

    def start_story(self, prompt):
        """ Generate a story based on the user prompt. """
        if not prompt:
            return "Generated text does not conform to the ontology."
        story = self.story_engine.generate_story(prompt)
        return story

    def make_choice(self, choice):
        """ Update the story based on user input. """
        updated_story = self.story_engine.update_story(choice)
        return updated_story
