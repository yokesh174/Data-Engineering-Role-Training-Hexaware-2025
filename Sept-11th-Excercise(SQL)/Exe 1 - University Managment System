University Management System

We’ll track students, courses, and enrollments.

1. Database & Collections Setup

use universityDB

// Students Collection
db.students.insertMany([
{ _id: 1, name: "Rahul Sharma", age: 21, email: "rahul@example.com", city:
"Bangalore" },
{ _id: 2, name: "Priya Singh", age: 22, email: "priya@example.com", city: "Delhi" },
{ _id: 3, name: "Aman Kumar", age: 20, email: "aman@example.com", city: "Hyderabad"
},
{ _id: 4, name: "Sneha Reddy", age: 23, email: "sneha@example.com", city: "Chennai"
}
]);

// Courses Collection
db.courses.insertMany([
{ _id: 101, title: "Database Systems", department: "CS", credits: 4 },
{ _id: 102, title: "Data Structures", department: "CS", credits: 3 },
{ _id: 103, title: "Economics 101", department: "Economics", credits: 2 },
{ _id: 104, title: "Operating Systems", department: "CS", credits: 4 }
]);

// Enrollments Collection (student_id references students, course_id references
courses)
db.enrollments.insertMany([
{ student_id: 1, course_id: 101, grade: "A" },
{ student_id: 1, course_id: 103, grade: "B" },
{ student_id: 2, course_id: 101, grade: "A" },
{ student_id: 3, course_id: 102, grade: "C" },
{ student_id: 4, course_id: 104, grade: "B" }
]);

2. Exercises

----> CRUD Basics

//Insert a new student into the students collection.
db.students.insertOne({_id:5, name:"Karan Mehta", age:21, email:"karan@example.com", city:"Mumbai"});
{
  acknowledged: true,
  insertedId: 5
}

// Find all students from Delhi.
db.students.find({ city:"Delhi"});
{
  _id: 2,
  name: 'Priya Singh',
  age: 22,
  email: 'priya@example.com',
  city: 'Delhi'
}

// Update Aman Kumar’s email.
db.students.updateOne({ name: "Aman Kumar" },  { $set : { email: "amankumar@university.com"}});
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}

// Delete the student "Sneha Reddy".
db.students.deleteOne({ name: "Sneha Reddy"});
{
  acknowledged: true,
  deletedCount: 1
}

---->Indexing

// Create a unique index on student email .
db.students.createIndex( {email: 1}, {unique: true});
email_1

// Create a compound index on department and credits in courses .
db.courses.createIndex({ department: 1, credits: -1});
department_1_credits_-1

// Verify indexes using getIndexes() .
db.courses.getIndexes();
[
  { v: 2, key: { _id: 1 }, name: '_id_' },
  {
    v: 2,
    key: { department: 1, credits: -1 },
    name: 'department_1_credits_-1'
  }
]

// Write a query on courses that benefits from the compound index.
db.courses.find({ department: "CS", credits: { $gte: 3 } });
{
  _id: 101,
  title: 'Database Systems',
  department: 'CS',
  credits: 4
}
{
  _id: 104,
  title: 'Operating Systems',
  department: 'CS',
  credits: 4
}
{
  _id: 102,
  title: 'Data Structures',
  department: 'CS',
  credits: 3
}

// Write a query that causes a COLLSCAN instead of using the index.
db.courses.find({ title: "Database Systems" });
{
  _id: 101,
  title: 'Database Systems',
  department: 'CS',
  credits: 4
}

----> Aggregation Framework

// Find the number of students enrolled in each course ( $group ).
db.enrollments.aggregate([{ $group: { _id: "$course_id", total_students: { $sum: 1 } } }]);
{
  _id: 102,
  total_students: 1
}
{
  _id: 101,
  total_students: 2
}
{
  _id: 103,
  total_students: 1
}
{
  _id: 104,
  total_students: 1
}

// Find the average age of students per city.
db.students.aggregate([{ $group: { _id: "$city", avg_age: { $avg: "$age" } } }]);
{
  _id: 'Hyderabad',
  avg_age: 20
}
{
  _id: 'Delhi',
  avg_age: 22
}
{
  _id: 'Mumbai',
  avg_age: 21
}
{
  _id: 'Bangalore',
  avg_age: 21
}

