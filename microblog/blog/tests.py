from django.test import TestCase

# Create your tests here.
class BlogTestCase(TestCase):

    def setUp(self) -> None:
        pass

    def test_index_access(self):
        self.assert_(True)