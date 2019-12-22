from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
from cassandra import ConsistencyLevel

cluster = Cluster(['127.0.0.1'], port=9042)
session = cluster.connect('obamzuro', wait_for_all_pools=True)
session.execute('USE obamzuro')

query = SimpleStatement("""INSERT INTO obamzuro.student JSON '{"student_id": 0,"completed_labs_counter": 2, "student_info": {"name": "Ivan", "surname": "Ivanov", "course": 4},	"student_subject_skill": {"A": {"subject_id": [2], "date_of_creating": "13.12.2008"}, "C": {"subject_id": [3], "date_of_creating": "13.12.2008"}, "E": {"subject_id": [1],"date_of_creating": "13.12.2008"}}}';""", consistency_level=ConsistencyLevel.ONE)
query.consistency_level = ConsistencyLevel.ONE
session.execute(query)
query = SimpleStatement("""INSERT INTO obamzuro.student JSON '{"student_id": 1,"completed_labs_counter": 2, "student_info": {"name": "Oleg", "surname": "Nebamzurov", "course": 4},	"student_subject_skill": {"A": {"subject_id": [2], "date_of_creating": "3.12.2008"}, "C": {"subject_id": [1], "date_of_creating": "3.12.2008"}, "E": {"subject_id": [3],"date_of_creating": "3.12.2008"}}}';""", consistency_level=ConsistencyLevel.ONE)
query.consistency_level = ConsistencyLevel.ONE
session.execute(query)
query = SimpleStatement("""INSERT INTO obamzuro.student JSON '{"student_id": 2,"completed_labs_counter": 1, "student_info": {"name": "Andrey", "surname": "Kosolapov", "course": 4},	"student_subject_skill": {"A": {"subject_id": [3], "date_of_creating": "13.2.2008"}, "C": {"subject_id": [1], "date_of_creating": "3.12.2008"}, "E": {"subject_id": [2],"date_of_creating": "13.12.2008"}}}';""", consistency_level=ConsistencyLevel.ONE)
query.consistency_level = ConsistencyLevel.ONE
session.execute(query)
rows = session.execute("SELECT * FROM student;")
for row in rows:
    print(row)

query = SimpleStatement("""INSERT INTO obamzuro.subject_lab (subject_id, lab_id, lab_number, subject_name) VALUES(
	%s, %s, %s, %s
);""", consistency_level=ConsistencyLevel.ONE)
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, (1, 1, 1, 'Math'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, (1, 2, 2, 'Math'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, (1, 3, 3, 'Math'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, (2, 4, 1, 'Physics'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, (2, 5, 2, 'Physics'))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, (2, 6, 3, 'Physics'))

rows = session.execute("SELECT * FROM subject_lab;")
for row in rows:
    print(row)

query = SimpleStatement("""
INSERT INTO obamzuro.lab_result(
	lab_id,
	student_id,
	is_passed)
VALUES (
	%s, %s, %s
);""", consistency_level=ConsistencyLevel.ONE)
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, (1, 0, True))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, (2, 0, False))
query.consistency_level = ConsistencyLevel.ONE
session.execute(query, (3, 0, True))
rows = session.execute("SELECT * FROM lab_result;")
for row in rows:
    print(row)

query = SimpleStatement("""UPDATE obamzuro.lab_result set is_passed=true where student_id=0 and lab_id=2;""", consistency_level=ConsistencyLevel.ONE)
query.consistency_level = ConsistencyLevel.ONE
session.execute(query)
rows = session.execute("""select * from obamzuro.lab_result;""")
for row in rows:
    print(row)

query = SimpleStatement("""UPDATE obamzuro.subject_lab set subject_name='Phys' where subject_id=2;""", consistency_level=ConsistencyLevel.ONE)
query.consistency_level = ConsistencyLevel.ONE
session.execute(query)
rows = session.execute("""select * from obamzuro.subject_lab;""")
for row in rows:
    print(row)


query = SimpleStatement("""UPDATE obamzuro.student set student_info={"name": 'Vanya', "surname":'Ivanov', "course": 4} where student_id=0;""", consistency_level=ConsistencyLevel.ONE)
query.consistency_level = ConsistencyLevel.ONE
session.execute(query)
rows = session.execute("select * from obamzuro.student;")
for row in rows:
    print(row)

query = SimpleStatement("""select student_id, lab_id, is_passed
from obamzuro.lab_result;""", consistency_level=ConsistencyLevel.ONE)
query.consistency_level = ConsistencyLevel.ONE
session.execute(query)

query = SimpleStatement("""select subject_name, lab_id
from obamzuro.subject_lab;""", consistency_level=ConsistencyLevel.ONE)
query.consistency_level = ConsistencyLevel.ONE
session.execute(query)

query = SimpleStatement("""delete subject_name from obamzuro.subject_lab where subject_id=2;""", consistency_level=ConsistencyLevel.ONE)
query.consistency_level = ConsistencyLevel.ONE
session.execute(query)
rows = session.execute("select * from obamzuro.subject_lab;")
for row in rows:
    print(row)

query = SimpleStatement("""delete student_info from obamzuro.student where student_id=0;""", consistency_level=ConsistencyLevel.ONE)
query.consistency_level = ConsistencyLevel.ONE
session.execute(query)
rows = session.execute("select * from obamzuro.student;")
for row in rows:
    print(row)

query = SimpleStatement("""delete completed_labs_counter from obamzuro.student where student_id=0;""", consistency_level=ConsistencyLevel.ONE)
query.consistency_level = ConsistencyLevel.ONE
session.execute(query)
rows = session.execute("select * from obamzuro.student;")
for row in rows:
    print(row)