# from bs4 import BeautifulSoup

# def detectLinks(s):
# 	soup = BeautifulSoup(s,"lxml")
# 	links = soup.findAll('a', href=True)
# 	for link in links:
# 		print (link['href'],",",link.text)

# def detectLinks(s):
# 	stringList = s.split("\n")
# 	resultList = []
# 	for line in stringList:
# 		tmp = line.split("a href=")
# 		if len(tmp)==1: continue
# 		link = tmp[1].split("\"")[1]
# 		title = tmp[1].split("</a>")[0].split(">")[1]
# 		resultList.append("{},{}".format(link,title))
# 	return resultList

import re

def detect_links(html):
    links = re.findall(r'<\s*a [^>]*href="([^"]*)"[^>]*>(.*?)</a', html)
    return ((href.strip(), re.sub('<[^>]*>', '', title.strip())) for href, title in links)

if __name__ == '__main__':
    import sys
    print '\n'.join('%s,%s' % link for link in detect_links(sys.stdin.read()))

# if __name__ == '__main__':
# 	    import sys
#     s = sys.stdin.read()
#     for result in detectLinks(s):
#         print (result)
