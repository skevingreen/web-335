// Author: Scott Green
// Date: February 25, 2025
// File: queries.js
// Description: MongoDB queries to find various information from WhatABook

// Write a query to display a list of books.
db.books.find();

// Write a query to display a list of books by genre.
db.books.aggregate([ {$match:{'genre':'Horror'}} ])

// Write a query to display a list of books by author.
db.books.aggregate([ {$match:{'author':'Stephen King'}} ])

//Write a query to display a book by bookId.
db.books.findOne({bookId: 'b0001'})