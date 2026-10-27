today = input ("what day is it? ")
today = today.lower()
time = input ("What time of day is it: morning, afternoon or evening? ")
time = time.lower()

if today != "monday" and today != "tuesday" and today != "wednesday" and today != "thursday" and today != "friday" and today != "saturday" and today != "sunday": 
    print ("Oops, I didn't recognize that. Spell out one of the seven days of the week.")
if time != "morning" and time != "afternoon" and time != "evening": 
    print ("Oops, I didn't recognize that. Write 'morning,' 'afternoon, or 'evening'.")
if time == "afternoon": 
    print("Better start thinking about what's for dinner.")
if today == ("friday" or "saturday") and time == "evening": 
    print ("Ah, the weekend. Time to kick back. ")
if today == "sunday" and time == "morning":
    print ("Prep some meals for the week.")
if today != "saturday" and today != "sunday" and time == "morning": 
    print ("Get the kids lunches ready for school.")
 
