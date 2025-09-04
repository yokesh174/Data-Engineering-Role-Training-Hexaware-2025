CREATE DATABASE company_db;

USE company_db;

CREATE TABLE Employees (
	Employee_ID INT PRIMARY KEY AUTO_INCREMENT,
    First_Name VARCHAR(50) NOT NULL,
    Last_Name VARCHAR(50) NOT NULL,
    Age INT,
    Department VARCHAR(100),
    Salary INT
);

INSERT INTO Employees (First_Name, Last_Name, Age, Department, Salary) VALUES
('Arun', 'Kumar', 23, 'IT', 25000),
('Arjun', 'Doss', 24, 'Marketing', 24000),
('Leo', 'Dass', 25, 'HR', 30000),
('Priya', 'Jeson', 22, 'Finance', 28000),
('Vimal', 'Vijay', 27, 'IT', 27000);

SELECT * FROM Employees;

SELECT First_Name, Department, Salary FROM Employees
WHERE Department = 'IT';

UPDATE Employees
SET Department = 'Accounts'
WHERE Employee_id = 4;

SELECT * FROM Employees;

DELETE FROM Employees
WHERE Employee_ID = 3;

SELECT * FROM Employees;
