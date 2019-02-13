#!/bin/bash
cd ./deleteCourse
/bin/bash deploy.sh
cd ../createCourse
/bin/bash deploy.sh
cd ../updateCourse
/bin/bash deploy.sh
cd ../getCourse
/bin/bash deploy.sh
cd ../checkMondays
/bin/bash deploy.sh
