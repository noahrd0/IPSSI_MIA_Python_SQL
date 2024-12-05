-- Query 1
SELECT 
    Students.student_id, 
    Students.name AS student_name, 
    Courses.course_name, 
    Courses.credits
FROM 
    Enrollments
JOIN 
    Students ON Enrollments.student_id = Students.student_id
JOIN 
    Courses ON Enrollments.course_id = Courses.course_id;

-- Query 2
SELECT 
    Students.student_id, 
    Students.name AS student_name
FROM 
    Students
LEFT JOIN 
    Enrollments ON Students.student_id = Enrollments.student_id
WHERE 
    Enrollments.student_id IS NULL;

-- Query 3
SELECT 
    Courses.course_id, 
    Courses.course_name, 
    COUNT(Enrollments.student_id) AS number_of_students
FROM 
    Courses
LEFT JOIN 
    Enrollments ON Courses.course_id = Enrollments.course_id
GROUP BY 
    Courses.course_id, Courses.course_name;

-- Query 4
SELECT 
    Courses.course_id, 
    Courses.course_name, 
    COUNT(Enrollments.student_id) AS number_of_students, 
    Courses.capacity
FROM 
    Courses
LEFT JOIN 
    Enrollments ON Courses.course_id = Enrollments.course_id
GROUP BY 
    Courses.course_id, Courses.course_name, Courses.capacity
HAVING 
    COUNT(Enrollments.student_id) > (Courses.capacity / 2);

-- Query 5
SELECT 
    Students.student_id, 
    Students.name, 
    COUNT(Enrollments.course_id) AS number_of_courses
FROM 
    Students
JOIN 
    Enrollments ON Students.student_id = Enrollments.student_id
GROUP BY 
    Students.student_id, Students.name
HAVING 
    COUNT(Enrollments.course_id) = (
        SELECT 
            MAX(course_count)
        FROM (
            SELECT 
                COUNT(course_id) AS course_count
            FROM 
                Enrollments
            GROUP BY 
                student_id
        ) AS subquery
    )
LIMIT 0, 25;

-- Query 6
SELECT 
    Students.student_id, 
    Students.name, 
    SUM(Courses.credits) AS total_credits
FROM 
    Students
JOIN 
    Enrollments ON Students.student_id = Enrollments.student_id
JOIN 
    Courses ON Enrollments.course_id = Courses.course_id
GROUP BY 
    Students.student_id, Students.name;

-- Query 7
SELECT 
    Courses.course_id, 
    Courses.course_name
FROM 
    Courses
LEFT JOIN 
    Enrollments ON Courses.course_id = Enrollments.course_id
WHERE 
    Enrollments.course_id IS NULL;

-- Task 6 && 7