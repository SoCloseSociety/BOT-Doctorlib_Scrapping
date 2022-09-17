from calendar import c
from itertools import count
from xml.dom.minidom import Document
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import random
import socket


from selenium.common.exceptions import (
    ElementNotVisibleException,
    ElementClickInterceptedException,
    WebDriverException,
    TimeoutException,
)
import pyautogui
import pyperclip
import csv
import pandas as pd
from glob import glob
import os 
import random


def is_connected():
  hostname = "one.one.one.one"  
  try:
    # see if we can resolve the host name -- tells us if there is
    # a DNS listening
    host = socket.gethostbyname(hostname)
    # connect to the host -- tells us if the host is actually reachable
    s = socket.create_connection((host, 80), 2)
    s.close()
    return True
  except Exception:
     pass # we ignore any errors, returning False
  return False




link = input("Enter Link : ")

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)  # version_main allows to specify your chrome version instead of following chrome global version
driver.maximize_window()

driver.get(link)  

while(True):
    try:
        driver.find_element(By.CLASS_NAME, 'results')
        break
    except:
        driver.close()
        os.system('nordvpn -c')
        time.sleep(10)

        while(True):
            if(is_connected()==False):
                os.system('nordvpn -c')
                time.sleep(10)
            elif(is_connected()==True):
                break    
                

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)  # version_main allows to specify your chrome version instead of following chrome global version
        driver.maximize_window()
        driver.get(link) 


time.sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

html = driver.page_source
soup = BeautifulSoup(html, features="html.parser")



result_section = soup.find_all("a", {"class": "dl-search-result-name js-search-result-path"})

profile_links = []
profile_subtitle_link = []

for a in soup.find_all('a', {"class": "dl-search-result-name js-search-result-path"}, href=True):
    profile_links.append(a['href'])


for s_t in soup.find_all('div', {"class": "dl-search-result-subtitle"}):
    profile_subtitle_link.append(s_t)




clean_profile_link = []



page = 2


while(True):
    try:
        driver.get(link+'/?page='+str(page)) 

        while(True):
            time.sleep(5)
            try:
                driver.find_element(By.XPATH, '//*[@id="doctor_search_bar"]')
                break
            except:
                driver.close()
                os.system('nordvpn -c')
                time.sleep(10)

                while(True):
                    if(is_connected()==False):
                        os.system('nordvpn -c')
                        time.sleep(10)
                    elif(is_connected()==True):
                        break    

                driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options) 
                driver.maximize_window()
                driver.get(link+'/?page='+str(page)) 
            
        try:
            driver.find_element(By.CLASS_NAME, 'results')
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            html = driver.page_source
            soup = BeautifulSoup(html, features="html.parser")
            for a in soup.find_all('a', {"class": "dl-search-result-name js-search-result-path"}, href=True):
                profile_links.append(a['href'])

            for s_t in soup.find_all('div', {"class": "dl-search-result-subtitle"}):
                profile_subtitle_link.append(s_t)
                
            page = page + 1

        except:
            break



    except:
        print("Major error occured")



print(len(profile_links))
print(len(profile_subtitle_link))

clean_profile_link = list(set(profile_links))


print(len(clean_profile_link))


dict = {'Profile_links': clean_profile_link} 
df = pd.DataFrame(dict)

df.to_csv('doctolib_profile_link.csv')



##############################################################################################################################
my_dr_name = []
my_dr_address = []
my_dr_skills = []
my_dr_degree_achivment = []


time.sleep(10)

