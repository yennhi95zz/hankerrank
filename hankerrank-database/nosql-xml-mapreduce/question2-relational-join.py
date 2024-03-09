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
            print(item)

mapReducer = MapReduce()

def mapper(record):
    # Split the record into its components
    record_parts = record.strip().split(',')
    
    # Check if the record is from the Employee table or Department table
    if record_parts[0] == 'Employee':
        # Emit SSN as key and (Employee_Name, 'E') as value
        mapReducer.emitIntermediate(record_parts[2], (record_parts[1], 'E'))
    elif record_parts[0] == 'Department':
        # Emit SSN as key and (Department_Name, 'D') as value
        mapReducer.emitIntermediate(record_parts[1], (record_parts[2], 'D'))

def reducer(key, list_of_values):
    # Initialize lists for employees and departments
    employees = []
    departments = []
    
    # Separate the values into employees and departments based on their type ('E' or 'D')
    for value in list_of_values:
        if value[1] == 'E':
            employees.append(value[0])
        elif value[1] == 'D':
            departments.append(value[0])
    
    # Generate the cartesian product of employees and departments
    for employee in employees:
        for department in departments:
            # Emit the joined record
            mapReducer.emit((key, employee, department))

if __name__ == '__main__':
    inputData = []
    for line in sys.stdin:
        inputData.append(line)
    mapReducer.execute(inputData, mapper, reducer)
