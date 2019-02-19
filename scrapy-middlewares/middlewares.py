# -*- coding: utf-8 -*-



from scrapy import signals
import random
from scrapy.conf import settings
from scrapy.http import HtmlResponse

class ProxyMiddleware(object):
    def process_request(self, request, spider):
        proxy = random.choice(settings['PROXIES'])
        request.meta['proxy'] = proxy

class UAMiddleware(object):
    def process_request(self, request, spider):
        ua = random.choice(settings['USER_AGENT_LIST'])
        request.headers['User-Agent'] = ua

class LoginMiddleware(object):
    def __init__(self):
        self.client = redis.StrictRedis()
    
    def process_request(self, request, spider):
        if spider.name == 'loginSpider':
            cookies = json.loads(self.client.lpop('cookies').decode())
            request.cookies = cookies
	

class SeleniumMiddleware(object):
    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver')
    def process_request(self, request, spider):
        if spider.name == 'seleniumSpider':
            self.driver.get(request.url)
            time.sleep(2)
            body = self.driver.page_source
        return HtmlResponse(self.driver.current_url,
                           body=body,
                           encoding='utf-8',
                           request=request)