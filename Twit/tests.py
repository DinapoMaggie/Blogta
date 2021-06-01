from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException

waititing=3

class TwitTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		
	def TearDown(self):
		self.browser.quit()
		
	#def test_browser_title(self):
		#self.browser.get('http://localhost:8000')
		#self.assertIn('Blog Content', self.browser.title)
		#self.fail('Finish the test now!?')
		
		
	def wait_rows_para_sa_list_ng_user(self, row_text):
		start_time = time.time()
		while time.time()-start_time < waititing:
			time.sleep (.1)
		try:
			table = self.browser.find_element_by_id('ContentList')
			rows = table.find_elements_by_tag_name('tr')
			self.assertIn(row_text, [row.text for row in rows])
			return
		except (AssertionError,WebDriverException) as e:
			if time.time()-start_time > waititing:
				raise e
		
	def test_startlistandretrieveparasaUNAGUSER(self):
		self.browser.get(self.live_server_url)
		self.assertIn('Twit Twit', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Spill the Twit!', headerText)
		name = self.browser.find_element_by_id('name')
		bio = self.browser.find_element_by_id('bio')
		inputContent = self.browser.find_element_by_id('Content')
		self.assertEqual(inputContent.get_attribute('placeholder'),'Write your content here.')
		name.send_keys('Gelyn Dinapo')
		time.sleep(.1)
		bio.send_keys('Coz im only human')
		time.sleep(.1)
		
		inputFeel= self.browser.find_element_by_id('Feeling')
		inputFeel.send_keys('Happy')
		time.sleep(.1)
		
		inputContent.send_keys('I went to park and met my old friends.')
		time.sleep(.1)
		inputCode= self.browser.find_element_by_id('Codename')
		self.assertEqual(inputCode.get_attribute('placeholder'),'Enter your codename.')
		inputCode.send_keys('Mashiiro Ame')
		time.sleep(.1)
		
		inputdesc= self.browser.find_element_by_id('Description')
		inputdesc.send_keys('#BFFs')
		time.sleep(.1)
		
		LogIn = self.browser.find_element_by_id('btnPost')
		LogIn.click()
		time.sleep(.1)
		self.wait_rows_para_sa_list_ng_user('1: I went to park and met my old friends. Happy Mashiiro Ame #BFFs')
		
#second input to ni 1st user ahh
		
		inputContent = self.browser.find_element_by_id('Content')
		self.assertEqual(inputContent.get_attribute('placeholder'),'Write your content here.')
		inputContent.send_keys('I tried to cook but i burned the sunny side up egg')
		time.sleep(.1)
		inputFeel= self.browser.find_element_by_id('Feeling')
		inputFeel.send_keys('Greatful')
		time.sleep(.1)
		inputCode= self.browser.find_element_by_id('Codename')
		self.assertEqual(inputCode.get_attribute('placeholder'),'Enter your codename.')
		inputCode.send_keys('Mashiiro Ame')
		time.sleep(.1)
		inputdesc= self.browser.find_element_by_id('Description')
		inputdesc.send_keys('#BurnedEgg')
		time.sleep(.1)
		LogIn = self.browser.find_element_by_id('btnPost')
		LogIn.click()
		time.sleep(.1)
		self.wait_rows_para_sa_list_ng_user('2: I tried to cook but i burned the sunny side up egg Greatful Mashiiro Ame #BurnedEgg')
		
	def test_ibaibangURLkadauser(self):
		self.browser.get(self.live_server_url)
		self.assertIn('Twit Twit', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Spill the Twit!', headerText)
		name = self.browser.find_element_by_id('name')
		bio = self.browser.find_element_by_id('bio')
		inputContent = self.browser.find_element_by_id('Content')
		self.assertEqual(inputContent.get_attribute('placeholder'),'Write your content here.')
		inputContent.send_keys('Ive been keeping all the letters that I wrote for you.')
		time.sleep(.1)
		inputFeel= self.browser.find_element_by_id('Feeling')
		inputFeel.send_keys('Doubtful')
		time.sleep(.1)
		inputCode= self.browser.find_element_by_id('Codename')
		self.assertEqual(inputCode.get_attribute('placeholder'),'Enter your codename.')
		inputCode.send_keys('ScarletHeart')
		time.sleep(.1)
		inputdesc= self.browser.find_element_by_id('Description')
		inputdesc.send_keys('#letters')
		time.sleep(.1)
		LogIn = self.browser.find_element_by_id('btnPost')
		LogIn.click()
		time.sleep(.1)
		self.wait_rows_para_sa_list_ng_user('1: Ive been keeping all the letters that I wrote for you. Doubtful ScarletHeart #letters')
		viewlist_url = self.browser.current_url
		self.assertRegex(viewlist_url, '/blogblog/.+')
		
		self.browser.quit()
		self.browser =webdriver.Firefox()
		self.browser.get(self.live_server_url)
		peaBody = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Ive been keeping all the letters that I wrote for you', peaBody)
		time.sleep(.1)
		inputContent = self.browser.find_element_by_id('Content')
		self.assertEqual(inputContent.get_attribute('placeholder'),'Write your content here.')
		inputContent.send_keys('Another sunny day has come and gone away')
		time.sleep(.1)
		inputFeel= self.browser.find_element_by_id('Feeling')
		inputFeel.send_keys('Regretful')
		time.sleep(.1)
		inputCode= self.browser.find_element_by_id('Codename')
		self.assertEqual(inputCode.get_attribute('placeholder'),'Enter your codename.')
		inputCode.send_keys('ScarletHeart')
		time.sleep(.1)
		inputdesc= self.browser.find_element_by_id('Description')
		inputdesc.send_keys('#passingby')
		time.sleep(.1)
		LogIn = self.browser.find_element_by_id('btnPost')
		LogIn.click()
		time.sleep(.1)
		self.wait_rows_para_sa_list_ng_user('1: Another sunny day has come and gone away Regretful ScarletHeart #passingby')
		new_url = self.browser.current_url
		self.assertRegex(new_url , '/blogblog/.+')
		self.assertNotEqual(viewlist_url, new_url )
		peaBody = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Ive been keeping all the letters that I wrote for you Doubtful ScarletHeart #letters', peaBody)
		self.assertIn('Another sunny day has come and gone away Regretful ScarletHeart #passingby', peaBody)		
