today = input ("what day is it? ")
today = today.lower()

time = input ("What time of day is it: morning, afternoon or evening? ")
time = time.lower()
fallback = True

if (today != "monday") and (today != "tuesday") and (today != "wednesday") and (today != "thursday") and (today != "friday") and (today != "saturday") and (today != "sunday"): 
    fallback = False
    print ("I didn't recognize the day you entered. Spell out one of the seven days of the week.")
elif (time != "morning") and (time != "afternoon") and (time != "evening"): 
    fallback = False
    print ("I didn't recognize the time of day. Write 'morning,' 'afternoon, or 'evening'.")

elif today == "sunday" and time == "afternoon":
    fallback = False
    print ("Prep some meals for the week ahead.")
elif today == "friday" and time == "evening":
    fallback = False
    print ("Ah, the weekend. Time to kick back. ")
elif today == "monday" and time == "morning": 
    fallback = False
    print ("Remember to bring the clean sheets back to preschool.")
elif today == "monday" and time == "evening":
    fallback = False
    print ("Is your Code the Dream homework ready? It's due tomorrow!")
elif today == "saturday" and time == "morning": 
    fallback = False
    print ("Let's get some fresh veggies from the farmer's market!")
elif today == "thursday" and time == "afternoon": 
    fallback = False
    print ("How about a cat nap? You earned it.")
elif today == "wednesday" and time == "afternoon":
    fallback = False
    print ("Have you figured out what's for dinner?")
elif today == "thursday" and time == "evening":
    fallback = False
    print ("Your turn to put the kids to bed.")
elif today == "sunday" and time == "morning": 
    fallback = False
    print ("Give Mama a call.")
elif fallback != False:
    print ("No urgent plans. Maybe catch up on work around the house.")
 
