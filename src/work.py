import requests
import codecs
from bs4 import BeautifulSoup as BS
# to bypass the server
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9,*/*;q=0.8'
}


def work(url):
    domain = 'https://www.work.ua'
    # Add url for request
    url = 'https://www.work.ua/ru/jobs-kyiv-python/'
    jobs = []
    errors = []
    # Add request
    resp = requests.get(url, headers=headers)
    # status code == 200 mean that we have answer form request
    if resp.status_code == 200:
        #Assign incoming content to soup variable and add type of parser
        soup = BS(resp.content,'html.parser')
        # find main vacancy list , we use find when want to find one element
        main_div = soup.find('div', id = 'pjax-job-list')
        if main_div:
            # if we want to find more than one element we use find_all
            div_list = main_div.find_all('div', attrs={'class', 'job-link'})
            # find title, company, description into vacancy block 
            for div in div_list:
                # h2 in div
                title = div.find('h2')
                # a tag into h2 tag to find attribute we use a[href]
                href = title.a['href']
                # descriptionn 
                content = div.p.text
                company = 'No name'
                logo = div.find('img')
                if logo:
                    company = logo['alt']
                jobs.append({
                    'title' : title.text,
                    'url' : domain + href,
                    'description': content,
                    'company' : company
                })
        else:
            errors.append({'url':url, 'title':'Page does not exist'})
    else:
        errors.append({'url':url, 'title':'Page do not response'})
    
    return jobs,errors


def rabota(url):
    domain = 'https://rabota.ua'
    jobs = []
    errors = []
    # Add request
    resp = requests.get(url, headers=headers)
    # status code == 200 mean that we have answer form request
    if resp.status_code == 200:
        #Assign incoming content to soup variable and add type of parser
        soup = BS(resp.content,'html.parser')
        # find main vacancy list , we use find when want to find one element
        main_div = soup.find('div', id = 'pjax-job-list')
        if main_div:
            # if we want to find more than one element we use find_all
            div_list = main_div.find_all('div', attrs={'class', 'job-link'})
            # find title, company, description into vacancy block 
            for div in div_list:
                # h2 in div
                title = div.find('h2')
                # a tag into h2 tag to find attribute we use a[href]
                href = title.a['href']
                # descriptionn 
                content = div.p.text
                company = 'No name'
                logo = div.find('img')
                if logo:
                    company = logo['alt']
                jobs.append({
                    'title' : title.text,
                    'url' : domain + href,
                    'description': content,
                    'company' : company
                })
        else:
            errors.append({'url':url, 'title':'Page does not exist'})
    else:
        errors.append({'url':url, 'title':'Page do not response'})
    
    return jobs,errors


if __name__ == '__main__':
    url = 'https://rabota.ua/zapros/python/%D0%BA%D0%B8%D0%B5%D0%B2'
    jobs, errors = rabota(url)
    # Create work.html in write mode
    h = codecs.open('work.txt','w','utf-8')
    # Write incoming information to html 
    h.write(str(jobs))
    h.close()