import re

def normalize(s):
    return re.sub(r"\s+", " ", s.lower().strip())

def tokenize(s):
    return normalize(s).split(" ")

def align_segments_to_words(segments, word_timestamps):
    w_words = [normalize(w["word"]) for w in word_timestamps]

    out = []
    w_idx = 0
    for segment in segments:
        seg_words = tokenize(segment["word"])
        if not seg_words:
            continue

        start_time = None
        end_time = None

        for i in range(w_idx, len(w_words) - len(seg_words) + 1):
            if w_words[i:i+len(seg_words)] == seg_words:
                start_time = word_timestamps[i]["start"]
                end_time   = word_timestamps[i+len(seg_words)-1]["end"]
                w_idx = i + len(seg_words)
                break

        if start_time is None:
            continue

        out.append({"word": segment["word"].strip(), "start": round(start_time, 3), "end": round(end_time, 3)})

    return out
