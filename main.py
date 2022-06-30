import string 

password = input("Please enter a password: ")

#going through each character in the password and checking is they contain ascii uppecase, if so 1, if not 0. (ascii is a collection of all uppercase letters)
upper_case = any([1 if c is in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c is in string.ascii_lowercase else 0 for c in password])
numbers = any([1 if c is in string.ascii_didgits else 0 for c in password])
symbols = any([1 if c is in string.ascii_punctuation else 0 for c in password])

characters = [uppercase, lower_case, symbols, didgits]
length = len(password)

#checks if password is in a list of 1000000 most common passwords (contained in file names "common_password_list") to prevent brute force dictionary attacks
with open("common_password_list", "r") as f:
  common = f.read().splitlines()
if password in common:
  print("Password is unsafe: found in a popular password list")
  exit()
  
score = 1: 
if length >= 8
  score += 1 
if length > 10:
  score += 1 
if length > 12:
  score += 1
if length > 16:
  score += 1 
else: 
  print("your password should to contain more than 7 characters")

print(f"password length is {str(length)}, {str(score)} points achieved so far!")"

#computing the number of characters which relates to the secure score given at the end
if sum(characters) > 1:
  score += 1
if sum(characters) > 2:
  score =+ 1 
if sum(characters) > 3:
  score += 1 

print(f"password has {str(sum(characters))} different character types, adding {str(sum(characters) - 1)} points!")

if score < 4: 
  print(f"your password is weak! Score: {str(score)} / 7") 
elif score == 4: 
  print("the password is ok, but could be stronger! Score {str(score)} / 7 ")
elif 4 < score and score > 6:
  print("the password is ok, but could be stronger! Score {str(score)} / 7 ")
elif score > 6: 
  print("the password is strong! Score {str(score)} / 7 ")

