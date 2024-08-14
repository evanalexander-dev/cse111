# I added line 50 to ask the customer to fill out a survey.

import csv
from datetime import datetime

def main():
    current_time = datetime.now()
    print("Inkom Emporium")

    try:
        products_dict = read_dictionary('products.csv', 0)

        num_of_items = 0
        subtotal = 0
        with open('request.csv', 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                item = products_dict[row[0]]
                num_of_items += int(row[1])
                subtotal += int(row[1]) * float(item[2])
                print(f"{item[1]}: {row[1]} @ {item[2]}")
    except FileNotFoundError as file_error:
        print("Error: missing file")
        print(file_error)
        return

    except PermissionError as permission_error:
        print("Error: permission denied")
        print(permission_error)
        return

    except KeyError as key_error:
        print("Error: unknown product ID in the request.csv file")
        print(key_error)
        return

    print(f"Number of Items: {num_of_items}")
    print(f"Subtotal: {subtotal:.2f}")

    sales_tax = subtotal * 0.06
    print(f"Sales Tax: {sales_tax:.2f}")

    total = subtotal + sales_tax
    print(f"Total: {total:.2f}")

    print("Thank you for shopping at Inkom Emporium.")
    print(f"{current_time:%a %b %d %H:%M:%S %Y}")
    print()
    print("Tell us how we did! https://notalink.toclickon/survey")

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
          dictionary and return the dictionary.
          Parameters
              filename: the name of the CSV file to read.
              key_column_index: the index of the column
                  to use as the keys in the dictionary.
          Return: a compound dictionary that contains
              the contents of the CSV file.
            """
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        dictionary = {}
        for row in reader:
            key = row[key_column_index]
            dictionary[key] = row
    return dictionary


if __name__ == '__main__':
    main()
