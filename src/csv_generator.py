import json
import sys
import operator


def generate_csv(json_file, output_file):
    data = []
    with open(json_file) as f:
        for line_num, json_line in enumerate(f):
            elements = json.loads(json_line)
            csv_line = elements["key"] + "," + str(elements["duration"]) + "," + elements["text"]
            data.append(csv_line)
    with open(output_file, 'w') as f:
        for line in data:
            f.write("%s\n" % line)