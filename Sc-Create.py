import requests
print("""
█▀ █▀▀   █▀▀ █▀█ █▀▀ ▄▀█ ▀█▀ █▀▀
▄█ █▄▄   █▄▄ █▀▄ ██▄ █▀█ ░█░ ██▄
[Create Snapchat Account]
_________________________
By Fostn
Insta @f09l
Twitter @lwv5
Telegram Channel @ifostn
_________________________
""")
user = input("Enter Username : ")
email = input("Enter Email : ")
password = input("Enter Password : ")
url = (f"https://tufaah1.osc-fr1.scalingo.io/snapchat_register/?user={user}&email={email}&password={password}")
r = requests.get(url).json()
if r['error'] == 'Taken user':
	print('\n''Username Taken')
elif r['error'] == 'Something went wrong':
	print('Try another Email ')
else:
	print('[successfully created]')
	print('_'*21)
	print("Username : "+user)
	print('Email : '+email)
	print('Password : '+password)
	print('_'*21)
	print('[For More Tools Fowllow Me]')
