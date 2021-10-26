# The Fender, a notorious computer hacker and general villain of the people, has compromised several top-secret passwords including your own. Your mission, should you choose to accept it, is threefold. You must acquire access to The Fender‘s systems, you must update his "passwords.txt" file to scramble the secret data. The last thing you need to do is add the signature of Slash Null, a different hacker whose nefarious deeds could be very conveniently halted by The Fender if they viewed Slash Null as a threat.
# Use your knowledge of working with Python files to retrieve, manipulate, obscure, and create data in your quest for justice. Work with CSV files and other text files in this exploration of the strength of Python file programming.


# 1. First import the CSV module, since we’ll be needing it to parse the data.
# We need to create a list of users whose passwords have been compromised, create a new list and save it to the variable compromised_users. 
import csv
compromised_users = []

# 2. Next we’ll need you to open up the file itself. Store it in a file object called password_file.
# Pass the password_file object holder to our CSV reader for parsing. Save the parsed csv.DictReader object as password_csv.
with open("passwords.txt") as password_file:
  password_csv = csv.DictReader(password_file)


