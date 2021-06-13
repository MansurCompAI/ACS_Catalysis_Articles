# importing libraries
from bs4 import BeautifulSoup
from datetime import date, datetime, timedelta
import requests


today = date.today()
# Conditions for selecting issues
issue = float(input('Choose the year of issue (the oldest issue is 2011) >>> '))
def issues(issue):
    if ((issue < 2020) and (issue > 2010)):
        url_issue = 'https://pubs.acs.org/loi/accacs/group/d2010.y'+str(int(issue))
    elif issue >= 2020:
        url_issue ='https://pubs.acs.org/loi/accacs/group/d2020.y'+str(int(issue))
    else:
        print('Sorry, the oldest available issue year is 2011')
        url_issue = None

# setting urls and extractions    
    if url_issue != None:
        html_text = requests.get(url_issue).text
        soup = BeautifulSoup(html_text, 'lxml')
        all_issue = soup.find_all('div', class_='parent-item')
        info_list = []
        for sp_issue in all_issue:
            issue_date = sp_issue.find('span', class_='coverDate').text
            link = sp_issue.a['href']
            volume_num = sp_issue.find('span', class_='comma').text
            info = { 'Date': issue_date,
                     'Volume_num': volume_num,
                     'Issue_num': 'Issue '+str(link.split('/')[-1]),
                     'Link':'https://pubs.acs.org'+str(link)
                    }
            info_list.append(info)
    else:
        print('Error date')  
    

    return info_list

issues = issues(issue)

# displaying the extracted issues and informations
for i, j in enumerate(issues):
    for keys, values in j.items():
        print(f' {keys} : {values}')
    print('====='*12, '\n')
    
print(f'The year of {int(issue)} has the {i} issues')
print('***'*12, '\n')

# final url for extraction
def sel_issue(iss_num):
    data = issues[-iss_num]
    url_final = data['Link']
    return url_final


