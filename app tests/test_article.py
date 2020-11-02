import unittest
from app.models import Article

class TestArticle(unittest.TestCase):
    
    def setUp(self):
		
        self.new_article = Article("Joe", "New Title", "Short","randomsite.com","randomimage.jpg","11/02/20", "None")
    
    def test_instance(self):
       
        self.assertTrue(isinstance(self.new_article, Article))
    
    def test_init(self):
		
        self.assertEqual(self.new_article.author, "Joe")
        self.assertEqual(self.new_article.title, "New Title")
        self.assertEqual(self.new_article.description, "Short")
        self.assertEqual(self.new_article.url, "randomsite.com")
        self.assertEqual(self.new_article.img, "randomimage.jpg")
        self.assertEqual(self.new_article.date, "11/02/20")
        self.assertEqual(self.new_article.content, "None")
        

if __name__ == "__main__":
    unittest.main()
