INSERT INTO Students (student_id, name, age, gender) VALUES
(1, 'Student1', 20, 'Female'),
(2, 'Student2', 22, 'Male'),
(3, 'Student3', 21, 'Male'),
(4, 'Student4', 23, 'Female'),
(5, 'Student5', 24, 'Male');

INSERT INTO Courses (course_id, course_name, credits, capacity) VALUES
(1, 'Maths', 3, 2),
(2, 'Physics', 4, 3),
(3, 'Tech', 3, 2),
(4, 'Biology', 4, 3);

INSERT INTO Enrollments (student_id, course_id) VALUES
(1, 1),
(2, 1),
(3, 2),
(4, 2),
(5, 2),
(1, 3),
(2, 3),
(3, 4),
(4, 4);
