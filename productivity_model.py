from datetime import datetime, timedelta
from fake_calendar import load_sample_events


def find_open_slots(events, work_start=9, work_end=18, min_duration_minutes=60):
    """Finds available time blocks between scheduled events."""
    events = sorted(events, key=lambda e: e['start'])
    day_start = datetime.now().replace(hour=work_start, minute=0, second=0, microsecond=0)
    day_end = datetime.now().replace(hour=work_end, minute=0, second=0, microsecond=0)

    slots = []
    current_time = day_start

    for event in events:
        if event['start'] > current_time:
            gap = (event['start'] - current_time).total_seconds() / 60
            if gap >= min_duration_minutes:
                slots.append({"start": current_time, "end": event['start']})
        current_time = max(current_time, event['end'])

    if (day_end - current_time).total_seconds() / 60 >= min_duration_minutes:
        slots.append({"start": current_time, "end": day_end})

    return slots


def schedule_deep_work():
    """Prints AI-style suggested deep work sessions based on gaps."""
    events = load_sample_events()
    open_blocks = find_open_slots(events)

    if not open_blocks:
        print("⚠️ No suitable deep work slots available today.")
        return

    print("🧠 Suggested Deep Work Sessions:")
    for block in open_blocks:
        duration = (block['end'] - block['start']).seconds // 60
        print(f" • {block['start'].strftime('%I:%M %p')} – {block['end'].strftime('%I:%M %p')} ({duration} min)")


if __name__ == "__main__":
    schedule_deep_work()
