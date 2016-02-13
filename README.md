# powDayTexter
A daily script that grabs new snow reports from Colorado resorts and texts users if a certain amount of snow has fallen.


Script Process:

1. CRON Job - Initiate script at a certain time each day. 
2. Data pull - Snag data from our source. Perhaps http://www.onthesnow.com/colorado/skireport.html?
3. Data parse - Sift through the data for the relevant values. Assign to appropriate variables.
4. Data compare by ShredderID - Assess user_location, user_snow_limit and current_conditions to see if text is merited.
5. Text shredder - Send SMS with pithy message including # of inches. (Twilio API?)
