import threading
from queue import Queue
from urllib.request import urlopen


# import Queue   # python 2
# import urllib2  # python 2, urlib includes urllib2 libraries

# 1 multi threading using functions
# called by each thread
def get_url(q, url):
    q.put(urlopen(url).read())


theurls = ["http://google.com", "http://yahoo.com"]

q = Queue()

for u in theurls:
    t = threading.Thread(target=get_url, args=(q, u))
    t.daemon = True
    t.start()

s = q.get()
print(s)
