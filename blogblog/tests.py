from django.test import TestCase
from blogblog.models import Item, Youser
from blogblog.views import tweet
'''from django.urls import resolve
from blogblog.views import tweet'''

class TweetTest(TestCase):
		
	def test_usestemplate(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'tweet.html')


class ORMTest(TestCase):

	def test_saveretrievelist(self):
		newYou = Youser()
		newYou.save()
		txtItem1=Item()
		txtItem1.youId = newYou
		txtItem1.text='one'
		txtItem1.feelId ='feel1'
		txtItem1.codeId ='code1'
		txtItem1.descId ='desc1'
		txtItem1.save()
		txtItem2=Item()
		txtItem2.youId = newYou
		txtItem2.text= 'two'
		txtItem2.feelId ='feel2'
		txtItem2.codeId ='code2'
		txtItem2.descId ='desc2'
		txtItem2.save()
		saved_Items = Item.objects.all()
		savedYouser = Youser.objects.first()
		self.assertEqual(saved_Items.count(),2)
		savedItem1 = saved_Items[0]
		savedItem2 = saved_Items[1]
		self.assertEqual(savedItem1.text, 'one')
		self.assertEqual(savedItem2.text, 'two')
		self.assertEqual(savedItem1.codeId, 'code1')
		self.assertEqual(savedItem2.codeId, 'code2')
		self.assertEqual(savedItem1.feelId, 'feel1')
		self.assertEqual(savedItem2.feelId, 'feel2')
		self.assertEqual(savedItem1.descId, 'desc1')
		self.assertEqual(savedItem2.descId, 'desc2')
		self.assertEqual(savedItem1.youId, newYou)
		self.assertEqual(savedItem2.youId, newYou)
		
class ViewTest(TestCase):

	def test_displaysAll(self):
		newYou = Youser.objects.create()
		Item.objects.create(youId=newYou, text= 'Danielle Teves')
		Item.objects.create(youId=newYou, text= 'Milleth Marupok')
		response = self.client.get(f'/blogblog/{newYou.id}/')
		self.assertContains(response,'Danielle Teves')
		self.assertContains(response,'Milleth Marupok')
		self.assertNotContains(response,'Rica Pretty')
		self.assertNotContains(response,'Dale Mabilis')
		
		newYou_2 = Youser.objects.create()
		Item.objects.create(youId=newYou_2, text= 'Rica Pretty')
		Item.objects.create(youId=newYou_2, text= 'Dale Mabilis')
		response = self.client.get(f'/blogblog/{newYou_2.id}/')
		self.assertContains(response,'Rica Pretty')
		self.assertContains(response,'Dale Mabilis')
		self.assertNotContains(response,'Danielle Teves')
		self.assertNotContains(response,'Milleth Marupok')
		
	def test_shareyourlist(self):
		newYou = Youser.objects.create()
		response = self.client.get(f'/blogblog/{newYou.id}/')
		self.assertTemplateUsed(response, 'tweet2.html')
		
	def test_pasalistpage(self):
		Twit1 = Youser.objects.create()
		Twit2 = Youser.objects.create()
		passList = Youser.objects.create()
		response = self.client.get(f'/blogblog/{passList.id}/')
		self.assertEqual(response.context['yId'],passList) 
		
class NewListTest(TestCase):
	def test_savepostrequest(self):
		response = self.client.post('/blogblog/newlist_url', data = {'Content':'Content','Feeling':'Feeling','Codename':'Codename','Description': 'Description'})
		#self.assertIn('Content', response.content.decode())
		#self.assertTemplateUsed(response, 'tweet.html')
		
		self.assertEqual(Item.objects.count(), 1)
		newItem = Item.objects.first()
		self.assertEqual(newItem.text, 'Content')
		self.assertEqual(newItem.codeId, 'Codename')
		self.assertEqual(newItem.descId, 'Description')
		
	def test_redirectingPOST(self):
		response = self.client.post('/blogblog/newlist_url', data = {'Content':'Content','Feeling':'Feeling','Codename':'Codename','Description': 'Description'})
		newlist = Youser.objects.first()
		self.assertRedirects(response, f'/blogblog/{newlist.id}/')
		
class AddItemTest(TestCase):
	def test_dagdagsaexistinglist(self):
		Twit1 = Youser.objects.create()
		Twit2 = Youser.objects.create()
		existingTwit = Youser.objects.create()
		self.client.post(f'/blogblog/{existingTwit.id}/addItem', data={'Content': 'New Content for existing','Feeling': 'New Feeling for existing','Codename': 'New Codename for existing','Description': 'New Description for existing'})
		self.assertEqual(Item.objects.count(),1)
		newItem =Item.objects.first()
		self.assertEqual(newItem.text,'New Content for existing')
		self.assertEqual(newItem.feelId,'New Feeling for existing')
		self.assertEqual(newItem.codeId,'New Codename for existing')
		self.assertEqual(newItem.descId,'New Description for existing')
		self.assertEqual(newItem.youId, existingTwit)

	def test_redirectstolistview(self):
		Twit1 = Youser.objects.create()
		Twit2 = Youser.objects.create()
		Twit3 = Youser.objects.create()
		existingTwit = Youser.objects.create()
		response = self.client.post(f'/blogblog/{existingTwit.id}/addItem', data={'Content': 'Content','Feeling':'Feeling','Codename':'Codename','Description': 'New Description for existing'})
		self.assertRedirects(response, f'/blogblog/{existingTwit.id}/')
	
	





