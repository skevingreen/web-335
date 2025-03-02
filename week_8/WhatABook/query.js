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