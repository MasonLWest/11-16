from collections import OrderedDict, defaultdict

# zoo.py
def hours():
    print('Open 9-5 daily')

# Call hours() function from zoo module
import zoo
zoo.hours()

# Import zoo module as menagerie and call its hours() function
import zoo as menagerie
menagerie.hours()

# Import hours() function from zoo directly and call it
from zoo import hours
hours()

# Import hours() function as info and call it
from zoo import hours as info
info()

# Make a dictionary called plain and print it
plain = {'a': 1, 'b': 2, 'c': 3}
print(plain)

# Make an OrderedDict called fancy and print it
fancy = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(fancy)

# Make a defaultdict called dict_of_lists, add a value to it, and print it
dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')
print(dict_of_lists['a'])
