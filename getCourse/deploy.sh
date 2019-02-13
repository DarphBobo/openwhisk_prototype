#!/bin/bash
mkdir tmp-build
cp *.py tmp-build/

# install dependencies
pip3 install dnspython couchdb -t tmp-build/

# zip
cd tmp-build
zip -r ../exec.zip ./*
cd ..

# update action
wsk action create getCourse exec.zip --kind python:3 --web true -i

# update api point
wsk api create /courses get getCourse -i

# delete artifacts
rm -rf tmp-build/ exec.zip

