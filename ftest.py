from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time

class TwitTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		
	def TearDown(self):
		self.browser.quit()
		
	#def test_browser_title(self):
		#self.browser.get('http://localhost:8000')
		#self.assertIn('Blog Content', self.browser.title)
		#self.fail('Finish the test now!?')
		
		
	def check_rows_para_sa_list_ng_user(self, row_text):
		table = self.browser.find_element_by_id('ContentList')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])
		
	def test_start_list_and_retrieve_it(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('Twit Twit', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Spill the Twit!', headerText)
		name = self.browser.find_element_by_id('name')
		bio = self.browser.find_element_by_id('bio')
		inputContent = self.browser.find_element_by_id('Content')
		self.assertEqual(inputContent.get_attribute('placeholder'),'Write your content here.')
		name.send_keys('Gelyn Dinapo')
		time.sleep(1)
		bio.send_keys('Coz im only human')
		time.sleep(1)
		inputContent.send_keys('I went to park and met my old friends.')
		time.sleep(1)
		inputCode= self.browser.find_element_by_id('Codename')
		self.assertEqual(inputCode.get_attribute('placeholder'),'Enter your codename.')
		inputCode.send_keys('Mashiiro Ame')
		time.sleep(1)
		LogIn = self.browser.find_element_by_id('btnPost')
		LogIn.click()
		time.sleep(1)
		self.check_rows_para_sa_list_ng_user('1: I went to park and met my old friends.')
		
#second input to ni 1st user ahh
		
		inputContent = self.browser.find_element_by_id('Content')
		self.assertEqual(inputContent.get_attribute('placeholder'),'Write your content here.')
		inputContent.send_keys('I tried to cook but i burned the sunny side up egg')
		time.sleep(1)
		inputCode= self.browser.find_element_by_id('Codename')
		self.assertEqual(inputCode.get_attribute('placeholder'),'Enter your codename.')
		inputCode.send_keys('Mashiiro Ame')
		time.sleep(1)
		LogIn = self.browser.find_element_by_id('btnPost')
		LogIn.click()
		time.sleep(1)
		self.check_rows_para_sa_list_ng_user('2: I tried to cook but i burned the sunny side up egg')
'''	-

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
		
if __name__=='__main__':
	unittest.main(warnings='ignore')