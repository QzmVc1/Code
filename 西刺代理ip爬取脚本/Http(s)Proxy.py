import requests
from bs4 import BeautifulSoup
import logging
import sys
import random


def obtainProxy(UA):
	httpList = []
	httpsList = []
	url = 'https://www.xicidaili.com/nn/'

	for i in range(1,10):
		try:
			r = requests.get(url+str(i),headers={'User-Agent':random.choice(UA)})
		except:
			logger = logging.basicConfig(level=logging.INFO, format ='%(asctime)s - %(levelname)s - %(message)s')
			logger.error('Url cannot be requested normally.')
			sys.exit(0)
		else:
			bsp = BeautifulSoup(r.text,"lxml")
			proxyList = bsp.find("table",{"id":"ip_list"}).findAll("tr")[1:]
			for proxy in proxyList:
				form = "%s://%s:%s"
				tdList = proxy.findAll("td")
				if tdList[5].string.lower() == "http":
					httpList.append(form % (tdList[5].string.lower(),tdList[1].string,tdList[2].string))
				else:
					httpsList.append(form % (tdList[5].string.lower(),tdList[1].string,tdList[2].string))
	return httpList,httpsList

def checkProxy(UA):
	validHttpList,validHttpsList = obtainProxy(UA)
	# print("http:\n"+'*'*44)
	# print(httpList)
	# print('*'*40)
	# print("https:\n"+'*'*44)
	# print(httpsList)
	# print('*'*40)
	url = "https://www.baidu.com"

	for http in range(len(validHttpList)):
		try:
			r = requests.get(url,headers={'User-Agent':random.choice(UA)},timeout=5)
			if r.status_code != 200:
				del validHttpList[http]
		except Exception as e:
			print(e)

	for https in range(len(validHttpsList)):
		try:
			r = requests.get(url,headers={'User-Agent':random.choice(UA)},timeout=5)
			if r.status_code != 200:
				del validHttpsList[https]
		except Exception as e:
			print(e)
	return validHttpList,validHttpsList

if __name__ == '__main__':
	UserAgent = [
		"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
		"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
		"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0",
		"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
		"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
		"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
		"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
		"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
		"Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
		"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
		"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
		"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
		"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
		"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
		"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
		"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
		"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
	]
	httpList,httpsList = checkProxy(UserAgent)
	print("http:\n"+'*'*40)
	print(httpList)
	print('*'*40)
	print("https:\n"+'*'*40)
	print(httpsList)
	print('*'*40)


