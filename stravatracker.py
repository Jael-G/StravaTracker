from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from time import sleep
import lxml
import json
from art import *
from os import system
import csv

def WriteNewRace(run_data):
                print(f'RACE ID: {run_data["id"]}\nNAME: {run_data["name"]}\nTYPE: {run_data["type"]}\nDATE: {run_data["startDateLocal"]}\nDISTANCE: {run_data["distance"]}\nELEVATION: {run_data["elevation"]}\nTIME: {run_data["movingTime"]}\nPACE: {pace} mph')
               
                with open('rundata.csv','a',newline='') as file:
                    new_fieldnames=['RACE ID','NAME', 'TYPE', 'DATE', 'DISTANCE', 'ELEVATION', 'TIME', 'PACE']
                    writer=csv.DictWriter(file, fieldnames=new_fieldnames)

                    #AFTER FIRST RUN COMMENT OUT ALL OF THE IF AND ELSE STATEMENTS
                    #VVVVVVVVVVVVVVVVVVVVVVV
                    if first_open:
                        writer.writeheader()

                    else:
                        pass
                    ##ΛΛΛΛΛΛΛΛΛΛΛΛΛΛΛΛΛΛΛΛΛΛ

                    writer.writerow({'RACE ID' : run_data["id"],'NAME': run_data["name"], 'TYPE': run_data["type"], 'DATE': run_data["startDateLocal"], 'DISTANCE': run_data["distance"], 'ELEVATION': run_data["elevation"], 'TIME': run_data["movingTime"], 'PACE': pace})
            
try:
    last_id=0
    first_open=True
    try:
        with open('idlog.txt', mode='r') as file:
            last_id=int(file.read().splitlines()[0])
        print(f'ID FOUND -> ID: {last_id}')
    except:
        print("idlog.txt FILE WAS NOT FOUND.. ASSUMING NO PREVIOUS ID WAS USED IN THE CODE")
        input('\nPRESS ENTER TO CONTINUE...')
        system('clear')

    print(text2art("STRAVA-TRACKER"))
    print('by Jael Gonzalez\n--------------------------------------------------------------------\n')
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path='CHROMEDRIVER PATH HERE', options=chrome_options)

    while True:
        page=driver.get('STRAVA PROFILE LINK HERE') #THE STRAVA PROFILE LINK USUALLY GOES LIKE: https://www.strava.com/athletes/000000
        soup = BeautifulSoup(driver.page_source, "lxml")
        sleep(1)
        mydivs = soup.find("div", {"data-react-class": "AthleteProfileApp"})["data-react-props"]
        run_data=json.loads(str(mydivs))['recentActivities'][0]
        new_id=run_data['id']


        if new_id==last_id:
            print('\nID REMAINED THE SAME...')
            print(f'\n[*]Previous Race ID: {last_id}\n[*]Latest Race ID: {new_id}')
            print("NO NEW RACE FOUND...")
            sleep(10)

        else:
            last_id=new_id
            with open('idlog.txt', mode='w') as file:
                file.write(str(last_id))
                print('\nNEW RACE FOUND:\n')
                time_list=run_data["movingTime"].split(':')
                
                if len(time_list)==3:
                    pace=float(run_data['distance'][:-3])/(float(time_list[0])+(float(time_list[1])/60)+(float(time_list[2])/3600))
                elif len(time_list)==2:
                    pace=float(run_data['distance'][:-3])/((float(time_list[0])/60)+(float(time_list[1])/3600))
                elif len(time_list)==1:
                    pace=float(run_data['distance'][:-3])/(float(time_list[0])/3600)
                pace=round(pace,2)
                WriteNewRace(run_data)
        print('\n--------------------------------------------------------------------')

except (KeyboardInterrupt, SystemExit):
    driver.close()
    driver.quit()
    print('CLOSING PROGRAM')

