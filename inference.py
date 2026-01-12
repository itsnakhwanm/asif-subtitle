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
    model_size = args.model_size
    device = args.device
    filename = args.filename
    max_words = args.max_words
    output = args.output
    output_basename, output_ext = os.path.splitext(output)

    model   = whsp.load_model(model_size,device=device)
    result  = model.transcribe(filename,word_timestamps=True,verbose=True)

    words   = get_word_timestamps(result)
    texts   = get_text(result)
    if args.max_words >= 2:
        texts = split_by_word_limit(texts,max_words=max_words)
    else:
        texts = words

    out_sub = align_independent(texts, words)
    if output_ext == ".srt":
        write_srt(out_sub, output)
    elif output_ext == ".vtt":
        write_vtt(out_sub, output)
    elif output_ext == "":
        print("You must specify a file extension.")
    else:
        print("This output extension is not available yet.")


if __name__ == "__main__":
    args = parse_args()
    if args.max_words == 2:
        if warning_sign("WARNING: This will inevitably create single-word captions.\nASIF cannot condone misuse of this option.\nDo you want to continue?"):
            main(args)
    else:
        main(args)
