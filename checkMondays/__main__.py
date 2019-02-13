import couchdb
import json

from couchdb import Server

couchserver = Server("http://172.18.0.12:5984")

dbname = "room"
if dbname in couchserver:
    db = couchserver[dbname]
else:
    db = couchserver.create(dbname)

def main(params):
    weekday = params['weekday']
    if weekday == "Montag":
        params['weekday'] = "Dienstag"
    if weekday == "monday":
        params['weekday'] = "tuesday"
    return params
