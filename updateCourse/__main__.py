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
    
# action to update an existing course from  
def main(params):
    course_id = params['course_id']
    topic = params['topic']
    description = params['description']
    duration = params['duration']
    weekday = params['weekday']
    time = params['time']
    start_date = params['start_date']
    end_date = params['end_date']
    
    # get course by id
    doc = db.get(course_id)
    
    # update fields
    if doc:
        if topic:
            doc["topic"] = topic
        if description:
            doc["description"] = description
        if duration:
            doc["duration"] = duration
        if weekday:
            doc["weekday"] = weekday
        if time:
            doc["time"] = time
        if start_date:
            doc["start_date"] = start_date
        if end_date:
            doc["end_date"] = end_date
        # persist
        doc_id, doc_rev = db.save(doc)
        return {
            'course_id': course_id,
            'doc_id': doc_id,
            "doc_rev": doc_rev,
            'success': 'true'
        }
    else:
        return {
            'course_id': course_id,
            'success': 'false',
            'message': 'Course does not exists'
        }
