# -------------------------------------------------- #
# Title: Assignment07
# Description: This script uses a menu to show pickling and structured errors.
# ChangeLog (Who,When,What):
# BEise, 11/28/2021, Created Script
# BEise, 11/30/2021, Modified Script
# -------------------------------------------------- #

import pickle

# Variable Declarations #
str_file_name = 'Grocery_list.dat'
str_item = ''
flt_price = 0
str_choice = ''
lst_table = []


# Processing #
class process_data:
    @staticmethod
    def add_data_to_list(item, price, list_of_rows):
        if item != '' and price != 0:
            row = {"Item": item, "Price": price}
            list_of_rows.append(row)
        return list_of_rows

    @staticmethod
    def total_items(list_of_rows):
        num_of_items = len(list_of_rows)
        return num_of_items

    @staticmethod
    def price_sum(list_of_rows):
        price_sum = "0"
        # print(list_of_rows)  # testing table of dictionary rows
        for row in list_of_rows:
            price_sum += row["Price"]
        return price_sum

    @staticmethod
    def pickle(file_name, list_of_rows):
        with open(file_name, "wb") as file:
            pickle.dump(list_of_rows, file)

    @staticmethod
    def unpickle(file_name):
        with open(file_name, 'rb') as file:
            grocery_list = pickle.load(file)
        return grocery_list

# Presentation #
class IO:
    @staticmethod
    def print_menu_options():
        print('''
          Online Grocery Ordering Options
          0 - Add a grocery item and its price to cart
          1 - Calculate cart total
          2 - Save cart
          3 - Retrieve previously saved cart 
          4 - Exit program
          ''')


    @staticmethod
    def input_menu_choice():
        choice = input("Select an option: ").strip()
        return choice

    @staticmethod
    def input_press_to_continue(optional_message=""):
        print(optional_message)
        input('Press the [Enter] key to continue.')


    @staticmethod
    def input_grocery_list_items(item="", price=0):
        try:
            item = input("Add an item to your cart: ").lower()
            if len(item) == 0:
                raise Exception("Item cannot be blank.")
            elif item.isnumeric():
                raise Exception("Item cannot contain numbers.")
            price = input("Enter price: ")
        except ValueError as e:
            print("Price cannot contain letters or characters.")
        except Exception as e:
            print("Error.")
            print(e)
        return item, price


    @staticmethod
    def print_current_items_in_list(list_of_rows):
        print("Receipt: ")
        for row in list_of_rows:
            print(str(row['Item']) + "," + str(row['Price']))

    @staticmethod
    def input_yes_no_choice(message):
        return input(message).strip().lower()


# Main Body of Script #
while True:
    IO.print_current_items_in_list(list_of_rows = lst_table)
    IO.print_menu_options()
    str_choice = IO.input_menu_choice()

    if str_choice == "0":
        str_item, flt_price = IO.input_grocery_list_items()
        process_data.add_data_to_list(item=str_item, price =flt_price, list_of_rows=lst_table)
        str_choice = IO.input_yes_no_choice("Add more items? [y/n] ")
        while str_choice.lower() == "y":
            str_choice, flt_price = IO.input_grocery_list_items()
            process_data.add_data_to_list(item=str_item, price=flt_price, list_of_rows=lst_table)
            str_choice = IO.input_yes_no_choice("Add more items? [y/n] ")
        else:
            continue

    elif str_choice == "1":
        print("Total number of items: ", process_data.total_items(list_of_rows=lst_table))
        print("Total price: ", process_data.price_sum(list_of_rows=lst_table))

    elif str_choice == "2":
        IO.input_press_to_continue("Saving receipt.")
        process_data.pickle(file_name=str_file_name, list_of_rows=lst_table)
        IO.input_press_to_continue('Receipt saved.')

    elif  str_choice == "3":
        IO.input_press_to_continue("Obtaining receipt.")
        lst_table = process_data.unpickle(file_name=str_file_name)

    elif str_choice == "4":  # Exits Program
        break

    else:
        IO.input_press_to_continue('Invalid option. Select 0-4.')