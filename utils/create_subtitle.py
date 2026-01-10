from .time_utils import *
def write_srt(cues, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        for index, cue in enumerate(cues):
            f.write(str(index)+"\n")
            f.write(format_timestamps(cue["start"])+" --> "+format_timestamps(cue["end"])+"\n")
            f.write(cue["word"]+"\n\n")