with open('doctolib_profile_link.csv', 'r', encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        if '/' in row[1]:
            print(row[1])

            dr_address = []
            skills_list = []
            degree_achivment = []
            #contact_section = []
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)  # version_main allows to specify your chrome version instead of following chrome global version
            driver.maximize_window()
            driver.get("https://www.doctolib.fr"+row[1])  
            while(True):
                try:
                    driver.find_element(By.CLASS_NAME, 'dl-profile-header-name')
                    break
                except:
                    driver.close()
                    os.system('nordvpn -c')
                    time.sleep(10)

                    while(True):
                        if(is_connected()==False):
                            os.system('nordvpn -c')
                            time.sleep(10)
                        elif(is_connected()==True):
                            break    
                            

                    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options) 
                    driver.maximize_window()
                    driver.get("https://www.doctolib.fr"+row[1])


            time.sleep(5)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            html = driver.page_source
            soup = BeautifulSoup(html, features="html.parser")


            dr_name = soup.find("h1", {"class":"dl-profile-header-name"})
            my_dr_name.append(dr_name.text)

            result_section = soup.find("div", {"class": "dl-profile-address-picker-address-text"})

            pr_name = ''
            pr_name_address = ''

           

            try:
                practice_place = result_section.find_all('div')
                pr_name = practice_place[1].text
            except:
                print("Error!!")

            try:
                pr_name_address = practice_place[0].text
            except:
                print("Error")

            pr_name_address = pr_name_address.replace(pr_name, '')
            dr_address.append(pr_name + '->'+ pr_name_address)
            time.sleep(5)


            try:
                skills =  soup.find("div", {"id": "skills"})

                skill_list = skills.find_all("div", {"class":"dl-profile-skill-chip"})
                for skill_name in skill_list:
                    skills_list.append(skill_name.text)
            except Exception as e:
                print(e)
                print("Nope")

            degree_others = soup.find_all("div", {"class": "dl-profile-card-section dl-profile-history"})


            for  i in degree_others:
                header = i.find("h4", {"class": "dl-profile-card-title"})
                degree_achivment.append(header.text)
                degree_achivment.append("------------------------")

                try:
                    list = i.find_all("div", {"class": "dl-profile-text dl-profile-entry"})
                    for  j in  list:
                        ###
                        year = j.find("div", {"class":"dl-profile-entry-time"})
                        ###
                        achivment = j.find("div", {"class":"dl-profile-entry-label"})
                        try:
                            degree_achivment.append(year.text)
                        except:
                            degree_achivment.append("")

                        try:
                            degree_achivment.append(achivment.text)
                        except:
                            degree_achivment.append("")
                except:
                    print("Error")

            try:
                contact = soup.find("div", {"id":"openings_and_contact"})
                contact_2 = contact.find_all("div", {"class":"dl-profile-box"})
                for con  in contact_2:
                    cont_header = con.find("h4", {"class": "dl-profile-card-subtitle"})
                    cont_header = cont_header.text
                    if("Horaires d'ouverture" in cont_header):
                        pass
                    else:
                        cont_subtitle = con.find("div")
                        dr_address.append(cont_header)
                        dr_address.append("-------------")
                        dr_address.append(cont_subtitle.text)
            except:
                print("Not Find")

            present_link = row[1]
            present_link = present_link.split('?')[0]
            # print(present_link)

            tab_links = soup.find_all("div", {"class":"openings_and_contact"})

            for a in soup.find_all('a', {"class": "dl-text"}, href=True):
                if present_link in a['href']:
                    driver.get("https://www.doctolib.fr"+a['href'])  
                    while(True):
                        try:
                            driver.find_element(By.CLASS_NAME, 'dl-profile-header-name')
                            break
                        except:
                            driver.close()
                            os.system('nordvpn -c')
                            time.sleep(10)

                            while(True):
                                if(is_connected()==False):
                                    os.system('nordvpn -c')
                                    time.sleep(10)
                                elif(is_connected()==True):
                                    break    
                                    

                            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options) 
                            driver.maximize_window()
                            driver.get("https://www.doctolib.fr"+row[1])

                    time.sleep(5)
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    html = driver.page_source
                    soup = BeautifulSoup(html, features="html.parser")

                    result_section = soup.find("div", {"class": "dl-profile-address-picker-address-text"})

                    pr_name = ''
                    pr_name_address = ''

                    

                    try:
                        practice_place = result_section.find_all('div')
                        pr_name = practice_place[1].text
                    except:
                        print("Error!!")

                    try:
                        pr_name_address = practice_place[0].text
                    except:
                        print("Error")

                    pr_name_address = pr_name_address.replace(pr_name, '')
                    dr_address.append(pr_name + '->'+ pr_name_address)
                    time.sleep(5)


                    try:
                        skills =  soup.find("div", {"id": "skills"})

                        skill_list = skills.find_all("div", {"class":"dl-profile-skill-chip"})
                        for skill_name in skill_list:
                            skills_list.append(skill_name.text)
                    except Exception as e:
                        print(e)
                        print("Nope")

                    degree_others = soup.find_all("div", {"class": "dl-profile-card-section dl-profile-history"})


                    for  i in degree_others:
                        header = i.find("h4", {"class": "dl-profile-card-title"})
                        degree_achivment.append(header.text)
                        degree_achivment.append("------------------------")

                    try:
                        list = i.find_all("div", {"class": "dl-profile-text dl-profile-entry"})

                        for  j in  list:
                        ###
                            year = j.find("div", {"class":"dl-profile-entry-time"})
                        ###
                            achivment = j.find("div", {"class":"dl-profile-entry-label"})
                            try:
                                degree_achivment.append(year.text)
                            except:
                                degree_achivment.append("")

                            try:
                                degree_achivment.append(achivment.text)
                            except:
                                degree_achivment.append("")
                    except:
                        print("Not Found")

                    try:
                        contact = soup.find("div", {"id":"openings_and_contact"})
                        contact_2 = contact.find_all("div", {"class":"dl-profile-box"})
                        for con  in contact_2:
                            cont_header = con.find("h4", {"class": "dl-profile-card-subtitle"})
                            cont_header = cont_header.text
                            if("Horaires d'ouverture" in cont_header):
                                pass
                            else:
                                cont_subtitle = con.find("div")
                                dr_address.append(cont_header)
                                dr_address.append("-------------")
                                dr_address.append(cont_subtitle.text)
                        dr_address.append("========================================")
                    except:
                        print("Not Found")
            

            contact_with_address = ""
            for i in dr_address:
                contact_with_address = contact_with_address + i + '\n'
            
            skills_of_dr = ""
            for i in skills_list:
                skills_of_dr = skills_of_dr + i + '\n'

            degree_achivment_of_dr = ""
            for i in degree_achivment:
                degree_achivment_of_dr = degree_achivment_of_dr + i + '\n'   

            my_dr_address.append(contact_with_address)
            my_dr_skills.append(skills_of_dr)
            my_dr_degree_achivment.append(degree_achivment_of_dr)

            print(len(my_dr_name))
            print(len(my_dr_address))
            print(len(my_dr_skills))
            print(len(my_dr_degree_achivment))

            dict = {'Name': my_dr_name, 'Address & Contact': my_dr_address, 'Skills': my_dr_skills, 'Degree': my_dr_degree_achivment} 
            df2 = pd.DataFrame(dict)

            df2.to_csv('doctolib_profile_details.csv')    

            driver.quit()    

            
             
 


 

