-- Insertion Students
INSERT INTO Students (student_id, name, age, gender) VALUES
(1, 'Alice', 20, 'F'),
(2, 'Bob', 22, 'M'),
(3, 'Clara', 19, 'F'),
(4, 'David', 21, 'M'),
(5, 'Eva', 23, 'F'),
(6, 'Franck', 20, 'M'),
(7, 'Gina', 22, 'F'),
(8, 'Hugo', 21, 'M'),
(9, 'Isabelle', 20, 'F'),
(10, 'Jules', 23, 'M');

-- Insertion Courses
INSERT INTO Courses (course_id, course_name, credits, capacity) VALUES
(1, 'Mathematics', 5, 30),
(2, 'Physics', 4, 25),
(3, 'Computer Science', 3, 20),
(4, 'History', 3, 15);

-- Insertion Enrollments
INSERT INTO Enrollments (student_id, course_id) VALUES
(1, 1),
(2, 1), 
(3, 2),
(4, 2),
(5, 3),
(6, 4),
(7, 3), 
(8, 4); 