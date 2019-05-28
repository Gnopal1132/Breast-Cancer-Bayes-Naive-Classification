'''
Data Set information:
1. Class: no-recurrence-events = 0, recurrence-events = 1
   2. age: 10-19, 20-29, 30-39, 40-49, 50-59, 60-69, 70-79, 80-89, 90-99.
   3. menopause: lt40 = 0, ge40 = 1, premeno = 2.
   4. tumor-size: 0-4, 5-9, 10-14, 15-19, 20-24, 25-29, 30-34, 35-39, 40-44,
                  45-49, 50-54, 55-59.
   5. inv-nodes: 0-2, 3-5, 6-8, 9-11, 12-14, 15-17, 18-20, 21-23, 24-26,
                 27-29, 30-32, 33-35, 36-39.
   6. node-caps: yes = 1, no = 0.
   7. deg-malig: 1, 2, 3.
   8. breast: left = 0, right = 1.
   9. breast-quad: left-up = 0, left-low = 1, right-up = 2, right-low = 3, central = 4.
  10. irradiat:	yes = 1, no = 0.

These are the Conventions that will be used
'''
import csv

def mean(Input):
    Sum = 0
    Input = Input.split('-')
    for i in range(int(Input[0]),int(Input[1])+1):
        Sum += i
    return (Sum/float(int(Input[1]) - int(Input[0])))
    
def Load_Preprocess_Data(filename):
    #Loading the CSV File
    DataSet = []
    with open(filename) as csvfile:
        readCSV = csv.reader(csvfile,delimiter = ',')
        for row in readCSV:
            DataSet.append(row)

    for Element in DataSet:
        if Element[0] == 'no-recurrence-events':
            Element[0] = 0
        else:
            Element[0] = 1
            
        if Element[2] == 'lt40':
            Element[2] = 0
        elif Element[2] == 'ge40':
            Element[2] = 1
        else:
            Element[2] = 2

        if Element[5] == 'yes':
            Element[5] = 1
        else:
            Element[5] = 0

        if Element[7] == 'left':
            Element[7] = 0
        else:
            Element[7] = 1

        if Element[8] == 'left-up':
            Element[8] = 0
        elif Element[8] == 'left-low':
            Element[8] = 1
        elif Element[8] == 'right-up':
            Element[8] = 2
        elif Element[8] == 'right-low':
            Element[8] = 3
        else:
            Element[8] = 4

        if Element[9] == 'yes':
            Element[9] = 1
        else:
            Element[9] = 0
        
        Element[1] = mean(Element[1])
        Element[3] = mean(Element[3])
        Element[4] = mean(Element[4])
        Element[6] = int(Element[6])
    
    return DataSet

if __name__ == '__main__':
    #To check execute it
    print(Load_Preprocess_Data('breast-cancer.data'))
   
    
