INSERT INTO department(dept_id,name) 
VALUES (1000,'Computer science'), 
        (1001,'Physics'), 
        (1002,'Chemistry'), 
        (1003,'Math'); 
 
 
INSERT INTO course(course_id,name,sem,dept_id) 
VALUES (10,'BCA',1,1000), 
        (11,'BCA',2,1000), 
        (12,'BCA',3,1000), 
        (13,'BCA',4,1000), 
        (14,'BCA',5,1000), 
        (15,'BCA',6,1000), 
        (16,'BTech',1,1000), 
        (17,'BTech',2,1000), 
        (18,'BTech',3,1000), 
        (19,'BTech',4,1000), 
        (20,'BTech',5,1000), 
        (21,'BTech',6,1000), 
        (22,'BTech',7,1000), 
        (23,'BTech',8,1000); 
 
INSERT INTO student(auid,password,firstname,lastname,email,course_id) 
VALUES (222706013,12345,'naresh','kumar','nkk124421@gmail.com',11), 
       (222706014,12345,'shahsinder','sharma','shashibhardwaaj@gmail.com',11), 
       (227106001,12345,'tarandeep','singh','tarandep@gmail.com',17), 
       (227106009,12345,'gurparvez','singh','gurparvez04@gmail.com',17); 
 
INSERT INTO subject 
VALUES  (101,'Digital Electronics'), 
         (102,'C Language'), 
         (103,'Communication SKills'), 
         (104,'Basic Math'), 
         (105,'Fundamentals of Computer'), 
         (106,'Inorganic Chemistry'), 
         (107,'General Math'), 
         (108,'Genral Physics'), 
         (109,'Engineering Bio'), 
         (110,'Relational Database Management System'), 
         (111,'Object Oriented Programming'), 
         (112,'Python'), 
         (113,'Computer Science Architecture'), 
         (114,'Statistics'); 
 
INSERT INTO course_subject 
VALUES 
        --bca 1: 
        (101,10), 
        (102,10), 
        (103,10), 
        (104,10), 
        (105,10), 
 
        --Btech 1: 
        (102,16), 
        (103,16), 
        (106,16), 
        (107,16), 
        (108,16), 
        (109,16), 
 
        --bca 2: 
        (110,11), 
        (111,11), 
        (112,11), 
        (113,11), 
 
        -- btech 2: 
        (110,17), 
        (111,17), 
        (112,17), 
        (113,17), 
        (114,17); 