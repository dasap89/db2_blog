# Example:
# list = [
#     ("Tom", "19", "167", "54"), 
#     ("Jony", "24", "180", "69"),
#     ("Json", "21", "185", "75") 
#     ("John", "27", "190", "87"), 
#     ("Jony", "24", "191", "98"), 
#     ]

# Result:
# [
#     ("John", "27", "190", "87"),
#     ("Jony", "24", "191", "98"),
#     ("Jony", "24", "180", "69"),
#     ("Json", "21", "185", "75"),
#     ("Tom", "19", "167", "54"),
# ]
from operator import itemgetter

def handle_list_of_tuples(input_list):

    return sorted(input_list, key=lambda tup: (tup[0], tup[1], tup[2], tup[3]))

input_list = [
    ("Tom", "19", "167", "54"), 
    ("Jony", "24", "180", "69"),
    ("Json", "21", "185", "75"),
    ("John", "27", "190", "87"), 
    ("Jony", "24", "191", "98"), 
]


if __name__ == '__main__':
    for row in handle_list_of_tuples(input_list):
        print(row)
