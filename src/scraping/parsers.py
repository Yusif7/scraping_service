import requests
import codecs
from bs4 import BeautifulSoup as BS

# We add all function to one set
__all__ = ('work', 'dou')

# to bypass the server
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9,*/*;q=0.8'
}


def work(url, city=None, language=None):
    domain = 'https://www.work.ua'
    # Add url for request
    #url = 'https://www.work.ua/ru/jobs-kyiv-python/'
    jobs = []
    errors = []
    if url:
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
                        'company' : company,
                        'city_id': city,
                        'language_id': language
                    })
            else:
                errors.append({'url':url, 'title':'Div does not exist'})
        else:
            errors.append({'url':url, 'title':'Page do not response'})
    
    return jobs,errors


def rabota(url, city=None, language=None):
    domain = 'https://rabota.ua'
    jobs = []
    errors = []
    if url:
        # Add request
        resp = requests.get(url, headers=headers)
        # status code == 200 mean that we have answer form request
        if resp.status_code == 200:
            #Assign incoming content to soup variable and add type of parser
            soup = BS(resp.content,'html.parser')
            new_jobs = soup.find('div', attrs={'class','f-vacancylist-newnotfound'})
            if not new_jobs:
                # find main vacancy list , we use find when want to find one element
                table = soup.find('table', id = 'table_id')
                if table:
                    # if we want to find more than one element we use find_all
                    tr_list = table.find_all('tr', attrs={'id', True})
                    # find title, company, description into vacancy block 
                    for tr in tr_list:
                        # h2 in div
                        div = tr.find('div', attrs={'class' : 'card-body'})
                        if div:
                            title = div.find('p', attrs = {'class' : 'card-title'})
                            # a tag into h2 tag to find attribute we use a[href]
                            href = title.a['href']
                            # descriptionn 
                            content = div.p.text
                            company = 'No name'
                            p = div.find('p', attrs = {'class' : 'company name'})
                            
                            if p:
                                company = p.a.text
                            jobs.append({
                                'title' : title.text,
                                'url' : domain + href,
                                'description': content,
                                'company' : company,
                                'city_id': city,
                                'language_id': language
                            })
                else:
                    errors.append({'url':url, 'title':'Table does not exist'})
            else:
                errors.append({'url':url, 'title':'Page is empty'})
        else:
            errors.append({'url':url, 'title':'Page do not response'})
    
    return jobs,errors

def dou(url, city=None, language=None):
    #domain = 'https://jobs.dou.ua/vacancies/?category=Python'
    jobs = []
    errors = []
    if url:
        # Add request
        resp = requests.get(url, headers=headers)
        # status code == 200 mean that we have answer form request
        if resp.status_code == 200:
            #Assign incoming content to soup variable and add type of parser
            soup = BS(resp.content,'html.parser')
            # find main vacancy list , we use find when want to find one element
            main_div = soup.find('div', id = 'vacancyListId')
            if main_div:
                # if we want to find more than one element we use find_all
                li_list = main_div.find_all('li', attrs={'class', 'l-vacancy'})
                # find title, company, description into vacancy block 
                for li in li_list:
                    # h2 in div
                    title = li.find('div', attrs={'class', 'title'})
                    # a tag into h2 tag to find attribute we use a[href]
                    href = title.a['href']
                    cont = li.find('div', attrs={'class', 'sh-info'})
                    # descriptionn 
                    content = cont.text
                    company = 'No name'
                    a = title.find('a', attrs={'class', 'company'})
                    if a:
                        company = a.text
                    jobs.append({
                        'title' : title.text,
                        'url' : href,
                        'description': content,
                        'company' : company,
                        'city_id': city,
                        'language_id': language
                    })
            else:
                errors.append({'url':url, 'title':'Div does not exist'})
        else:
            errors.append({'url':url, 'title':'Page do not response'})
    
    return jobs,errors

if __name__ == '__main__':
    url = 'https://jobs.dou.ua/vacancies/?city=Kyiv&category=Python'
    jobs, errors = dou(url)
    # Create work.html in write mode
    h = codecs.open('work.txt','w','utf-8')
    # Write incoming information to html 
    h.write(str(jobs))
    h.close()