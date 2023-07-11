--CPP-------------------------------------------
INSERT INTO question (subject_id, question, option_1, option_2, option_3, option_4, answer)
VALUES 

(111, 'What is the output of the following code? int x = 5; cout << ++x + x++;', 
   '11',
   '12',
   '10',
   'Compiler Error', 
   '12'),

(111, 'Which of the following is a valid C++ identifier?', 
   'my_variable', 
   '2nd_variable', 
   '$var', 
   'for', 
   'my_variable'),
  
(111, 'What is the output of the following C++ code? int x = 5; cout << x++;', 
   '5', 
   '6', 
   'Compiler error', 
   'Undefined behavior', 
   '5'),

(111, 'Which of the following is a correct way to allocate memory dynamically in C++?', 
 'int* p = new int;', 
 'int p = new int;', 
 'int* p = malloc(sizeof(int));', 
 'int* p = new int[10];', 
 'int* p = new int;'),

(111, 'What is the output of the following C++ code? int arr[] = {1, 2, 3}; cout << arr[3];', 
 'Compiler error', 
 'Undefined behavior', 
 '0', 
 'Garbage value', 
 'Undefined behavior'),
 
 (111, 'What is the purpose of the keyword "const" in C++?', 
  'To make a variable immutable', 
  'To make a variable mutable', 
  'To make a function constant', 
  'To make a function mutable', 
  'To make a variable immutable'),

(111, 'What is C++?', 
 'A programming language', 
 'A markup language', 
 'A scripting language', 
 'A styling language', 
 'A programming language'),
 
 (111, 'What is the use of inheritance in C++?', 
  'To reuse the code', 
  'To create objects',
  'To allocate memory',
  'To perform operations on data', 
  'To reuse the code'),

(111, 'What is the difference between C and C++?',
 'C++ supports oops', 
 'C++ is a procedural language', 
 'C is a high-level language', 
 'C++ is a low-level language', 
 'C++ supports oops'),

(111, 'What is the use of inheritance in C++?', 
 'To reuse the code', 
 'To create objects', 
 'To allocate memory', 
 'To perform operations', 
 'To reuse the code');


--RDBMS
INSERT INTO question (subject_id, question, option_1, option_2, option_3, option_4, answer)  
VALUES  
    (110, 'Which of the following is not a type of join in SQL?', 'Inner join', 'Outer join', 'Cross join', 'Center join', 'Center join'), 
     
    (110, 'What is the command used to create a new database in SQL?', 'CREATE DATABASE', 'CREATE TABLE', 'CREATE SCHEMA', 'CREATE INDEX', 'CREATE DATABASE'), 
     
    (110, 'Which of the following is not a valid data type in SQL?', 'INT', 'VARCHAR', 'FLOAT', 'BOOLEAN', 'BOOLEAN'), 
     
    (110, 'What is the command used to delete a table in SQL?', 'DROP TABLE', 'DELETE TABLE', 'REMOVE TABLE', 'ERASE TABLE', 'DROP TABLE'), 
     
    (110, 'What is the command used to add a new column to an existing table in SQL?', 'ALTER TABLE', 'ADD COLUMN', 'CREATE COLUMN', 'INSERT COLUMN', 'ALTER TABLE'), 
     
    (110, 'Which of the following is a constraint in SQL that ensures that all values in a column are unique?', 'PRIMARY KEY', 'FOREIGN KEY', 'CHECK', 'UNIQUE', 'UNIQUE'), 
     
    (110, 'Which of the following is not a function in SQL?', 'AVG', 'SUM', 'LEN', 'COUNT', 'LEN'), 
     
    (110, 'What is the command used to add a new row to a table in SQL?', 'INSERT INTO', 'ADD ROW', 'CREATE ROW', 'NEW ROW', 'INSERT INTO'), 
     
    (110, 'Which of the following is a clause in SQL that is used to filter rows based on specified conditions?', 'WHERE', 'GROUP BY', 'HAVING', 'ORDER BY', 'WHERE'), 
     
    (110, 'What is the command used to modify the data in a table in SQL?', 'UPDATE', 'MODIFY', 'CHANGE', 'ALTER', 'UPDATE');

--Python

