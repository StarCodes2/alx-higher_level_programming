#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """divides element by element 2 lists."""
    result =[]
    for i in range(list_length):
        try:
            div = float(my_list_1[i]) / float(my_list_2[i])
        except IndexError:
            div = 0
            print("out of range")
        except ZeroDivisionError:
            div = 0
            print("division by 0")
        except (ValueError, TypeError):
            div = 0
            print("wrong type")
        finally:
            result.append(div)

    return result
