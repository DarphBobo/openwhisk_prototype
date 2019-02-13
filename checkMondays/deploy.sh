#!/bin/bash
mkdir tmp-build
cp *.py tmp-build/

# install dependencies
pip3 install dnspython -t tmp-build/

# zip
cd tmp-build
zip -r ../exec.zip ./*
cd ..

# create action
wsk action create checkMondays exec.zip --kind python:3 --web true -i
wsk action create forgetMondays --web true --sequence checkMondays,createCourse -i

wsk api create /courses /forgetMondays post forgetMondays -i


# delete artifacts
rm -rf tmp-build/ exec.zip

