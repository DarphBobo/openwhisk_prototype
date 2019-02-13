import couchdb
import json

from couchdb import Server

couchserver = Server("http://172.18.0.12:5984")

dbname = "course"
if dbname in couchserver:
    db = couchserver[dbname]
else:
    db = couchserver.create(dbname)

def main(params):
    if "course_id" in params:
        course_id = params['course_id']
        doc = db.get(course_id)
        if doc:
            return {
                'course': doc,
                'success': 'true',
                'params': params
            }
        else:
            return {
                'course_id': course_id,
                'success': 'true',
                'message': 'Course not found'
            }
    else:
        courses = []
        for docid in db.view('_all_docs'):
            courses.append(docid)
        return {
            'courses': courses,
            'success': 'true'
        }
