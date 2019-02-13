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
    
# methode to create a new course from POST-call
def main(params):
    # get params
    course_id = params['course_id']
    topic = params['topic']
    description = params['description']
    duration = params['duration']
    weekday = params['weekday']
    time = params['time']
    start_date = params['start_date']
    end_date = params['end_date']
    
    # persist
    doc_id, doc_rev = db.save({"_id": course_id, "course_id": course_id, "topic": topic, "description": description, "duration": duration, "weekday": weekday, "time":time, "start_date": start_date, "end_date": end_date})

    return {
        'course_id': course_id,
        'doc_id': doc_id,
        "doc_rev": doc_rev,
        "success": 'true'
    }
