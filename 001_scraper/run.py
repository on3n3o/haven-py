import requests
import re

visited = []
data = requests.get('http://ulanelectronics.pl')
emails = []
links = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', data.text)
# print(links)
links = list(set(links))
for val in links:
    if val not in visited:
        print(val)
        visited.append(val)
        data = requests.get(val)
        found_emails = re.findall(r'([\d\w\.]+@[\d\w\.\-]+\.\w+)', data.text)
        emails.append(found_emails)
        print(found_emails)

print(visited)
print(emails)