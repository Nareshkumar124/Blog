SELECT count(*) FILTER(WHERE question.answer=answer.student_answer) as right,
count(*) FILTER(WHERE question.answer!=answer.student_answer and answer.student_answer!='NOT' ) as wrong,
count(*) FILTER(WHERE answer.student_answer='NOT') as Not_attepted
FROM student JOIN course_subject
USING(course_id)
JOIN question USING(subject_id)
JOIN answer USING(question_id)
WHERE subject_id=112 and student.auid=222706013;




SELECT subject.subject_id,title from student
JOIN course_subject USING(course_id)
JOIN subject USING(subject_id) JOIN submit USING(auid,subject_id)
WHERE student.auid=222706013;



-- SELECT 
-- count(*) FILTER(WHERE question.answer=answer.student_answer) as right,
-- count(*) FILTER(WHERE question.answer!=answer.student_answer and answer.student_answer!='NOT' ) as wrong,
-- count(*) FILTER(WHERE answer.student_answer='NOT') as Not_attepted
-- FROM answer
-- JOIN question USING(question_id) 
-- WHERE auid=222706013 and subject_id = 112;

SELECT * FROM submit;