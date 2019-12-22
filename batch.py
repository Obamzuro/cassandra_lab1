from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
from cassandra import ConsistencyLevel

cluster = Cluster(['127.0.0.1'], port=9042)
session = cluster.connect('obamzuro', wait_for_all_pools=True)
session.execute('USE obamzuro')

query = SimpleStatement("""BEGIN BATCH
	INSERT INTO obamzuro.subject_lab (subject_id, lab_id, lab_number, subject_name) VALUES(1, 1, 1, 'Math');
    INSERT INTO obamzuro.lab_result(lab_id, student_id, is_passed) VALUES (1, 0, true);
APPLY BATCH;""", consistency_level=ConsistencyLevel.ONE)
session.execute(query)