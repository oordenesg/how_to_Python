# Magic 8-Ball

# This is a popular toy developed in 1950s for fortune-telling or advice seeking. 
# We will write a Python program that can actually answer "Yes" or "No" questions given some questions.
# To do this we will 9 possible answers:

# 1. Yes - definitely.
# 2. It is decidedly so.
# 3. Without a doubt.
# 4. Reply hazy, try again.
# 5. Ask again later.
# 6. Better not tell you now.
# 7. My sources say no.
# 8. Outlook not so good.
# 9. Very doubtful.

# Let's create our 8-Ball program.

# 1. In magic8.py, declare a variable name and assign it to the name of the person who will be asking the Magic 8-Ball.
name = "Mark"
# 2. Now, declare a variable question, and assign to a “Yes” or “No” question you’d like to ask the Magic 8-Ball.
question = "Will I win the lotery?"
# 3. We want to store the answer of the Magic 8-Ball in another variable, which we’ll call answer. For now, assign this variable to an empty string.
answer = ""
# 4. Next, we’ll create a variable to store the randomly generated value. Declare a variable called random_number, and assign it to the function call:
import random
random_number = random.randint(1,9)
# 5. Now that we’ve declared all the variables needed, it’s time to implement the core logic of our program! For this section, we’ll be utilizing control flow using an if/elif/else statement to assign different answers for each randomly generated value.
# First, write an if statement where if the random_number is equal to 1, answer is assigned to the phrase “Yes - definitely.”. Then, continue writing elif statements for each of the remaining phrases for the values 3 to 9.
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer ="Without a doubt"
elif random_number == 4:
  answer ="Reply hazy, try again"
elif random_number == 5:
  answer ="Ask again later"
elif random_number == 6:
  answer ="Better not tell you now"
elif random_number == 7:
  answer ="My sources say no"
elif random_number == 8:
  answer ="Outlook not so good"
elif random_number == 9:
  answer ="Very doubtful"
else:
  answer ="Error"

# 6. Now, let’s see our program in action! Write a print() statement to output the asker’s name and their question, which should be in the following format: Name + "asks:" + Question
print(name +"asks: " + question)
# 7. Add a second print() statement that will output the Magic 8-Ball’s answer in the following format: Magic 8-Ball's answer: [answer]
print("Magic 8-Ball's answer: My source say "+ answer)

