# 1. Traceback (most recent call last):
# 1. (cont.) File "/Users/mosisecret/CodeTheDream/python_class/python_homework/python-intro-homework/week-2/assignment-2/warmup4.py", line 6, in <module>
# 1. (cont.)   print (f"Hi {naame}, how are you liking the Python class so far? ")
# 1. (cont.)              ^^^^^
# 1. (cont.) NameError: name 'naame' is not defined. Did you mean: 'name'?
# 2. The script assigned an input to the variable "name." Then there's a print function using the variable that...
# 2. (cont.) ...should display a sentence in response to the input. 
# But in the print function the variable is misspelled. 
# 3. I corrected the spelling of the variable in the print function and resaved the script. 
name = input("Hey, what's your name? ")
print (f"Hi {name}, how are you liking the Python class so far? ")