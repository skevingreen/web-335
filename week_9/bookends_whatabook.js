/*
Title: query.js
Author: Robert King
Date: February 27, 2025
Description: Queries for performing various operations on customers, books, & wishlistItems using MongoDB Shell.
*/

// Select the database to use.
use("whatabookDB");

// Display list of books.
db.books.find();

// Display a list of books by genre.
db.books.find({ genre: "Fantasy"});

// Display a list of books by author.
db.books.find({ author: "James Lowder" });

// Display a book by bookId.
db.books.find({ bookId: 201 });

// Display a wishlist by customerId
db.wishlistItems.find({ customerId: 101 })

// Add books to a customer's wishlist
db.wishlistItems.insertOne({ _id:"wish-304", wishlistId:301, customerId:101, bookId:205 })

// Remove a book from a customer's wishlist
db.wishlistItems.deleteOne({ _id:"wish-304" })