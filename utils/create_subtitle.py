from .time_utils import *
def write_srt(segments, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        for index, segment in enumerate(segments):
            f.write(str(index)+"\n")
            f.write(srt_format_timestamps(segment["start"])+" --> "+srt_format_timestamps(segment["end"])+"\n")
            f.write(segment["word"]+"\n\n")
def write_vtt(segments, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("WEBVTT\n\n")
        for index, segment in enumerate(segments):
            f.write(str(index)+"\n")
            f.write(srt_format_timestamps(segment["start"])+" --> "+srt_format_timestamps(segment["end"])+"\n")
            f.write(segment["word"]+"\n\n")
