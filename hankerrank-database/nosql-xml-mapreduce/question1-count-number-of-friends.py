import sys
from collections import OrderedDict

class MapReduce:
    def __init__(self):
        self.intermediate = OrderedDict()
        self.result = []
   

    def emitIntermediate(self, key, value):
        self.intermediate.setdefault(key, [])       
        self.intermediate[key].append(value)

    def emit(self, value):
        self.result.append(value) 

    def execute(self, data, mapper, reducer):
        for record in data:
            mapper(record)

        for key in self.intermediate:
            reducer(key, self.intermediate[key])

        self.result.sort()
        for item in self.result:
            print("{\"key\":\"" + item[0] + "\",\"value\":\"" + str(item[1]) + "\"}")

mapReducer = MapReduce()

def mapper(record):
    #Start writing the Map code here
    friends = record.split()
    mapReducer.emitIntermediate(friends[0], 1)
    mapReducer.emitIntermediate(friends[1], 1)
    
def reducer(key, list_of_values):
    #Start writing the Reduce code here
    total_friends = sum(list_of_values)
    mapReducer.emit((key, total_friends))
    
if __name__ == '__main__':
  inputData = []
  for line in sys.stdin:
   inputData.append(line)
  mapReducer.execute(inputData, mapper, reducer)