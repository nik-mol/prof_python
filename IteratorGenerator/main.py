# ===============================ITERATOR===============================
from collections.abc import Iterable

# ---------basic_homework--------------
class FlatIteratorBasic:
    def __init__(self, nested_list):
        self.start = 0
       
    def get_flat_list(self, nested_list):
        flat_list = []
        for list in nested_list:
            flat_list += list
        return flat_list

    def __iter__(self):
        return (self)

    def __next__(self):
        flat_list = self.get_flat_list(nested_list)
        if self.start < len(flat_list):
            letter = flat_list[self.start]
            self.start += 1
            return letter
        else:
            raise StopIteration

# ---------additional_homework--------------
class FlatIteratorAdditional:
    def __init__(self, nested_list):
        self.nested_list = nested_list

    def __iter__(self):
        return (self)

    def __next__(self):
        for item in self.nested_list:
            if isinstance(item, str) or (not isinstance(item, Iterable)):
                return item
            else:
                self.FlatIteratorAdditional(item)

# ===============================GENERATOR===============================

# ---------basic_homework---------------
def FlatGeneratorBasic(nested_list):
    return (letter for list in nested_list for letter in list)
    # for list in nested_list:
    #   for letter in list:
    #     yield letter


# ---------additional_homework---------------
def FlatGeneratorAdditional(nested_list):
    chack_list = lambda x: (isinstance(x, str)) or (not isinstance(
        x, Iterable))
    for list in nested_list:
        if chack_list(list):
            yield list
        else:
            yield from FlatGeneratorAdditional(list)


nested_list = [
    ['a', 'b', 'c', ['Hello', 8]],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

if __name__ == '__main__':

    for item in FlatIteratorBasic(nested_list):
        print(item)
    flat_list = [item for item in FlatIteratorBasic(nested_list)]
    print(flat_list)

    for item in FlatGeneratorAdditional(nested_list):
        print(item)
    flat_list = [item for item in FlatGeneratorAdditional(nested_list)]
    print(flat_list)

    for item in FlatGeneratorBasic(nested_list):
        print(item)
    flat_list = [item for item in FlatGeneratorBasic(nested_list)]
    print(flat_list)

    for item in FlatGeneratorAdditional(nested_list):
        print(item)
    flat_list = [item for item in FlatGeneratorAdditional(nested_list)]
    print(flat_list)