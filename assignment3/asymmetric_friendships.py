import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    mr.emit_intermediate(record[0], record[1])
    mr.emit_intermediate(record[1], record[0])

def reducer(name, friends):
    friends = sorted(friends)
    singular_names = []
    for friend in friends:
        if friend in singular_names:
            singular_names.remove(friend)
        else:
            singular_names.append(friend)
    
    for singular_name in singular_names:
        mr.emit((name, singular_name))           
 
# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
