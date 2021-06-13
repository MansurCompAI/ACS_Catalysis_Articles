# importing libraries
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd
import os
from pretty_html_table import build_table
from datetime import date

today =date.today()
# reading and loading data 
data = pd.read_csv('articles.csv')
df = pd.DataFrame(data)
# Recieveing keywords from user
st = ''
keywords = []
while st != 'stop':
    filters = input('Insert the keywords (type "stop" for completing)  >>> ')
    if filters.lower() == 'stop':
        break
    else:
        keywords.append(filters)
        
# Filtering out according to keywords
idx_list = []
for i,j in enumerate(df['Title']):
    for word in keywords:
        if word in j:
            idx = i
            idx_list.append(idx)  # appending finding indeces
# print(idx_list)

Titles = []
Links = []
Authors = []

# extractions
for num in idx_list:
    Titles.append(df['Title'][num]) # assigning titles
    Links.append(df['Link'][num])  # assigning links
    Authors.append(df['Author_list'][num]) # assigning authorlist
# list in a list
Infos = [Titles, Links, Authors]   
new_df = pd.DataFrame(Infos, index=['Title', 'Link', 'Authors'])
new_df=new_df.T
new_df.to_csv('extracted.csv') # saving into csv file

# Sender funtion
def send_mail(body):
    message = MIMEMultipart()
    message['Subject'] = f'ACS catalysts update {today}'
    message['From'] = 'mansurbek.abdullayev1994@gmail.com'
    message['To'] = 'mansurbek.comchemai@gmail.com'
    pwd = os.environ.get('EMAIL_PASSWORD')
    body_content = body
    message.attach(MIMEText(body_content, "html"))
    msg_body = message.as_string()

    server = SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(message['From'], pwd)
    server.sendmail(message['From'], message['To'], msg_body)
    server.quit()

print('Keywords were accepted!\nFiltering out and Emailing are processing.... ')

# converting data into beatiful table and sending them through email
def send_email():
    data = build_table(new_df
                        , 'green_dark'
                        , font_size='medium'
                        , font_family='Open Sans,sans-serif'
                        , text_align='left'
                        , width='auto'
                        , index=False
			, even_color='black'
			, even_bg_color='white'
                        )
    send_mail(data)
    return print('Email was sent succesfully')

send_email()
