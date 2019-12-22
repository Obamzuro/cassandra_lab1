DROP TABLE obamzuro.student;
DROP TABLE obamzuro.subject_lab;
DROP TABLE obamzuro.lab_result;
DROP KEYSPACE obamzuro;

CREATE KEYSPACE obamzuro 
WITH replication = {
	'class': 'SimpleStrategy', 
	'replication_factor': 2
};

CREATE TABLE obamzuro.subject_lab
(
	subject_id int,
	subject_name text STATIC,
	lab_id int,
	lab_number int,
	PRIMARY KEY (subject_id, lab_id)
);

CREATE TYPE IF NOT EXISTS obamzuro.subject_skill
(
	subject_id set<int>,
	date_of_creating text	
);

CREATE TYPE IF NOT EXISTS obamzuro.student_info_type
(
	name text,
	surname text,
	course int
);

CREATE TABLE obamzuro.student(
	student_id int,
	completed_labs_counter int,
	student_subject_skill map<text, frozen<subject_skill>>,
	student_info frozen<student_info_type>,
	PRIMARY KEY (student_id)
);

CREATE TABLE obamzuro.lab_result(
	lab_id int,
	student_id int,
	is_passed boolean,
	PRIMARY KEY (student_id, lab_id)
);