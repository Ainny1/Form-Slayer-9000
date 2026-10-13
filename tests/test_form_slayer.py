import unittest
from form_slayer import inspect_html


class FormSlayerTests(unittest.TestCase):
    def test_detects_password_in_get_form(self):
        result = inspect_html('<form method="GET"><input name="pwd" type="password"></form>')
        self.assertEqual(result["form_count"], 1)
        self.assertTrue(any("Password field in GET" in x for x in result["forms"][0]["observations"]))

    def test_post_form_with_action(self):
        result = inspect_html('<form method="post" action="/submit"><input name="email"></form>')
        self.assertEqual(result["forms"][0]["method"], "post")
        self.assertEqual(result["forms"][0]["observations"], [])

    def test_empty_document(self):
        self.assertEqual(inspect_html("<html></html>")["form_count"], 0)


if __name__ == "__main__":
    unittest.main()
