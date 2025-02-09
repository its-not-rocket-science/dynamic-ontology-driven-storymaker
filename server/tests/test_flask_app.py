""" Integration tests for the Flask app. """
import unittest
import requests
import threading

from src.app import app


class TestFlaskApp(unittest.TestCase):
    """ Integration tests for the Flask app. """
    PORT = 5000
    BASE_URL =f"http://localhost:{PORT}"

    @classmethod
    def setUpClass(cls):
        cls.server_thread = threading.Thread(target=cls.run_flask_app)
        cls.server_thread.daemon = True
        cls.server_thread.start()
    @classmethod
    def run_flask_app(cls):
        # Run the Flask app
        app.run(port=cls.PORT, use_reloader=False)

    @classmethod
    def tearDownClass(cls):
        # Stop the Flask app (optional, as the thread is daemonized)
        pass

            
    def test_generate_story(self):
        """ Test story generation with a valid prompt. """
        response = requests.post(
            f"{self.BASE_URL}/generate",
            json={"prompt": "Once upon a time..."},
            timeout=10
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("story", response.json())

    def test_update_story(self):
        """ Test updating the story with user input. """
        response = requests.post(
            f"{self.BASE_URL}/update",
            json={"input": "Gandalf fought a dragon."},
            timeout=10
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("story", response.json())

    def test_visualize_story(self):
        """ Test the visualization of the story ontology. """
        response = requests.get(f"{self.BASE_URL}/visualize", timeout=10)
        self.assertEqual(response.status_code, 200)
        self.assertIn("nodes", response.json())
        self.assertIn("edges", response.json())


if __name__ == "__main__":
    unittest.main()
