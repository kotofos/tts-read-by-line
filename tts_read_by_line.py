import argparse
import os
import pathlib
from gtts import gTTS

def main():
    parser = argparse.ArgumentParser(description='Lyrics TTS converter')
    parser.add_argument('input', help='input file')
    parser.add_argument('-o', '--out', help='output dir')
    parser.add_argument('-l', '--lang', required=True, help='language')
    args = parser.parse_args()

    input_file = args.input
    output_dir = args.out
    lang = args.lang
    if output_dir is None:
        output_dir = pathlib.Path(input_file).name + '_out'

    with open(input_file, encoding='utf-8') as f:
        input_text = f.read()

    lines = input_text.split('\n')
    lines = [l for l in lines if l != '']

    os.makedirs(output_dir, exist_ok=True)
    for i, l in enumerate(lines):
        tts = gTTS(text=l, lang=lang)
        tts.save(os.path.join(output_dir, '{:03} {}.mp3'.format(i, l)))

if __name__ == '__main__':
    main()
