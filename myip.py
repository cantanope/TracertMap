from requests import get

ip = get('https://api.ipify.org').content.decode('utf8')
list=[]
list.append('{}'.format(ip))
print(list)