import csv


def parsing_csv(path_to_file):

    with open(path_to_file, newline='') as csvfile:
        data_reader = csv.reader(csvfile)
        parsed_data = []
        for row in data_reader:
            parsed_data.append({"first_name": row[0],
                                "last_name": row[1],
                                "email_adress": row[2]})
        return parsed_data
