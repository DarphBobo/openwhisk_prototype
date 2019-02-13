#
# This was part of a student project the Munich University of Applied Sciences.
# https://github.com/DarphBobo/openwhisk_prototype
#

# Action to filter "weekday" variatons of monday notations and transforms to tuesday.
def main(params):
    weekday = params['weekday']
    if weekday == "Montag":
        params['weekday'] = "Dienstag"
    if weekday == "monday":
        params['weekday'] = "tuesday"
    if weekday == "Monday":
        params['weekday'] = "Tuesday"
    return params
