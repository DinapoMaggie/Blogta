from django.test import TestCase
from blogblog.models import Item
from blogblog.views import tweet
'''from django.urls import resolve
from blogblog.views import tweet'''

class TweetTest(TestCase):
	
	'''def test_tweetreturnstocorrectview(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'tweet.html')'''
		
	def test_usestemplate(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'tweet.html')
		
	def test_saveifneeded(self):
		response = self.client.get('/')
		self.assertEqual(Item.objects.count(), 0)
		
	def test_savepostrequest(self):
		response = self.client.post('/', data = {'Content':'Content'})
		#self.assertIn('Content', response.content.decode())
		#self.assertTemplateUsed(response, 'tweet.html')
		
		self.assertEqual(Item.objects.count(), 1)
		newItem = Item.objects.first()
		self.assertEqual(newItem.text, 'Content')
		
	def test_redirectingPOST(self):
		response = self.client.post('/', data = {'Content':'Content'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/blogblog/viewlist_url')
			
	def test_ididisplayyungitemsnitemplate(self):
		Item.objects.create(text= 'item1')
		Item.objects.create(text= 'item2')
		response = self.client.get('/')
		self.assertIn('item1', response.content.decode())
		self.assertIn('item2', response.content.decode())
		
		

class ORMTest(TestCase):

	def test_saveretrievelist(self):
		txtItem1=Item()
		txtItem1.text='one'
		txtItem1.save()
		txtItem2=Item()
		txtItem2.text= 'two'
		txtItem2.save()
		saved_Items=Item.objects.all()
		self.assertEqual(saved_Items.count(),2)
		savedItem1=saved_Items[0]
		savedItem2=saved_Items[1]
		self.assertEqual(savedItem1.text, 'one')
		self.assertEqual(savedItem2.text, 'two')
		
class ViewTest(TestCase):

	def test_displaysAll(self):
		Item.objects.create(text= 'Danielle Teves')
		Item.objects.create(text= 'Milleth Marupok')
		response = self.client.get('/blogblog/viewlist_url')
		self.assertContains(response,'Danielle Teves')
		self.assertContains(response,'Milleth Marupok')

# Create your tests here.
