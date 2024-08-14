import csv

def main():
    students = read_dictionary('students.csv')
    inumber = input("Enter an I-Number: ")
    inumber = inumber.replace('-', '')

    if not inumber.isdigit():
        print("Invalid I-Number")
        return
    elif len(inumber) < 9:
        print("Invalid I-Number: too few digits")
        return
    elif len(inumber) > 9:
        print("Invalid I-Number: too many digits")
        return

    try:
        print(f"Student Name: {students[inumber]}")
    except KeyError:
        print("No such student")


def read_dictionary(filename):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.
    Parameters
      filename: the name of the CSV file to read.
    Return: a dictionary that contains
      the contents of the CSV file.
    """
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        return {rows[0]: rows[1] for rows in reader}


if __name__ == '__main__':
    main()
