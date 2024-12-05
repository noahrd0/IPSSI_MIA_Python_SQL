# University Enrollment Management System

This project demonstrates the creation and management of a university enrollment system using SQL. The project includes creating database schemas, populating tables with sample data, and executing various queries to retrieve and manipulate data.

## Files

- `schema.sql`: Contains the SQL commands to create the database schema.
- `data.sql`: Contains the SQL commands to populate the tables with sample data.
- `queries.sql`: Contains the SQL queries to perform various tasks and retrieve information from the database.

## Database Schema

The database consists of three tables: `Students`, `Courses`, and `Enrollments`.

### Students Table

Tracks student details.

| Column     | Type         | Description          |
|------------|--------------|----------------------|
| student_id | INT          | Primary key          |
| name       | VARCHAR(50)  | Student's name       |
| age        | INT          | Student's age        |
| gender     | VARCHAR(10)  | Student's gender     |

### Courses Table

Stores information about university courses.

| Column     | Type         | Description          |
|------------|--------------|----------------------|
| course_id  | INT          | Primary key          |
| course_name| VARCHAR(50)  | Course name          |
| credits    | INT          | Number of credits    |
| capacity   | INT          | Course capacity      |

### Enrollments Table

Links students to courses.

| Column        | Type         | Description                          |
|---------------|--------------|--------------------------------------|
| enrollment_id | INT          | Primary key, auto-increment          |
| student_id    | INT          | Foreign key referencing `Students`   |
| course_id     | INT          | Foreign key referencing `Courses`    |

## Sample Data

The `data.sql` file populates the tables with the following sample data:

### Students

| student_id | name      | age | gender |
|------------|-----------|-----|--------|
| 1          | Student1  | 20  | Female |
| 2          | Student2  | 22  | Male   |
| 3          | Student3  | 21  | Male   |
| 4          | Student4  | 23  | Female |
| 5          | Student5  | 24  | Male   |

### Courses

| course_id | course_name | credits | capacity |
|-----------|-------------|---------|----------|
| 1         | Maths       | 3       | 2        |
| 2         | Physics     | 4       | 3        |
| 3         | Tech        | 3       | 2        |
| 4         | Biology     | 4       | 3        |

### Enrollments

| enrollment_id | student_id | course_id |
|---------------|------------|-----------|
| 1             | 1          | 1         |
| 2             | 2          | 1         |
| 3             | 3          | 2         |
| 4             | 4          | 2         |
| 5             | 5          | 2         |
| 6             | 1          | 3         |
| 7             | 2          | 3         |
| 8             | 3          | 4         |
| 9             | 4          | 4         |