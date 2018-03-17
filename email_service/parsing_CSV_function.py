import csv


def parsing_csv(path_to_file):
    with open(path_to_file, newline='') as csvfile:
        data_reader = csv.DictReader(csvfile)
        for row in data_reader:
            return ({"first_name": row['First Name'], "last_name": row['Last Name'], "email_adress": row["Email Address"]})