INSERT INTO question (subject_id, question, option_1, option_2, option_3, option_4, answer) VALUES 
    (112, 'What is the output of the following Python code? x = "hello" y = x[1:3] print(y)', 'el', 'he', 'ho', 'lo', 'el'),    
    (112, 'What is the output of the following Python code? x = [1, 2, 3] y = x.pop() print(y)', '3', '2', '1', 'None', '3'),    
    (112, 'What is the output of the following Python code? x = [1, 2, 3] y = x[::-1] print(y)', '[3, 2, 1]', '[1, 2, 3]', '[3, 2]', '[2, 1, 3]', '[3, 2, 1]'),    
    (112, 'What is the output of the following Python code? x = "hello" y = x.upper() print(y)', 'HELLO', 'hello', 'H', 'h', 'HELLO'),    
    (112, 'What is the output of the following Python code? x = (1, 2, 3) y = list(x) y.append(4) print(y)', '[1, 2, 3, 4]', '[1, 2, 3]', '[4, 1, 2, 3]', '[1, 2, 4, 3]', '[1, 2, 3, 4]'),    
    (112, 'What is the output of the following Python code? x = [1, 2, 3] y = x[1:] y[0] = 4 print(x)', '[1, 2, 3]', '[4, 2, 3]', '[1, 4, 3]', '[1, 2, 4]', '[1, 2, 3]'),    
    (112, 'What is the output of the following Python code? x = "hello" y = x.split() print(y)', '["hello"]', '["h", "e", "l", "l", "o"]', '["he", "ll", "o"]', '[]', '["hello"]'),    
    (112, 'What is the output of the following Python code? x = [1, 2, 3] y = x.remove(2) print(y)', 'None', '1', '2', '[1, 3]', 'None'),    
    (112, 'What is the output of the following Python code? x = "hello" y = list(x) y[1] = "a" z = "".join(y) print(z)', 'hallo', 'hello', 'haaao', 'hlaao', 'hallo'),    
   (112, 'What is the output of the following Python code? x = {"a": 1, "b": 2} y = x.get("c", 3) print(y)', '3', '1', '2', 'c', '3');



--CAS
INSERT INTO question (subject_id, question, option_1, option_2, option_3, option_4, answer)
VALUES 
	(113, 'Which component of a computer is responsible for executing instructions?', 'Arithmetic logic unit', 'Control unit', 'Memory unit', 'Input/output unit', 'Control unit'),
	(113, 'What is the purpose of the arithmetic logic unit (ALU) in a computer?', 'To execute instructions', 'To store data', 'To perform arithmetic operations', 'To process data', 'To perform arithmetic operations'),
	(113, 'Which component of a computer is responsible for temporarily storing data that is being processed?', 'Arithmetic logic unit', 'Control unit', 'Memory unit', 'Input/output unit', 'Memory unit'),
	(113, 'What is the purpose of the input/output (I/O) unit in a computer?', 'To execute instructions', 'To perform arithmetic operations', 'To store data', 'To handle input and output operations', 'To handle input and output operations'),
	(113, 'Which type of memory is typically the fastest?', 'Read-only memory (ROM)', 'Random-access memory (RAM)', 'Cache memory', 'Virtual memory', 'Cache memory'),
	(113, 'Which type of memory is non-volatile?', 'Read-only memory (ROM)', 'Random-access memory (RAM)', 'Cache memory', 'Virtual memory', 'Read-only memory (ROM)'),
	(113, 'Which type of memory is used to store frequently accessed data for quick retrieval?', 'Read-only memory (ROM)', 'Random-access memory (RAM)', 'Cache memory', 'Virtual memory', 'Cache memory'),
	(113, 'What is the purpose of a bus in a computer?', 'To execute instructions', 'To store data', 'To perform arithmetic operations', 'To transfer data between components', 'To transfer data between components'),
	(113, 'Which component of a computer is responsible for permanently storing data?', 'Arithmetic logic unit', 'Control unit', 'Memory unit', 'Input/output unit', 'Memory unit'),
	(113, 'Which component of a computer is responsible for controlling the flow of data between the other components?', 'Arithmetic logic unit', 'Control unit', 'Memory unit', 'Input/output unit', 'Control unit');