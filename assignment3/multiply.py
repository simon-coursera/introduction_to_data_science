import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line
N = 5
L = 5

def mapper(record):
    matrix = record[0]
    i = record[1]
    j = record[2]
    value = record[3]
    
    if matrix == "a":
        for k in range(1, N):
            mr.emit_intermediate("%d,%d"%(i,k), value)
    else:
        for i in range(1, L):
            mr.emit_intermediate("%d,%d"%(i,j), value)
    #mr.emit_intermediate(record[1][0:-10], record[0])

def reducer(key, values):    
    mr.emit(key)
 
# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)