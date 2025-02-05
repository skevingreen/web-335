""" 
    Title: green-exercise5.3.py
    Author: Scott Green
    Date: 05 February 2025
    Description: Hands-On 3.1: Conditionals, Lists, and Loops
"""

# Define a list of tasks associated with running a lemonade stand
tasks = ["Buy ingredients", "Make lemonade", "Sell lemonade", "Count earnings", "Clean up"] # We have 5 tasks to perform

# Loop over the tasks and print them out
for task in tasks:  # Find a task in the loop
  print(task) # Print the task to stdout

# Define a list of days
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"] # We have 7 days in the list to represent a full week

# Print a blank line
print("")

# Loop through each day and print out what the task is for that day
for i in range(len(days)):  # Find the length of the days list and iterate over each item
  if (i == 0) or (i == 6):  # Figure out if today is a weekend day
    print("It's the weekend, take the day off") # If today is a weekend day, print out that the day should be taken off
  else: # Otherwise, it's a weekday
    print("Today is " + days[i] + " you need to: " + tasks[i - 1])  # Print out the day and the day's task (note the arrays are offset from one another by 1)