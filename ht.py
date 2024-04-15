from hashtable import HashTable

my_hashtable = HashTable(5)  # Create instance of hashtable with fixed sized 5
my_hashtable['mango'] = 'yellow'  # Add key-value pair to hashtable
my_hashtable['apple'] = 'red'  # Add key-value pair to hashtable
my_hashtable['banana'] = 'yellow'  # Add key-value pair to hashtable
my_hashtable['mango'] = 'orange'  # 'yellow'

my_hashtable.keys()  # ['mango', 'apple', 'banana']
my_hashtable.values()  # ['orange', 'red', 'yellow']

