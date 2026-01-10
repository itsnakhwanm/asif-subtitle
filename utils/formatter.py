def get_word_timestamps(transcription):
    out = []
    segments = transcription["segments"]
    for segment in segments:
        for word_index in segment["words"]:
            word=word_index["word"]
            start=float(word_index["start"])
            end=float(word_index["end"])
            out.append({"word": word, "start":round(start,3), "end":round(end,3)})
    return out

def get_text(transcription):
    out = []
    segments = transcription["segments"]
    for segment in segments:
        start=float(segment["start"])
        end=float(segment["end"])
        word=segment["text"]
        out.append({"word":word,"start":round(start,3), "end":round(end,3)})
    return out


def split_by_word_limit(segments, max_words=5):
    out = []
    for segment in segments:
        words = segment["word"].split()
        start = segment["start"]
        end   = segment["end"]

        if not words:
            continue

        if len(words) == 1:
            out.append({"word": words[0], "start": round(start, 3), "end": round(end, 3)})
            continue

        total_words = len(words)
        duration = end - start
        step = duration / total_words

        chunks = []
        for i in range(0, total_words, max_words):
            chunks.append(words[i:i+max_words])

        if len(chunks) > 1 and len(chunks[-1]) == 1:
            last_word = chunks[-1][0]
            prev_chunk = chunks[-2]

            moved_word = prev_chunk.pop()
            chunks[-1] = [moved_word, last_word]
        word_index = 0
        for chunk in chunks:
            chunk_start = start + word_index * step
            chunk_end   = start + (word_index + len(chunk)) * step
            out.append({"word": " ".join(chunk), "start":round(chunk_start,3), "end":round(chunk_end,3)})
            word_index += len(chunk)
    return out
