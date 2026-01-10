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
    parser.add_argument("--max-words", type=int, default=7, help="Max words")
    parser.add_argument("--max-lines", type=int, default=2)
    parser.add_argument("--model-size", type=str, default="small", help="Model size.")
    parser.add_argument("--device", type=str, default="cpu", help="Device used to render.")
    args = parser.parse_args()
    return args
    print(args.filename)

def main(args):
    model = whsp.load_model(args.model_size,device=args.device)
    result = model.transcribe(args.filename,word_timestamps=True,verbose=True)

    words=get_word_timestamps(result)
    texts=get_text(result)
    texts=split_by_word_limit(texts)
    aligned=align_segments_to_words(texts,words)

    write_srt(text, args.output)

if __name__ == "__main__":
    args = parse_args()
    if args.max_words == 2 and args.max_lines == 1:
        if warning_sign("Caution: This will inevitably create single-word captions.\nASIF cannot condone misuse of this option.\nDo you want to continue?"):
            main(args)
    else:
        main(args)
    #transcribe(args.filename)
