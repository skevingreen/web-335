/**
    Title: WhatABook.js
    Author: Scott Green
    Date: 25 February 2025
    Description: MongoDB Shell Scripts for the WhatABook collections.
 */

// Delete the books and customers collections.
db.books.drop()
db.customers.drop()

// Create the houses and students collections using Document Validation.
db.createCollection("customers", {
	validator: { $jsonSchema: {
		bsonType: "object",
		properties: {
			firstName: {
				bsonType: "string"
			},
			lastName: {
				bsonType: "string"
			},
			customerId: {
				bsonType: "string"
			}
		}
	}}
})

db.createCollection("books", {
	validator: { $jsonSchema: {
		bsonType: "object",
		properties: {
			title: {
				bsonType: "string"
			},
			genre: {
				bsonType: "string"
			},
			author: {
				bsonType: "string"
			},
			bookId: {
				bsonType: "string"
			}
		}
	}}
})

// Customers.
joan = {
	"firstName": "Joan",
	"lastName": "Jett",
	"customerId": "c0001"
}

roger = {
	"firstName": "Roger",
	"lastName": "Daltrey",
	"customerId": "c0002"
}

don = {
	"firstName": "Don",
	"lastName": "Henley",
	"houseId": "c0003"
}

gene = {
	"firstName": "Gene",
	"lastName": "Simmons",
	"houseId": "c0004"
}

// Insert the documents.
db.customers.insertOne(joan)
db.customers.insertOne(roger)
db.customers.insertOne(don)
db.customers.insertOne(gene)

// Books
it = {
	"title": "It",
	"genre": "Horror",
	"author": "Stephen King",
	"bookId": "b0001"
}

hitOrMyth = {
	"title": "Hit or Myth",
	"genre": "Comedy",
	"author": "Robert Aspirin",
	"bookId": "b0002"
}

warOfTheWorlds = {
	"title": "The War of The Worlds",
	"genre": "Science Fiction",
	"author": "H.G. Wells",
	"bookId": "b0003"
}

dunwichHorror = {
	"title": "The Dunwich Horror",
	"genre": "Horror",
	"author": "H.P. Lovecraft",
	"bookId": "b0004"
}

shining = {
    "title": "The Shining",
    "genre": "Horror",
    "author": "Stephen King",
    "bookId": "b0005" 
}

// Insert the documents.
db.books.insertOne(it)
db.books.insertOne(hitOrMyth)
db.books.insertOne(warOfTheWorlds)
db.books.insertOne(dunwichHorror)
db.books.insertOne(shining)