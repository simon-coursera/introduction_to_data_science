import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    document_id = record[0]
    text = record[1]
    words = list(set(text.split()))
    for w in words:
        mr.emit_intermediate(w, document_id)

def reducer(word, list_of_ids):
    mr.emit((word, list_of_ids))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
