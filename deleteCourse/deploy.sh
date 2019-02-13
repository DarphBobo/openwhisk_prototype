#!/bin/bash
mkdir tmp-build
cp *.py tmp-build/

# install dependencies
pip3 install dnspython couchdb -t tmp-build/

# zip
cd tmp-build
zip -r ../exec.zip ./*
cd ..

# create action
wsk action create deleteCourse exec.zip --kind python:3 --web true -i

# create api point
wsk api create /courses delete deleteCourse -i

# delete artifacts
rm -rf tmp-build/ exec.zip

