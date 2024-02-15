import argparse
import re
from lib.json_output import createJSON
from lib.csv_output import createCSV

parser = argparse.ArgumentParser()
parser.add_argument("--File", help="File or path to a file to read from", default="data.txt")
args = parser.parse_args()

dict = {}

with open(args.File) as file:
    for line in file:
        if 'End' in line:
            continue

        m = re.search('## Begin (.*)', line)
        if m:
            curentParagraph = m.group(1)
            dict[curentParagraph] = {}
        else:
            m = re.search('(.*) type=(.*) format=(.*)', line)
            if m:
                dict[curentParagraph]['name'] = m.group(1)
                dict[curentParagraph]['type'] = m.group(2)
                dict[curentParagraph]['format'] = m.group(3)

print(dict)
print("General Done")
createJSON(dict)
print("JSON Done")
createCSV(dict)
print("CSV Done")


