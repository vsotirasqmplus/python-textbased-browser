import sys
import os.path
from collections import deque
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style

my_stack = deque()
# my_stack.append('element')
# my_stack.pop()

# The information about the dir were confusing.
# They did not state if it is a direct argument and the argument should be named dir
# or there will be a named argument to identify in the sys.argv list.

# Also PyCharm was getting an error 13 PermissionsDenied
# which should be manually corrected via the terminal for the parent browser directory

ssl = 'https://'
dot_com = '.com'

directory = sys.argv[1]
if not os.path.exists(directory) or not os.path.isdir(directory):
    os.mkdir(directory, mode=0o777)
    os.chmod(directory, 0o777)

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

# urls = {'bloomberg.com': bloomberg_com, 'nytimes.com': nytimes_com}

while True:
    served = False

    url = input()
    url = url.lower()

    if url == 'back':
        if len(my_stack) > 0:
            # First pop the last served as it is the current
            url = my_stack.pop().pop()
            # Second pop the previous page
            # url = my_stack.pop()

    if url == 'exit':
        quit()

    full_url = url

    if url[-4:] != dot_com:
        full_url = url + dot_com
        # full_url = url
    else:
        url = url[0:-4]

    if url[-3:] == 'com':
        full_url = url[0:-3] + '.com'
        # full_url = url

    if url[-4:] == '.org':
        full_url = url

    if url[0:9] != 'https://':
        full_url = ssl + full_url

    dot = url.rfind('.')
    if dot > 0:
        file_name = directory + '/' + url[0:dot] + url[dot + 1:]
        # file_name = directory + '/' + url
    else:
        file_name = directory + '/' + url

    # print(f'Full URL [{full_url}] URL [{url}] URL-3 [{url[0:-3]}] Filename [{file_name}] Dir [{dir}]')

    with requests.get(full_url) as r:
        if 200 <= r.status_code < 300:
            my_stack.append(url)
            # print(f'Status [{r.status_code}]')
            served = True

            if not os.path.isfile(file_name):  # and url in urls:
                soup = BeautifulSoup(r.text, 'html.parser')
                with open(f'{file_name}', 'wt') as file:
                    for element in soup.find_all(['p', 'a', 'ol', 'ul', 'li']):
                        if element.name == 'a':
                            file.write(Fore.BLUE + element.get_text() + Fore.BLACK)
                        else:
                            file.write(element.get_text())

            if os.path.isfile(file_name):
                with open(f'{file_name}', 'rt') as file:
                    # content = file.read()
                    # soup = BeautifulSoup(content,'html.parser')
                    # print(soup.get_text())
                    for line in file:
                        print(line)

    if not served:
        print('error The Url cannot be found')
