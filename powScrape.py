# Scrape data from http://www.onthesnow.com/colorado/skireport.html
# Extract table element in div class="resBox"
# Store table in file on server   !!!! WHY? Stored in memory, immediately compare against shredderID values.

# Import libraries to use
from lxml import html
import requests

# Declare variables to be used in each section

# 1 - Data scrape
page = requests.get('http://www.onthesnow.com/colorado/skireport.html')
tree = html.fromstring(page.content)

# 2 - Data parse 

resortCond = []           # 2D array of today's conditions at each resort [[0 - resName, 1 - freshPow]]
    # sample resortCond: [["Alta", 4]["Loveland", 14]["Squaw Valley", 10]["La Clusaz", 6]]
    # ???!?!???!?!?!?!?!?!?!??!?!?!?!!?!!!!!
return resortCond

# 3 - Data compare

shredderList = []         # 2D array of shredders to test [[0 - shredderID, 1 - shredderName, 2 - shredderPowLimit, 3 - shredderRes, 4 - shredderNum][...][...]]
    # Sample shredderList value: [[121, "Jerry Jones", 6, "Squaw Valley", "6173456789"], [55, "Carrie Gleich", 14, "Alta", "2078883344"], [11, "Candide Thovex, 9, "La Clusaz", "+445678831213"]]
shredderSMS = []        # Our list of shredders to SMS today [[0 - shredderID, 1 - shredderName, 2 - shredderRes, 3 - freshPow,][...][...]]
    # Sample shredderSMS: [["Jerry Jones"][][][]]

for i in resortCond:
# Pull values from shredderList that match resortCond[i]



  resort = 
  resFresh = 

for i in shredderList
if shredderList[i][2] == resort:
  if shredderPowLimit <= resFresh:
    shredderSMS.append(resFresh, shredderName)


