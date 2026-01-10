def build_from_words(segments):
    timeline = []

    for segment in segments:
        if "words" not in segment:
            continue

        for word in segment:
            timeline.append({
                "word": word["word"],
                "start": word["start"],
                "end": word["end"],
                "segment_id": segment["id"]
                })
            print(timeline)

    return timeline

