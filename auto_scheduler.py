from ics import Calendar, Event
from productivity_model import find_productive_gaps
from datetime import datetime
import uuid

def generate_deep_work_ics(events, output_path="deep_work.ics"):
    # Find available blocks
    gaps = find_productive_gaps(events)

    c = Calendar()
    for block in gaps:
        e = Event()
        e.name = "🔒 Deep Work: Strategic Focus"
        e.begin = block["start"]
        e.end = block["end"]
        e.uid = str(uuid.uuid4())
        e.description = f"Auto-scheduled based on calendar analysis ({block['duration_minutes']} min)"
        c.events.add(e)

    with open(output_path, "w") as f:
        f.writelines(c)
    print(f"✅ Saved: {output_path}")
