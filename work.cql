INSERT INTO obamzuro.student JSON
	'{
		"student_id": 0,
		"completed_labs_counter": 2, 
		"student_info": {"name": "Ivan", "surname": "Ivanov", "course": 4}, 
		"student_subject_skill": {
			"A": {
				"subject_id": [1], 
				"date_of_creating": "13.12.2008"}, 
			"C": {
				"subject_id": [3], 
				"date_of_creating": "13.12.2008"}, 
			"E": {
				"subject_id": [2], 
				"date_of_creating": "13.12.2008"}
		}
	}';
INSERT INTO obamzuro.student JSON
	'{
		"student_id": 1,
		"completed_labs_counter": 2, 
		"student_info": {"name": "Oleg", "surname": "Nebamzurov", "course": 4}, 
		"student_subject_skill": {
			"A": {
				"subject_id": [2], 
				"date_of_creating": "3.12.2008"}, 
			"C": {
				"subject_id": [1], 
				"date_of_creating": "3.12.2008"}, 
			"E": {
				"subject_id": [3], 
				"date_of_creating": "3.12.2008"}
		}
	}';
INSERT INTO obamzuro.student JSON
	'{
		"student_id": 2,
		"completed_labs_counter": 1, 
		"student_info": {"name": "Andrey", "surname": "Kosolapov", "course": 4}, 
		"student_subject_skill": {
			"A": {
				"subject_id": [3], 
				"date_of_creating": "13.2.2008"}, 
			"C": {
				"subject_id": [1], 
				"date_of_creating": "13.2.2008"}, 
			"E": {
				"subject_id": [2], 
				"date_of_creating": "13.2.2008"}
		}
	}';
SELECT * FROM obamzuro.student;
INSERT INTO obamzuro.subject_lab (subject_id, lab_id, lab_number, subject_name) VALUES(
	1, 1, 1, 'Math'
);
INSERT INTO obamzuro.subject_lab (subject_id, lab_id, lab_number, subject_name) VALUES(
	1, 2, 2, 'Math'
);
INSERT INTO obamzuro.subject_lab (subject_id, lab_id, lab_number, subject_name) VALUES(
	1, 3, 3, 'Math'
);
INSERT INTO obamzuro.subject_lab (subject_id, lab_id, lab_number, subject_name) VALUES(
	2, 4, 1, 'Physics'
);
INSERT INTO obamzuro.subject_lab (subject_id, lab_id, lab_number, subject_name) VALUES(
	2, 5, 2, 'Physics'
);
INSERT INTO obamzuro.subject_lab (subject_id, lab_id, lab_number, subject_name) VALUES(
	2, 6, 3, 'Physics'
);
SELECT * FROM obamzuro.subject_lab;
INSERT INTO obamzuro.lab_result(
	lab_id,
	student_id,
	is_passed)
VALUES (
	1, 0, true
);
INSERT INTO obamzuro.lab_result(
	lab_id,
	student_id,
	is_passed)
VALUES (
	2, 0, false
);
INSERT INTO obamzuro.lab_result(
	lab_id,
	student_id,
	is_passed)
VALUES (
	3, 0, true
);
SELECT * FROM obamzuro.lab_result;
UPDATE obamzuro.lab_result set is_passed=true where student_id=0 and lab_id=2;
select * from obamzuro.lab_result;
UPDATE obamzuro.subject_lab set subject_name='Phys' where subject_id=2;
select * from obamzuro.subject_lab;
UPDATE obamzuro.student set student_info={"name": 'Vanya', "surname":'Ivanov', "course": 4} where student_id=0;
select * from obamzuro.student;
select student_id, lab_id, is_passed
from obamzuro.lab_result;
select subject_name, lab_id
from obamzuro.subject_lab;
delete subject_name from obamzuro.subject_lab where subject_id=2;
select * from obamzuro.subject_lab;
delete student_info from obamzuro.student where student_id=0;
select * from obamzuro.student;
delete completed_labs_counter from obamzuro.student where student_id=0;
select * from obamzuro.student;