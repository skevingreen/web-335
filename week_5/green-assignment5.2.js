/**
    Title: green-assignment5.2.js
    Author: Scott Green
    Date: 05 February 2025
    Assignment: 5.2 - Projections
    Description: MongoDB Shell Scripts for the updating users collection.
 */

/**
 * Create one User document. 
 */
gershwin = {
  "firstName": "George",
	"lastName": "Gershwin",
	"employeeId": "1013",
	"email": "ggershwin@me.com",
	"dateCreated": new Date()
}

/**
 * Insert the newly created user document.
 */
db.users.insertOne(gershwin)

/**
 * Prove Gershwin's record was added.
 */
db.users.findOne({firstName:'George'})

/**
 * Update Mozart's email address.
 */
db.users.updateOne({employeeId: '1009'}, {$set: {email: 'mozart@me.com'}});

/**
 * Prove Mozart's email record was updated.
 */
db.users.findOne({firstName:'Wolfgang'})

/**
 * Display all users in the collection using projections to show only first name, last name, and email address
 */
db.users.find({}, {_id:0, firstName:1, lastName:1, email:1})