// Author: Scott Green
// Date: January 30, 2025
// File: green-exercise4.3.js
// Description: MongoDB queries to find various information

// display all users in the collection
db.users.find();

// display the user with the email address jbach@me.com
db.users.findOne({email:'jbach@me.com'});

// display the user with the last name Mozart
db.users.findOne({lastName:'Mozart'});

// display the user with the first name Richard
db.users.findOne({firstName:'Richard'});

// display the user with employeeId 1010
db.users.findOne({employeeId:'1010'});