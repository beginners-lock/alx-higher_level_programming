#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element by element.
    args:
        my_list_1 (list) - The first list.
        my_list_2 (list) - The second list.
        list_length (int) - The number of elements to divide.
    returns:
       a new list of length list_length containing all the divisions.
    """
    new_list = []
    for index in range(0, list_length):
        try:
            div = my_list_1[index] / my_list_2[index]
        except TypeError:
            print("DataType Error")
            div = 0
        except ZeroDivisionError:
            print("Zero Divison Error")
            div = 0
        except IndexError:
            print("Invalid Index")
            div = 0
        finally:
            new_list.append(div)
    return (new_list)
