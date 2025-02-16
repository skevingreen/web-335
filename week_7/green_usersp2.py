"""
Title: green_usersp2.py
Author: Scott Green
Date: February 16. 2025
Description: Hands-On 5.2: Python with MongoDB, Part II
"""

# Import the MongoClient
from pymongo import MongoClient
import datetime

# Build a connection string to connect to
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.qgo4d.mongodb.net/web335DBretryWrites=true&w=majority")

# Configure a variable to access the web335DB
db = client['web335DB']

# Create a new user document
hayden = {
    "firstName": "Joseph",
    "lastName": "Haydn",
    "employeeId": "1013",
    "email":"jhaydn@me.com",
    "dateCreated": datetime.datetime.utcnow()
}

# Insert the new user into the users collection
print("Insert a new user...")
hayden_user_id = db.users.insert_one(hayden).inserted_id
print(hayden_user_id)   #display the id that was created
print("")   #print a blank line

# Prove the document was created
print("Prove the new user was inserted...")
print(db.users.find_one({"employeeId":"1013"}))
print("")   # print a blank line

# Update the email address of the new user
db.users.update_one(
    {"employeeId":"1013"},
    {
        "$set":{
            "email":"joseph.haydn@me.com"
        }
    }
)

# Prove the email was updated
print("Prove the email was updated...")
print(db.users.find_one({"employeeId":"1013"}))
print("")   # print a blank line

# Delete the user created above
db.users.delete_one({"employeeId":"1013"})

# Prove the user was deleted
print("Prove the user was deleted...")
print(db.user.find_one({"employeeId":"1013"}))

# Call the find function to display all of the users in the collection
# for user in db.users.find():
#     print(user) # print the document