import couchdb
from couchdb import Server

#
# This was part of a student project the Munich University of Applied Sciences.
# https://github.com/DarphBobo/openwhisk_prototype
#

couchserver = Server("http://172.18.0.12:5984")

dbname = "course"
if dbname in couchserver:
    db = couchserver[dbname]
else:
    db = couchserver.create(dbname)

# action to delete a course from a DELETE-call. 
def main(params):
    course_id = params['course_id']
    # search doc
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
