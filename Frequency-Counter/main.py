"""
Frequency Counter
""" 
n = int(input("How many numbers you want to add: " ))
num = []

for i in range(n):
    x = int(input("Enter your Number: " ))
    num.append(x)

print(f"Your list {num}\n" )

"""Create a dictionary which keep record ho frequency of numbers""" 
count = {}

for item in num:
    if item in count:
        count[item] +=1
    else:
        count[item] = 1
        
"""Counts how often each number appears in a user-entered list.""".
max_count = 0
max_numbers = []
for key,value in count.items():
    if value > max_count:
        max_count = value
        max_numbers = [key]
    elif value == max_count:
        max_numbers.append(key)
    
    print(f"{key} comes {value} times" )
    
    
print(f"Most frequent number: {max_numbers}" )
print(f"frequency: {max_count}" )