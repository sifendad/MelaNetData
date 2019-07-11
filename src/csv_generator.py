import json
import sys
import operator


def generate_csv(json_file, output_file):
    data = []
    with open(json_file) as f:
        for line_num, json_line in enumerate(f):
            elements = json.loads(json_line)
            csv_line = "../MelaNet/" + elements["key"] + "," + str(elements["duration"]) + "," + elements["text"]
            data.append(csv_line)
    with open(output_file, 'w') as f:
        f.write("%s\n" % "wav_filename,wav_filesize,transcript")
        for line in data:
            f.write("%s\n" % line)
            
def generate_alphabet(alphabet, output_file):
    with open(output_file, 'w') as f:
        for x in alphabet:
            f.write("%s\n" % x)
        f.write("%s\n" % " ")