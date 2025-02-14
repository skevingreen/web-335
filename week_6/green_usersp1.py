"""
Title: green_usersp1.py
Author: Scott Green
Date: February 13. 2025
Description: Hands-On 4.2: Python with MongoDB, Part I
"""

# Import the MongoClient
from pymongo import MongoClient

# Build a connection string to connect to
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.qgo4d.mongodb.net/web335DBretryWrites=true&w=majority")

# Configure a variable to access the web335DB
db = client['web335DB']

# Call the find function to display all of the users in the collection
for user in db.users.find():
    print(user) # print the document

# print a blank line
print(""); 

# Display a document where the employeeId is 1011
print(db.users.find_one({"employeeId":"1011"}))

# print a blank line
print("");

# Display a document where the lastName is Mozart
print(db.users.find_one({"lastName":"Mozart"}))