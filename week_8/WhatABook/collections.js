/**
  Title: collections.js
    Author: Robert King
    Date: February 27, 2025
    Description: MongoDB Shell Scripts for customers, books, & wishlistItems collections.
 */

// Delete the customers, books, and wishlistItems collections.
db.customers.drop()
db.books.drop()
db.wishlistItems.drop()

// Create the customers, books, and wishlistItems collections using Document Validation.
db.createCollection("customers", {
  validator: { $jsonSchema: {
    bsonType: "object",
    properties: {
      _id: {
        bsonType: "string"
      },
      customerId: {
        bsonType: "int"
      },
      firstName: {
        bsonType: "string"
      },
      lastName: {
        bsonType: "string"
      }
    }
  }}
})

db.createCollection("books", {
  validator: { $jsonSchema: {
    bsonType: "object",
    properties: {
      _id: {
        bsonType: "string"
      },
      bookId: {
        bsonType: "int"
      },
      title: {
        bsonType: "string"
      },
      author: {
        bsonType: "string"
      },
      genre: {
        bsonType: "string"
      }
    }
  }}
})

db.createCollection("wishlistItems", {
  validator: { $jsonSchema: {
    bsonType: "object",
    properties: {
      _id: {
        bsonType: "string"
      },
      wishlistId: {
        bsonType: "int"
      },
      customerId: {
        bsonType: "int"
      },
      bookId: {
        bsonType: "int"
      }
    }
  }}
})

// customers
robert = {
  "_id":"cust-101",
  "customerId": 101,
  "firstName": "Robert",
  "lastName": "King"
}

isabella = {
  "_id":"cust-102",
  "customerId": 102,
  "firstName": "Isabella",
  "lastName": "King"
}

james = {
  "_id":"cust-103",
  "customerId": 103,
  "firstName": "James",
  "lastName": "Davis"
}

mary = {
  "_id":"cust-104",
  "customerId": 104,
  "firstName": "Mary",
  "lastName": "Thompson"
}


// Insert the documents.
db.customers.insertOne(robert)
db.customers.insertOne(isabella)
db.customers.insertOne(james)
db.customers.insertOne(mary)

// books.
book1 = {
  "_id": "book-201",
  "bookId": 201,
  "title": "Prince of Lies",
  "author": "James Lowder",
  "genre":"Fantasy"
}

book2 = {
  "_id": "book-202",
  "bookId": 202,
  "title": "On a Pale Horse",
  "author": "Piers Anthony",
  "genre":"Fantasy"
}

book3 = {
  "_id": "book-203",
  "bookId": 203,
  "title": "Ender's Game",
  "author": "Orson Scott Card",
  "genre":"Science Fiction"
}

book4 = {
  "_id": "book-204",
  "bookId": 204,
  "title": "Magician",
  "author": "Raymond E. Feist",
  "genre":"Fantasy"
}

book5 = {
  "_id": "book-205",
  "bookId": 205,
  "title": "The Grapes of Wrath",
  "author": "John Steinbeck",
  "genre":"Historical Fiction"
}

book6 = {
  "_id": "book-206",
  "bookId": 206,
  "title": "The Odyssey",
  "author": "Homer",
  "genre":"Mythology"
}

// Insert the documents. 
db.books.insertOne(book1)
db.books.insertOne(book2)
db.books.insertOne(book3)
db.books.insertOne(book4)
db.books.insertOne(book5)
db.books.insertOne(book6)

// wishlistItems
wishlist1 = {
  "_id":"wish-301",
  "wishlistId":301,
  "customerId":101,
  "bookId":201
}

wishlist2 = {
  "_id":"wish-302",
  "wishlistId":302,
  "customerId":102,
  "bookId":202
}

wishlist3 = {
  "_id":"wish-303",
  "wishlistId":303,
  "customerId":103,
  "bookId":203
}

// Insert the documents.
db.wishlistItems.insertOne(wishlist1)
db.wishlistItems.insertOne(wishlist2)
db.wishlistItems.insertOne(wishlist3)

