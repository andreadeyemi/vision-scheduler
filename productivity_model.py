from datetime import timedelta

def find_productive_gaps(events, min_gap_minutes=90):
    # Sort by start time
    events.sort(key=lambda e: e["start"])
    deep_blocks = []

    for i in range(len(events) - 1):
        end_current = events[i]["end"]
        start_next = events[i + 1]["start"]
        gap = start_next - end_current

        if gap >= timedelta(minutes=min_gap_minutes):
            deep_blocks.append({
                "start": end_current,
                "end": start_next,
                "duration_minutes": int(gap.total_seconds() / 60)
            })

    return deep_blocks
