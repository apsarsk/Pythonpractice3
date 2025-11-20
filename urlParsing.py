url='http://www.kaggle.com/datasets'
# protocol=url[:url.find(':')]
# dot1=url.find('.')
# dot2=url.find('.',dot1+1)
# domain=url[dot1+1:dot2]
# page=url[url.find('/',dot2):]
#
# print(protocol,domain,page)

protocol=url[:url.find(':')]
dot1=url.find('.')
dot2=url.find('.',dot1+1)
domain=url[dot1+1:dot2]
page=url[url.find('/',dot2):]
print(protocol)
print(domain)
print(page)