import csv


def parsing_csv(path_to_file):

    with open(path_to_file, newline='') as csvfile:
        data_reader = csv.DictReader(csvfile)
        parsed_data = []
        try:
            for row in data_reader:
                parsed_data.append({"first_name": row['First Name'],
                                "last_name": row['Last Name'],
                                "email_adress": row['Email Address']})
        except csv.Error:
            pass

        return parsed_data
