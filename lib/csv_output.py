import csv

def createCSV(dict):
    csv_columns = ['', 'name', 'type', 'format']
    dict_data = {}

    csv_file = "Paragraphs.csv"
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns, delimiter="|")
            writer.writeheader()
            for paragraph in dict:
                dict_data = {"":paragraph,'name': dict[paragraph]["name"], 'type': dict[paragraph]["type"], 'format': dict[paragraph]["format"]}
                writer.writerow(dict_data)
    except IOError:
        print("I/O error")