// Find the highest credit course in the CS department.
db.courses.aggregate([{ $match: { department: "CS" } },{ $sort: { credits: -1 } },{ $limit: 1 }]);
{
  _id: 101,
  title: 'Database Systems',
  department: 'CS',
  credits: 4
}

// Show all enrollments with student names (using $lookup ).
db.enrollments.aggregate([
  {
    $lookup: {
      from: "students",
      localField: "student_id",
      foreignField: "_id",
      as: "student_info"
    }
  }
]);

{
  _id: ObjectId('68c286b2cff9a81d61ff3218'),
  student_id: 1,
  course_id: 101,
  grade: 'A',
  student_info: [
    {
      _id: 1,
      name: 'Rahul Sharma',
      age: 21,
      email: 'rahul@example.com',
      city: 'Bangalore'
    }
  ]
}
{
  _id: ObjectId('68c286b2cff9a81d61ff3219'),
  student_id: 1,
  course_id: 103,
  grade: 'B',
  student_info: [
    {
      _id: 1,
      name: 'Rahul Sharma',
      age: 21,
      email: 'rahul@example.com',
      city: 'Bangalore'
    }
  ]
}
{
  _id: ObjectId('68c286b2cff9a81d61ff321a'),
  student_id: 2,
  course_id: 101,
  grade: 'A',
  student_info: [
    {
      _id: 2,
      name: 'Priya Singh',
      age: 22,
      email: 'priya@example.com',
      city: 'Delhi'
    }
  ]
}
{
  _id: ObjectId('68c286b2cff9a81d61ff321b'),
  student_id: 3,
  course_id: 102,
  grade: 'C',
  student_info: [
    {
      _id: 3,
      name: 'Aman Kumar',
      age: 20,
      email: 'amankumar@university.com',
      city: 'Hyderabad'
    }
  ]
}
{
  _id: ObjectId('68c286b2cff9a81d61ff321c'),
  student_id: 4,
  course_id: 104,
  grade: 'B',
  student_info: []
}

// Show all students with the list of courses they enrolled in (nested $lookup ).
db.students.aggregate([
  {
    $lookup: {
      from: "enrollments",
      localField: "_id",
      foreignField: "student_id",
      as: "enrolled_courses"
    }
  },
  {
    $lookup: {
      from: "courses",
      localField: "enrolled_courses.course_id",
      foreignField: "_id",
      as: "course_details"
    }
  }
]);

{
  _id: 1,
  name: 'Rahul Sharma',
  age: 21,
  email: 'rahul@example.com',
  city: 'Bangalore',
  enrolled_courses: [
    {
      _id: ObjectId('68c286b2cff9a81d61ff3218'),
      student_id: 1,
      course_id: 101,
      grade: 'A'
    },
    {
      _id: ObjectId('68c286b2cff9a81d61ff3219'),
      student_id: 1,
      course_id: 103,
      grade: 'B'
    }
  ],
  course_details: [
    {
      _id: 103,
      title: 'Economics 101',
      department: 'Economics',
      credits: 2
    },
    {
      _id: 101,
      title: 'Database Systems',
      department: 'CS',
      credits: 4
    }
  ]
}
{
  _id: 2,
  name: 'Priya Singh',
  age: 22,
  email: 'priya@example.com',
  city: 'Delhi',
  enrolled_courses: [
    {
      _id: ObjectId('68c286b2cff9a81d61ff321a'),
      student_id: 2,
      course_id: 101,
      grade: 'A'
    }
  ],
  course_details: [
    {
      _id: 101,
      title: 'Database Systems',
      department: 'CS',
      credits: 4
    }
  ]
}
{
  _id: 3,
  name: 'Aman Kumar',
  age: 20,
  email: 'amankumar@university.com',
  city: 'Hyderabad',
  enrolled_courses: [
    {
      _id: ObjectId('68c286b2cff9a81d61ff321b'),
      student_id: 3,
      course_id: 102,
      grade: 'C'
    }
  ],
  course_details: [
    {
      _id: 102,
      title: 'Data Structures',
      department: 'CS',
      credits: 3
    }
  ]
}
{
  _id: 5,
  name: 'Karan Mehta',
  age: 21,
  email: 'karan@example.com',
  city: 'Mumbai',
  enrolled_courses: [],
  course_details: []
}

// Count how many students got grade "A" .
db.enrollments.countDocuments({ grade: "A" });
2
