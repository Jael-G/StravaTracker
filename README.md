# StravaTracker
Python3 Script that acces your Strava public profile every 2 hours, gets the latest run and writes it into a .csv file
## Libraries Needed

- Selenium
- BeautifulSoup
- art
- lxml

The rest normally come included in Python

# IMPORTANT
- After running it once,comment out the lines from 20 to 24 in order to prevent the program from riding the .csv headers over and over again.
- You must specified your chrome driver path and your strava.com profile link in the areas indicated in the code

# Running Code
- Windows
  ```python stravatracker.py```
  
 - Linux
  ```python3 stravatracker.py```

