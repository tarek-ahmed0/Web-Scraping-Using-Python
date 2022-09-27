# LIBRARIES            
from bs4 import BeautifulSoup
from itertools import zip_longest
import requests
import csv
# FETCH THE PAGE URL
url = requests.get(r"https://wuzzuf.net/search/jobs/?q=Data+Analyst+&a=hpb")
# FETCH PAGE CONTENT / MARKUP
content = url.content
# PARSE CONTENT WITH BEAUTIFULSOUP
bs = BeautifulSoup(content, "lxml")
# FETCH ELEMENTS CONTAINING INFORMATION (WE NEED IT)
job_titles = bs.find_all("h2", {"class" : "css-m604qf"})
company_names = bs.find_all("a", {"class" : "css-17s97q8"})
company_locations = bs.find_all("span", {"class" : "css-5wys0k"})
job_skills = bs.find_all("div", {"class" : "css-y4udm8"})
job_status = bs.find_all("span", {"class" : "css-1ve4b75 eoyjyou0"})
# TEXT EXTARCTION FROM (FETCHED ELEMENTS)
# - EMPTY LISTS (To APPEND EXTARCTIONN TEXT INIT)
job_title_list = []
company_names_list = []
company_locations_list = []
job_skills_list = []
job_status_list = []
# - CREATE A FOR LOOP ( NUM OF TIMES : LEN(ELEMENTS) )
times = len(job_titles) 
for i in range(times) :
    job_title_list.append(job_titles[i].text)
    company_names_list.append(company_names[i].text)
    company_locations_list.append(company_locations[i].text)
    job_skills_list.append(job_skills[i].text)
    job_status_list.append(job_status[i].text)
# CREATE CSV FILE ( FILL WITH OUR DATA )
with open("D:\Web Scraping\Wuzzuf\jobstest.csv", "w") as data_analysis_file :
    writer = csv.writer(data_analysis_file)
    writer.writerow(["Job Title", "Company", "Location", "Skills", "Work Status", "Salary"])
    writer.writerows(zip_longest(*[job_title_list, company_names_list, company_locations_list, job_skills_list, job_status_list]))

