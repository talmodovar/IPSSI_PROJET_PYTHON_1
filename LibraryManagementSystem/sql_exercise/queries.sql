-- Tâche 3: Demande de renseignements sur les inscriptions des élèves

-- 3.1
Select T1.name, T3.course_name , T3.credits

from students as T1
inner join enrollments as T2 on (T1.student_id = T2.student_id)
inner join courses as T3 on (T2.course_id = T3.course_id)


-- 3.2
Select T1.name, T2.student_id, 'Pas de cours' as course

from students as T1
left join enrollments as T2 on (T1.student_id = T2.student_id)
where T2.student_id IS NULL;




-- Tâche 4 : Statistiques des cours d'information

-- 4.1
Select T1.course_name, count( T2.student_id) AS num_enrollments
from courses as T1
inner join enrollments as T2 on (T1.course_id = T2.course_id)
group by 1


-- 4.2
Select T1.course_name, count( T2.student_id) AS num_enrollments
from courses as T1
inner join enrollments as T2 on (T1.course_id = T2.course_id)
group by T1.course_name, T1.capacity
HAVING COUNT(T2.student_id) > T1.capacity / 2;



-- Tâche 5: Analyse avancée des inscriptions

-- 5.1
SELECT T1.name, COUNT(T2.course_id) AS num_courses
FROM students AS T1
INNER JOIN enrollments AS T2 ON T1.student_id = T2.student_id
GROUP BY T1.student_id, T1.name
HAVING COUNT(T2.course_id) = (
    SELECT MAX(course_count)
    FROM (
        SELECT COUNT(course_id) AS course_count
        FROM enrollments
        GROUP BY student_id
    ) AS subquery
);


-- 5.2
SELECT T1.student_id, T1.name, SUM(T3.credits) AS total_credits
FROM Students as T1
JOIN Enrollments as T2 ON T1.student_id = T2.student_id
JOIN Courses as T3 ON T2.course_id = T3.course_id
GROUP BY T1.student_id, T1.name;


-- 5.3
SELECT T3.course_name
FROM courses AS T3
LEFT JOIN enrollments AS T2 ON T3.course_id = T2.course_id
WHERE T2.student_id IS NULL;






-- Tâche 7: Données de propreté et de réinitialisation

-- 7.1
DELETE FROM enrollments
WHERE course_id = 2;


-- 7.2
DELETE FROM students
WHERE student_id NOT IN (
    SELECT DISTINCT student_id
    FROM enrollments
);