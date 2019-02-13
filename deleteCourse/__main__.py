import couchdb
from couchdb import Server

couchserver = Server("http://172.18.0.12:5984")

dbname = "course"
if dbname in couchserver:
    db = couchserver[dbname]
else:
    db = couchserver.create(dbname)

def main(params):
    course_id = params['course_id']
    doc = db.get(course_id)
    if doc:
        db.delete(doc)
        return {
            'course_id': course_id,
            'success': 'true'
        }
    else:
        return {
            'course_id': course_id,
            'success': 'false',
            'message': 'Course does not exists'
        }
