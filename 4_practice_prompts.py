
# ----------------------------------------
# Print Practice Exercises
# ----------------------------------------

# Print Practice #1
# Write Python code that prints the sentence: I love learning Python
print("I love learning Python")


# Print Practice #2
# Write Python code that prints the sentence: Learning with 'TOTAL Python' is super fun!
print("Learning with 'TOTAL Python' is super fun!")


# Print Practice #3
# Write Python code that prints the number 555 to the screen as a result of a mathematical expression
print(500 + 55)

##############################################################################################################
# Find 3 objects around the room and create variables from it,
# Insert those variables into an f-string sentence(look at slide 22)in repl.it

object1 = "laptop"
object2 = "computer"
object3 = "table"

print(f"On the {object3}, there is a {object1} and {object2}.")

# Familiarize yourself with the syntax of the print() function.
# Print your name.
print("Saul")
# Print today's date.
print("11/3/2025")
# Print the name of your favorite movie.
print("Sharknado")
# Print your name and age on separate lines using a single print() function.
print("name: Jafet \nage: 15 ") #idk  how to do ts can someone to it 
# Use f-strings to print a message like: "In 10 years, [Your Name] will be [Your Age + 10] years old."
Your_name = "Jafet"
Your_age = 15
print(f"In 10 years, {Your_name} will be {Your_age + 10} years old.")

##############################################################################################################

###########################String Practice##################################
# syntax is the way we write code
# print("Hello World")
# name = "John"
# in other languages, this is different
# in javascript for example, you define
# variables with let or const or var
# in python, you just give your variables a
# name and then define it with a value
# Use the comment feature if you want to goof off

#challenge
# find a summary of the movie blue beetle online and create a 
# variable called blue_beetle_summary and print it it out to the screen

blue_beetle_summary = "Blue Beetle is a 2023 American superhero film based on the DC Comics character Jaime Reyes / Blue Beetle. Directed by Ángel Manuel Soto and written by Gareth Dunnet-Alcocer, it is the 14th film in the DC Extended Universe (DCEU). Xolo Maridueña stars as Reyes, a recent college graduate who is granted superpowers by an ancient alien relic known as the Scarab. Adriana Barraza, Damián Alcázar, Raoul Max Trujillo, Susan Sarandon, and George Lopez also star in the film. John Rickard and Zev Foreman produced the film for DC Films and Warner Bros. Pictures."

print(blue_beetle_summary)

# print the length of the summary
print(len(blue_beetle_summary))
# upper case the entire summary
print(blue_beetle_summary.upper())
# print the summary
print(blue_beetle_summary)
# print the summary in lowercase
print(blue_beetle_summary.lower())
# replace the word blue with red
print(blue_beetle_summary.replace("blue", "red"))
# print the summary
print(blue_beetle_summary)
# string index the word beetle and print it out
print(blue_beetle_summary[5:11])
# print the last word of the summary
print(blue_beetle_summary.split(" ")[-1])
# print the summary in reverse
print("".join(reversed(blue_beetle_summary)))

##########################input practice#############################################
#input is when we ask the user for input/data
# Ask the user to enter their name.
input("What is your name?")
# Input Practice #1
# Write Python code that allows the user to enter their answer, by making them the following question:
input("What are you learning today?")
# What are you learning today?
text = input("What are you learning today?")
# Your code must be able to print to the screen whatever is entered by the user (use the print function).
print(text)

# Input Practice #2
# Write Python code that allows the user to enter their answer, by making them the following question:
# Where are you from?
response = input("Where are you from? ")
# Your code must be able to print to the screen whatever is entered by the user (use the print function).
print(response)
# Input Practice #3
# Write Python code that displays the user's full name on the screen, by allowing them to enter their first and last name with the following instructions:
# What is your name?
# What is your surname?
# The code must be able to print the user's first and last name on the screen, separated by a space.

name = input("What is your name?")
surname = input("What is your surname?")
print(name, surname)

# Exercise:
# Write a program that asks the user for their name and favorite color, then prints a message using both pieces of information.u
urname = input("What is your name")
color = input("What is your favorite color")
print(f"Your favorite color is {color} & your name is {urname}")