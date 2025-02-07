# src/user_interaction.py
class UserInteraction:
    def __init__(self, story_engine):
        self.story_engine = story_engine

    def start_story(self, prompt):
        print("Welcome to Diongenix! Let's create a story together.")
        if not prompt:
            return "Generated text does not conform to the ontology."
        # prompt = input("Enter a starting point for the story: ")
        story = self.story_engine.generate_story(prompt)
        print("\nGenerated Story:\n", story)
        return story

    def make_choice(self, choice):
        # choice = input("\nWhat happens next? (Enter your choice): ")
        updated_story = self.story_engine.update_story(choice)
        print("\nUpdated Story:\n", updated_story)
        return updated_story