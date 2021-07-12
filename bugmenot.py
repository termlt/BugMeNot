import requests
from bs4 import BeautifulSoup as BS
import sys

print("Press 'Ctrl + C' to close the script.")

def main():
    website = input('Enter the URL: ')   

    if 'exit'.upper() in website:
        sys.exit()

    r = requests.get(f'http://bugmenot.com/view/{website}')

    html = BS(r.content, 'html.parser')

    no_site = 'This site has been barred from the bugmenot system.'
    not_found = 'No logins found.'

    nosite = html.find('p')
    notfound = html.find("div", {"id": "share-it"})

    if no_site in nosite:
        print('\nThis site has been barred from the bugmenot system.')

    elif not_found in notfound.text:
        print('\nNo logins found.')

    else:
        for i in html.find_all('article'):

            kbd = i.find_all('kbd')

            li = i.find('li', class_ = 'success_rate')

            print(f"\nUsername: {kbd[0].text}\nPassword: {kbd[1].text} \nSuccess rate: {li.text.strip(' success rate')}\n")


while True:
    print()
    main()                