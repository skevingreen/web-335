"""
Title: whatabook_v1.2.py
Author: Robert King
Date: March 7, 2025
Description: Python program that connects to MongoDB database and performs tasks using a menu.
"""
# Install pymongo (pip -m pip install pymongo)
# Import the MongoClient
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Create connection string
uri = "mongodb+srv://web335_user:s3cret@bellevueuniversity.7gku3.mongodb.net/?retryWrites=true&w=majority&appName=BellevueUniversity"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Configure a variable to access the whatabookDB
db = client['whatabookDB']

# Send a ping to confirm a successful database connection
try:
  client.admin.command('ping')
  print("\nPinged your deployment. You have successfully connected to MongoDB!")
except Exception as e:
  print(e)
  
# Function to display all books
def display_books():
  # Print a header for the list of books
  print("\n=== List of Books ===")
  # Retrieve all book records from the database collection 'books'
  books = db.books.find({})
  # Iterate through each book in the retrieved records
  for book in books:
    # Print book details: bookId, title, author, genre
    print(f"ID: {book['bookId']} \nTitle: {book['title']} \nAuthor: {book['author']} \nGenre: {book['genre']}\n")

# Function to display books by selected genre
def display_books_by_genre():
  # Print a header for the genre selection
  print("\n=== Books by Genre ===")
  # Retrieve a list of distinct genres from the database
  genres = db.books.distinct("genre")
  # Display the available genres to the user
  print("Available genres:")
  # Iterate through the genres and display with corresponding numbers
  for i, genre in enumerate(genres, 1):
    print(f"{i}. {genre}")
  try:
    # Prompt the user to enter a number corresponding to their chose genre
    genre_choice = int(input("Enter the number corresponding to your chosen genre: ").strip())
    # Check if the user's selection is within the valid range
    if 1 <= genre_choice <= len(genres):
      # Assign the selected genre based on user input
      selected_genre = genres[genre_choice - 1]
    else:
      # Print an error message if the selection is out of range
      print("Error: Invalid selection.")
      return
  except ValueError:
    # Handle cases where the user input is not a valid integer
    print("Error: Please enter a valid number.")
    return
  # Check if the selected genre is actually in the list of available genres
  if selected_genre not in genres:
    print("Error: Invalid genre selection.")
    return
  # Print the selected genre
  print(f"\nBooks in Genre: {selected_genre}")
  # Retrieve books from the database that belong to the selected genre
  books = db.books.find({"genre": selected_genre})
  # Iterate through each book in the selected genre and display details: bookId, title, author
  for book in books:
    print(f"{book['bookId']} - {book['title']} by {book['author']}")

# Function to display all customers who have a wishlist
def display_customers_with_wishlist():
  print("\n=== Customers with Wishlist ===")
  # Find all customer IDs with wishlist items
  customer_ids_with_wishlist = db.wishlistItems.distinct("customerId")
  # Fetch and display the customers who have wishlist items
  customers_with_wishlist = db.customers.find({"customerId": {"$in": customer_ids_with_wishlist}})
  
  # Print header
  print(f"{'First Name':<15}{'Last Name':<15}{'Customer ID':<12}")
  print("-" * 42)
  # Print each customer with a wishlist
  for customer in customers_with_wishlist:
    print(f"{customer['firstName']:<15}{customer['lastName']:<15}{customer['customerId']:<12}")

# Function to display a customer's wishlist
def display_wishlist():
  while True:
    try:
      # Prompt the user to enter a numeric customer ID
      customer_id = int(input("\nEnter Customer ID (e.g., 101, 102, 103): ").strip())
      break
    except ValueError:
      # Error handling for when the input is not a valid integer
      print("Error: Please enter a valid numeric Customer ID.")
  # Check if the customer exists in the database
  customer = db.customers.find_one({"customerId": customer_id})
  # If no matching customer is found print an error message
  if not customer:
    print("Error: Customer ID not found.")
    return
  # Print the customer's name as a header for their wishlist
  print(f"\n=== Wishlist for {customer['firstName']} {customer['lastName']} ===")
  # Retrieve wishlist items associated with a give customer ID
  wishlist_items = db.wishlistItems.find({"customerId": customer_id})
  # Flag to track if any items are found in the wishlist
  found = False
  # Iterate through the retrieved wishlist items
  for item in wishlist_items:
    # Find the corresponding book details based on the book ID stored in the wishlist
    book = db.books.find_one({"bookId": item["bookId"]})
    # If the book exists then print title and author
    if book:
      print(f"Title: {book['title']} by {book['author']}")
      # Sets flag to true since at least one wishlist item was found
      found = True
    # If no items were found in the wishlist print user message
    if not found:
      print("No items found in the wishlist.")

# Main menu
def main():
  while True:
    print("\n=== WhatABook Menu ===")
    print("1. Display all books")
    print("2. Display books by genre")
    print("3. Display customers with wishlist")
    print("4. View customer wishlist")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
      display_books()
    elif choice == "2":
      display_books_by_genre()
    elif choice == "3":
      display_customers_with_wishlist()
    elif choice == "4":
      display_wishlist()
    elif choice == "5":
      print("Exiting program. Goodbye!")
      break
    else:
      print("Invalid choice. Please enter a number between 1-5.")

# Run the program
if __name__ == "__main__":
  main()