import unittest

class Settings:
    def __init__(self, url, newsSection):
        self.baseUrl = url
        self.newsSection = newsSection
    def getUrl(self):
        return self.baseUrl
    def getNewsUrl(self):
        return self.__consturctNewsUrl()
    def __consturctNewsUrl(self):
        return self.baseUrl + self.newsSection

class TestSettingsMethods(unittest.TestCase):
    # def test_that_settings_class_will_return_right_url(self):
    #     testUrl = "http://ya.ru"
    #     testNewsSection = "/news"
    #     settings = Settings(testUrl, testNewsSection)
    #     self.assertEqual(settings.getUrl(), testUrl)

    # def test_that_settings_class_will_return_right_news_url(self):
    #     testUrl = "http://ya.ru"
    #     testNewsSection = "/news"
    #     settings = Settings(testUrl, testNewsSection)
    #     self.assertEqual(settings.getNewsUrl(), testUrl + testNewsSection)

    def test_test(self):
        self.assertGreater(1, 2)

if __name__ == "__main__":
    unittest.main()