import MapReduce
import sys

"""
Implement a relational join as a MapReduce query

"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents

    mr.emit_intermediate(record[1], record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    for first in list_of_values:
      for second in list_of_values:
        if first[0] == 'order' and second[0] == 'line_item':
            mr.emit((key, first+second))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
