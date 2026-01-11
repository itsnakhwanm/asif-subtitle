import argparse
import torch
import re
import numpy as np
import whisper as whsp
from utils import *
import os


def parse_args():
    parser = argparse.ArgumentParser(description="A tool to create readable caption for accessibility purposes.",epilog="example")
    parser.add_argument("filename", help='A media filename. Could be either video (with audio) or audio.')
    parser.add_argument("-o", "--output", type=str, required=True)
    parser.add_argument("--max-words", type=int, default=7, help="Max words.\nWarning: If you type 2, it will inevitably create single-word captions.")
    parser.add_argument("--model-size", type=str, default="small", help="Model size.")
    parser.add_argument("--device", type=str, default="cpu", help="Device used to transcribe.")
    args = parser.parse_args()
    return args

def main(args):
    model = whsp.load_model(args.model_size,device=args.device)
    result = model.transcribe(args.filename,word_timestamps=True,verbose=True)

    words=get_word_timestamps(result)
    print(words)
    texts=get_text(result)
    texts=split_by_word_limit(texts,max_words=args.max_words)
    print(texts)
    aligned=align_independent(texts,words)
    print(aligned)

    output_splitted = os.path.splitext(args.output)
    if output_splitted[1] == ".srt":
        write_srt(aligned, args.output)
    elif output_splitted[1] == ".vtt":
        write_vtt(aligned, args.output)

if __name__ == "__main__":
    args = parse_args()
    if args.max_words == 2:
        if warning_sign("Caution: This will inevitably create single-word captions.\nASIF cannot condone misuse of this option.\nDo you want to continue?"):
            main(args)
    else:
        main(args)
    #transcribe(args.filename)
