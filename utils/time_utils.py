def format_timestamps(time_seconds):
    hours = int(time_seconds // 3600)
    minutes = int((time_seconds // 60) % 60)
    seconds = int(time_seconds % 60)
    milliseconds = round((time_seconds * 1000) % 1000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"
