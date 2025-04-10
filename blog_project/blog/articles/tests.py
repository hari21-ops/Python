from django.test import TestCase

# Create your tests here.
class SanityTest(TestCase):
    def test_basic_math(self):
        self.assertEqual(2 + 2, 4)
