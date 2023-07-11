CREATE TABLE department
(   
    dept_id INT PRIMARY KEY, 
    name varchar(100) NOT NULL
);

CREATE TABLE course
( 
    course_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    sem INT NOT NULL,
    dept_id INT REFERENCES department(dept_id) 
);  

CREATE TABLE student
(   
  auid INT PRIMARY KEY, 
  password VARCHAR(50) NOT NULL,
  firstName varchar(50) NOT NULL, 
  lastName varchar(50),   
  email varchar(320) UNIQUE NOT NULL, 
  course_id int REFERENCES course(course_id)
); 

CREATE TABLE subject
( 
  subject_id INT PRIMARY KEY CHECK (subject_id >= 100 AND subject_id <= 999),
  title VARCHAR(200)NOT NULL,
  image BYTEA 
); 

CREATE TABLE course_subject
( 
  subject_id INT REFERENCES subject(subject_id),
  course_id INT REFERENCES course(course_id), 
  PRIMARY KEY(subject_id,course_id)
); 
CREATE TABLE timimg
( 
  subject_id INT REFERENCES subject(subject_id), 
  start_date TIMESTAMP NOT NULL,
  end_date TIMESTAMP NOT NULL, 
  duration INT NOT NULL,
  PRIMARY KEY(subject_id)
);


CREATE TABLE question
( 
  question_id SERIAL PRIMARY KEY,
  subject_id INT REFERENCES subject(subject_id), 
  question VARCHAR(1000),
  option_1 VARCHAR(200), 
  option_2 VARCHAR(200),
  option_3 VARCHAR(200), 
  option_4 VARCHAR(200),  
  answer VARCHAR(200) 
);  

CREATE TABLE answer
(
  auid INT REFERENCES student(auid), 
  question_id INT REFERENCES question(question_id),
  student_answer VARCHAR(200), 
  PRIMARY KEY(AUID,question_id)
);


CREATE TABLE submit
(
  auid INT REFERENCES student(auid),
  subject_id INT REFERENCES subject(subject_id), 
  PRIMARY KEY (auid,subject_id) 
);
