#!/bin/bash
wsk action delete createCourse -i
wsk action delete deleteCourse -i
wsk action delete updateCourse -i
wsk action delete getCourse -i
wsk action delete checkMondays -i
wsk action delete forgetMondays -i

wsk api delete / -i
wsk api delete /courses -i
