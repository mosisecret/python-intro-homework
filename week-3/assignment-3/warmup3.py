#Boolean Expression Practice
print(not True and False) # False. Not is evaluated first, making the expression equivalent to False and False. 
print(True or False and False) # False. And evaluates before or, making the expression True or False. 
# Or returns True when at least one condition is true. 
print(not (5>3)) # False. The value inside the parentheses is True. The Not operator then makes the value False.
print (10 == 10 and 4 !=4) # False. The And operator returns True only when both conditions are True. 
print(not False or not True) # True. The Or operator returns True when one value is true. 