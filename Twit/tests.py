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
		inputContent.send_keys('I went to park and met my old friends.')
		time.sleep(.1)
		inputCode= self.browser.find_element_by_id('Codename')
		self.assertEqual(inputCode.get_attribute('placeholder'),'Enter your codename.')
		inputCode.send_keys('Mashiiro Ame')
		time.sleep(.1)
		LogIn = self.browser.find_element_by_id('btnPost')
		LogIn.click()
		time.sleep(.1)
		self.wait_rows_para_sa_list_ng_user('1: I went to park and met my old friends.')
		
#second input to ni 1st user ahh
		
		inputContent = self.browser.find_element_by_id('Content')
		self.assertEqual(inputContent.get_attribute('placeholder'),'Write your content here.')
		inputContent.send_keys('I tried to cook but i burned the sunny side up egg')
		time.sleep(.1)
		inputCode= self.browser.find_element_by_id('Codename')
		self.assertEqual(inputCode.get_attribute('placeholder'),'Enter your codename.')
		inputCode.send_keys('Mashiiro Ame')
		time.sleep(.1)
		LogIn = self.browser.find_element_by_id('btnPost')
		LogIn.click()
		time.sleep(.1)
		self.wait_rows_para_sa_list_ng_user('2: I tried to cook but i burned the sunny side up egg')
		
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
		inputCode= self.browser.find_element_by_id('Codename')
		self.assertEqual(inputCode.get_attribute('placeholder'),'Enter your codename.')
		inputCode.send_keys('ScarletHeart')
		time.sleep(.1)
		LogIn = self.browser.find_element_by_id('btnPost')
		LogIn.click()
		time.sleep(.1)
		self.wait_rows_para_sa_list_ng_user('1: Ive been keeping all the letters that I wrote for you.')
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
		inputCode= self.browser.find_element_by_id('Codename')
		self.assertEqual(inputCode.get_attribute('placeholder'),'Enter your codename.')
		inputCode.send_keys('ScarletHeart')
		time.sleep(.1)
		LogIn = self.browser.find_element_by_id('btnPost')
		LogIn.click()
		time.sleep(.1)
		self.wait_rows_para_sa_list_ng_user('1: Ive been keeping all the letters that I wrote for you')
		SeconndUrl = self.browser.current_url
		self.assertRegex(SeconndUrl, '/blogblog/.+')
		self.assertNotEqual(viewlist_url, SeconndUrl)
		peaBody = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Ive been keeping all the letters that I wrote for you', peaBody)
		self.assertIn('2: Another sunny day has come and gone away', peaBody)		
		
		
'''

		table = self.browser.find_element_by_id('ContentList')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('1: I went to park and met my old friends. from Mashiiro Ame', [row.text for row in rows])
	
		#unang user
		inputUser = self.browser.find_element_by_id('NewContent')
		inputUser.click()
		time.sleep(1)
		inputContent.send_keys('I went to park and met my old friends.')
		inputPword= self.browser.find_element_by_id('Codename')
		inputPword.click()
		time.sleep(1)
		inputCode.send_keys('Mashiiro Ame')
		LogIn = self.browser.find_element_by_id('btnPost')
		LogIn.click()
		time.sleep(1)
		self.check_rows_para_sa_list_ng_user('1: I went to park and met my old friends.)# for Password1234')
	
		#second user
		inputUser = self.browser.find_element_by_id('NewContent')
		inputUser.click()
		time.sleep(1)
		inputUser.send_keys('Today, we got a lot of customer. Exhausted.')
		inputPword= self.browser.find_element_by_id('Codename')
		inputPword.click()
		time.sleep(1)
		inputPword.send_keys('Dominic')
		LogIn = self.browser.find_element_by_id('btnPost')
		LogIn.click()
		time.sleep(1)
		self.check_rows_para_sa_list_ng_user('2: Dominic')# for Password5678')
		
	def test_check_live_server(self):
		self.browser.get(self.live_server_url)
		#self.fail('Finish the test!')
		'''
		
#if __name__=='__main__':
#	unittest.main(warnings='ignore')
