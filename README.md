# OpenWhisk Prototype
Spike for OpenWhisk implementation for a language learning platform.

## Course-Endpoints:
All Course-Actions are reachable on the endpoint `/courses `
###createCourse
**POST**-call to create a new course.
 
 Parameters:

    "course_id": "3",
    "description": "Grundlagen der Sprache",
    "duration": "2h",
    "end_date": "31.02.2019",
    "start_date": "01.10.2019",
    "time": "3h",
    "topic": "Spanisch für Anfänger",
    "weekday": "Monday"

###deleteCourse
**DELETE**-call to delete a existing course. 

Parameters:

`    "course_id": "3"`
###getCourse
**GET**-call to get all courses or the details of a specific course.

Parameters:

empty or only the course id

`    "course_id": "3"`

###updateCourse
**PUT**-call to _update_ an existing course.

    "course_id": "3",                               
    "description": "Grundlagen der Sprache",
    "duration": "2h",
    "end_date": "31.02.2019",
    "start_date": "01.10.2019",
    "time": "3h",
    "topic": "Spanisch für Anfänger",
    "weekday": "Monday"

The parameter "course_id" must be an existing ID in the course database. 

###checkMondays
reachable on the endpoint `/courses/forgetMondays`

Demonstration of the function-sequenece. Works with the same parameters like the createCourse-Action and modifies the "weekday"-parameter (Nobody likes mondays... lets start on tuesday). 