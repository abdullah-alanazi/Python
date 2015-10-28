import urllib.request
from urllib.error import  URLError
import re


def newURL(url, domain):
	global log1
	if(len(log1)>100):
		return
	if(url in log1 and log1[url] == 1):
		return
	else:
		log1[url] = 1
		print("getting:::", url)
	try:
		sampleURL= urllib.request.urlopen(url)
		SCode=sampleURL.getcode()
		if(SCode == 200):
			con10t=sampleURL.read()
			con10t_1 = con10t.decode("utf-8")
			regexp_A = re.compile('<a>(?P<a>(.*))</a>')
			Samplekeywords = re.compile('<meta name="view" content="(?P<view>(.*))" />')
			regexpURL = re.compile("http://"+domain+"[/\w+]*")

			result = regexp_A.search(con10t_1, re.IGNORECASE)

			if result:
				A = result.group("a")
				print(A)

			result = Samplekeywords.search(con10t_1, re.IGNORECASE)

			if result:
				keyword1 = result.group("view")
				print(keyword1)

			for (urls) in re.findall(regexpURL, con10t_1):
					if(urls  not in log1 or log1[urls] != 1):
						log1[urls] = 0
						newURL(urls, domain)
	except URLError as e:
		print("ErrOr")

log1 = {}

seed = "http://www.newhaven.edu/"

log1[seed]=0

newURL(seed, "www.newhaven.edu")
