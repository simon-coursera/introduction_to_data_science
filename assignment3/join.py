import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    mr.emit_intermediate(record[1], record)

def reducer(id, records):
    orders = [_order for _order in records if _order[0] == "order"]
    line_items = [_line_item for _line_item in records if _line_item[0] == "line_item"]
    
    #join_records = []
    for _order in orders:
        for _line_item in line_items:
            mr.emit(_order + _line_item)
            
    #mr.emit((join_records))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
