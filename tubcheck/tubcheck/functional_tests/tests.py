from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from pygeckodriver import geckodriver_path
import time


class OneTimeCheck(StaticLiveServerTestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox(executable_path=geckodriver_path)
        self.browser.implicitly_wait(3)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_upload_image_and_get_prediction(self):
        # user opens up page and sees it's has something to do with CheXNet
        self.browser.get(self.live_server_url)
        time.sleep(1)

        page_text = self.browser.find_element_by_tag_name('body').text

        self.assertIn('CheXNet', page_text)

        # form for uploading is there

        # user picks an image file and clicks upload button

        # page with prediction results opens up

        self.fail('Write the test!')
