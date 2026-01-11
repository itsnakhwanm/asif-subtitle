import re

def normalize(s):
    return re.sub(r"[^a-z0-9\-]", "", s.lower())

def align_independent(segments, word_timestamps):

    out = []
    w_norm = [normalize(w["word"]) for w in word_timestamps]
    for segment in segments:
        target = normalize(segment["word"])
        best = None
        for i in range(len(word_timestamps)):
            acc = ""
            start_time = word_timestamps[i]["start"]
            for j in range(i, len(word_timestamps)):
                acc += w_norm[j]
                end_time = word_timestamps[j]["end"]
                if acc == target:
                    best = (start_time, end_time)
                    break

                if len(acc) > len(target):
                    break

            if best:
                break

        if best:
            s, e = best
        else:
            s, e = segment["start"], segment["end"]

        out.append({"word": segment["word"].strip(), "start": round(start_time, 3), "end": round(end_time, 3)})
    return out
