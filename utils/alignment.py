import re

def align_independent(segments, word_timestamps):

    out = []
    w_index = 0
    for segment in segments:
        text = segment["text"]
        s_words = re.findall("\\b[\\w']+\\b",text)
        for i in s_words:
            print(i, word_timestamps[w_index])
            print(s_words)
            if re.search(f"{s_words[0]}",word_timestamps[w_index]["text"]):
                start = word_timestamps[w_index]["start"]
            if re.search(f"{s_words[-1]}",word_timestamps[w_index]["text"]):
                end = word_timestamps[w_index]["end"]
            w_index += 1
        out.append({"text":text,"start":round(start, 3),"end":round(end, 3)})
    print(out)
    return out
