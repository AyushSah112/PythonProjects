'''
password strength checker
'''
#Material for password checking
lowercase = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x","y","z"
    ]

uppercase = [
    "A","B","C","D","E","F","G","H","I","J","K","L","M",
    "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
    ]

numbers = [
    "0","1","2","3","4","5","6","7","8","9"
    ]

symbols = [
    "!","@","#","$","%","^","&","*","(",")",
    "_","-","+","=","<",">","?","/","{","}",
    "[","]","|",":",";"
    ]
    

a = input("Enter your password:\n")
lst = list(a)

score = 0
has_lower = False
has_upper = False
has_number = False
has_symbol = False

for i in lst:
    if i in lowercase:
        has_lower = True
    if i in uppercase:
        has_upper = True
    if i in numbers:
        has_number = True
    if i in symbols:
        has_symbol = True

if has_lower:
    score += 1
if has_upper:
    score += 2
if has_number:
    score += 3
if has_symbol:
    score += 5

if len(a) > 0 and len(a) <= 5:
    score += 1
if len(a) > 5 and len(a) <= 10:
    score += 2
if len(a) > 10:
    score += 3

if score > 0 and score <= 4:
    print("Your password is weak")
elif score > 4 and score <= 8:
    print("Your password is medium")
elif score > 8 and score <= 11:
    print("Your password is strong")
else:
    print("Your password is very strong")