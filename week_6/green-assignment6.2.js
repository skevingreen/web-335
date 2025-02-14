// find all students
db.students.find();


// define a new student
student = {firstName: 'Scott', lastName: 'Green', studentId: 's1019', houseId: 'h1008'};

// add the new student
db.students.insertOne(student);

// prove the new student was added
db.students.findOne({firstName: 'Scott'});


// update house id of student
db.students.updateOne({firstName: 'Scott'}, {$set:{houseId: 'h1010'}});

// prove the house id was update
db.students.findOne({firstName: 'Scott'});


// delete the student created above
db.students.deleteOne({firstName: 'Scott'});

// prove the student was deleted
db.students.findOne({firstName: 'Scott'});


// display all students by house
db.houses.aggregate([ {$lookup: {from: 'students', localField:'houseId', foreignField:'houseId', as:'student_docs'}} ]);


// display all students in house Gryffindor
db.houses.aggregate([ {$match:{'houseId':'h1007'}}, {$lookup:{from: 'students', localField:'houseId', foreignField:'houseId', as: 'student_docs'}} ]);


// display all students in the house with an Eagle mascot
db.houses.aggregate([ {$match:{'mascot':'Eagle'}}, {$lookup:{from: 'students', localField:'houseId', foreignField:'houseId', as: 'student_docs'}} ]);
