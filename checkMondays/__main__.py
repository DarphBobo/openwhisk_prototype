def main(params):
    weekday = params['weekday']
    if weekday == "Montag":
        params['weekday'] = "Dienstag"
    if weekday == "monday":
        params['weekday'] = "tuesday"
    if weekday == "Monday":
        params['weekday'] = "Tuesday"
    return params
