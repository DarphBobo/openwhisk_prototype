import couchdb
import json
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

# action to get a single course or a list of all courses
def main(params):
    # check if list or detail
    if "course_id" in params:
        course_id = params['course_id']
        # get course detail
        doc = db.get(course_id)
        if doc:
            # return detail
            return {
                'course': doc,
                'success': 'true',
                'params': params
            }
        else:
            # no such course
            return {
                'course_id': course_id,
                'success': 'false',
                'message': 'Course not found'
            }
    else:
        courses = []
        # get list of all courses
        for docid in db.view('_all_docs'):
            courses.append(docid)
        return {
            'courses': courses,
            'success': 'true'
        }
