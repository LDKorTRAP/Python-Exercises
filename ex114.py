import urllib
import urllib.request
try:
    site = urllib.request.urlopen("http://www.pudim.com.br/")
except urllib.error.URLError:
    print('O SITE NÃO ABRIU! SAD MONKEY')
else:
    print('O SITE ABRIU MACACO HEHE!')
