import couchdb
from couchdb import Server

couchserver = Server("http://172.18.0.12:5984")

dbname = "course"
if dbname in couchserver:
    db = couchserver[dbname]
else:
    db = couchserver.create(dbname)
    
# methode to create a new course from POST-call
def main(params):
    course_id = params['course_id']
    topic = params['topic']
    description = params['description']
    duration = params['duration']
    weekday = params['weekday']
    time = params['time']
    start_date = params['start_date']
    end_date = params['end_date']

    doc_id, doc_rev = db.save({"_id": course_id, "course_id": course_id, "topic": topic, "description": description, "duration": duration, "weekday": weekday, "time":time, "start_date": start_date, "end_date": end_date})

    return {
        'course_id': course_id,
        'topic': topic,
        "description": description,
        "duration": duration,
        "weekday": weekday,
        "time": time,
        "start_date": start_date,
        "end_date": end_date
    }
