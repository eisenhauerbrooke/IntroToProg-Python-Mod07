# Pickling and Error Handling
**Dev:** *BEise*  
**Date:** *11/30/2021*

## Introduction
This assignment focused on pickling and unpickling data and using error handling to help the user better understand pre-determined error messages. The script established in Assignment 7 uses picking, unpickling, and error handling to place an online grocery order. 

## Pickling 
Pickling is used in Python to serialize an object (https://www.geeksforgeeks.org/understanding-python-pickling-example/).  Deserializing an object can be done by un-pickling the dataset. Serializing a dataset is a way to convert the object into characters that can be stored persistently. When data is stored in a pickle, it takes up less room in memory because it doesn’t serialize the object each time it’s referenced in the code. Figure 1 from the online grocery order script created in this assignment show how pickling and unpickling are used to serialize and deserialize the users grocery selections. The dump() function is used to serialize the object and “wb” is a parameter that writes the data into the file as a binary. The load() function is used to convert the characters back into an object during unpickling and the “rb” parameter is used to read the binary data from the file.
  
```
@staticmethod
    def pickle(file_name, list_of_rows):
        with open(file_name, "wb") as file:
            pickle.dump(list_of_rows, file)

    @staticmethod
    def unpickle(file_name):
        with open(file_name, 'rb') as file:
            grocery_list = pickle.load(file)
        return grocery_list
```
Figure 1: Pickling and Unpickling

## Error Handling
Whenever a human interacts with your script, they will likely introduce new errors that can corrupt the code. It is best practice to use structured error handling when a human will be interacting, or inputting data into your code, to avoid unnecessary errors. Examples of error handling include limiting the type of data input as a number or letter. Figure 2 shows text from the script for this assignment that includes error handling for specific errors. If the user omits inputting an item in the cart or tries to input a number, they will get the error shown below. Additionally, if the user tries to input letters or characters in the price, they will also get an error message. 

```
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
```
Figure 2: Error Handling

These are the most common input errors the user would see when working with the code. Any other input can be deemed invalid by the code, which will output the appropriate error text in python. 

## Script
The PyCharm output of the online grocery ordering code described in previous paragraphs is shown in Figure 3. The code prompts the user to select an option. The user adds groceries and their respective prices to their cart, and the receipt is shown. 
 
 
 ![Figure 3](https://github.com/eisenhauerbrooke/IntroToProg-Python-Mod07/blob/main/Figure%203.png "Figure 3: Code in PyCharm")
 
 
Figure 4 shows the same program output in the Command Module.

 ![Figure 4](https://github.com/eisenhauerbrooke/IntroToProg-Python-Mod07/blob/main/Figure%204.png "Figure 4: Command Module")


## Summary
In summary, pickling is used in the script to serialize an object and store it as a binary character. The character can be unpickled to restore the data to an object. The code uses error handling to ensure the user inputs the appropriate items.

