from datetime import datetime, timedelta

def load_sample_events():
    base_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    
    return [
        {"title": "Team Standup", "start": base_date + timedelta(hours=9), "end": base_date + timedelta(hours=9, minutes=30)},
        {"title": "1:1 with Manager", "start": base_date + timedelta(hours=11), "end": base_date + timedelta(hours=11, minutes=30)},
        {"title": "Lunch", "start": base_date + timedelta(hours=12), "end": base_date + timedelta(hours=13)},
        {"title": "Project Sync", "start": base_date + timedelta(hours=15), "end": base_date + timedelta(hours=16)},
        {"title": "End of Day Review", "start": base_date + timedelta(hours=17), "end": base_date + timedelta(hours=17, minutes=30)},
    ]
