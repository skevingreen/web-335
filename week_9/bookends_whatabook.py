"""
Title: bookends_whatabook.py
Author: Scott Green
Date: March 1. 2025
Description: WhatABook Console Application
"""

# import sys 
import sys

# Import the MongoClient
from pymongo import MongoClient

# Build a connection string to connect to
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.qgo4d.mongodb.net/whatabookDBDBretryWrites=true&w=majority")

# Configure a variable to access the whatabookDB database
db = client['whatabookDB']

# list all available books and related information
def list_all_books():
  books = db.books.find()
  for book in books:
    print("bookId: " + str(book["bookId"]))
    print("title: " + book["title"])
    print("author: " + book["author"])
    print("genre: " + book["genre"])
    print("")

# list books and related information by provided genre
def list_books_by_genre(type):
  books = db.books.find({ "genre":type })
  for book in books:
    print("bookId: " + str(book["bookId"]))
    print("title: " + book["title"])
    print("author: " + book["author"])
    print("genre: " + book["genre"])
    print("")

# returns an list of genres
def get_genres():
  genres = db.books.distinct("genre")
  return genres

# display list of genres
def list_genres():
  genre_list = get_genres()
  for genre in genre_list:
    print(genre)
  print("")

# https://pynative.com/python-check-user-input-is-number-or-string/
# validate that customer_id is an integer
def validate_customerId(customer_id):
  try:
    val = int(customer_id)
    return True
  except:
    return False

# print the wishlist for given customerId
# https://www.mongodb.com/developer/languages/python/python-quickstart-aggregation/
def list_wishlist(customer_id):
  if (validate_customerId(customer_id)):
    pipeline = [
      {
        "$match": {
          "customerId":int(customer_id)
        }
      },
      {
        "$lookup": {
          "from":"books",
          "localField":"bookId",
          "foreignField":"bookId",
          "as":"customer_books"
        }
      }
    ]

    # get the results of our query
    results = db.wishlistItems.aggregate(pipeline)

    # loop through the query results and print out the details
    for result in results:
      print("wishlistId: " + str(result["wishlistId"]))
      print("customerId: " + str(result["customerId"]))
      for book in result["customer_books"]:
        print("bookId: " + str(book["bookId"]))
        print("title: " + book["title"])
        print("author: " + book["author"])
        print("genre: " + book["genre"])
        print("")
  else:
    print("CustomerId must be a number.")
    print("")

# Display a list of actions and perform them until the user quits
while (True):
  # print a menu of actions that can be taken
  print("Available actions:")
  print("1) Display books.")
  print("2) Display books by genre.")
  print("3) Display wishlist by customerId (e.g., 101).")
  selection = input("Enter a number or q to quit: ")
  print("")

  # take an action based on the provided input
  if (selection == "q"):
    # https://stackoverflow.com/questions/73663/how-do-i-terminate-a-script
    sys.exit()  # user chose to quit
  elif (selection == "1"):
    list_all_books()
  elif (selection == "2"):
    list_genres()
    type = input("Enter a genre: ")
    print("")
    list_books_by_genre(type)
  elif (selection == "3"):
    customer_id = input("Enter customerId: ")
    print("")
    list_wishlist(customer_id)
  else:
    print("Invalid selection.")