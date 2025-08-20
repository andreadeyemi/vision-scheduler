from ics import Calendar
import datetime

def parse_calendar(file_path):
    with open(file_path, 'r') as f:
        calendar = Calendar(f.read())

    events = []
    for event in calendar.events:
        events.append({
            "summary": event.name,
            "start": event.begin.datetime,
            "end": event.end.datetime
        })

    return events
