import urllib.request

local_filename, headers = urllib.request.urlretrieve('http://python.org/')
html = open('page.txt', 'w')
html.close()