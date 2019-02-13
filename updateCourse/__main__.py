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
    topic = params['topic']
    description = params['description']
    duration = params['duration']
    weekday = params['weekday']
    time = params['time']
    start_date = params['start_date']
    end_date = params['end_date']
    
    doc = db.get(course_id)
    
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
            
        db.save(doc)
        return {
            'course_id': course_id,
            'topic': topic,
            "description": description,
            "duration": duration,
            "weekday": weekday,
            "time": time,
            "start_date": start_date,
            "end_date": end_date,
            'success': 'true'
        }
    else:
        return {
            'course_id': course_id,
            'success': 'false',
            'message': 'Course does not exists'
        }
