CREATE DATABASE student_db;

USE student_db;

CREATE TABLE Students (
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INT,
    course VARCHAR(50)
);

INSERT INTO Students (name, age, course) VALUES ('Rahul Sharma', 21, 'Data Engineer'),
('Priya Singh', 22, 'AI Engineer'),
('Aman Kumar', 23, 'Data Science');

SELECT * FROM students;

SELECT name, course FROM students
WHERE age > 21;

UPDATE students
SET course = 'Machine Learning'
WHERE id = 2;

DELETE FROM students
WHERE id = 3;
