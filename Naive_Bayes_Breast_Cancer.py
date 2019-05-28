import PreProcess_Load_Data as Data_Set
import math
import random
import statistics as sv


#Training and Testing Sample
def ProcessDataSet(dataset,splitRatio):
    TrainingSize = int(len(dataset)*splitRatio)
    TrainSet = []
    TestSet = dataset
    while len(TrainSet) < TrainingSize:
        index = random.randrange(len(TestSet))
        TrainSet.append(TestSet.pop(index))
    return [TrainSet,TestSet]

def Seperate_By_Class(dataset):
    Data_set = {}
    for vector in dataset:
        if vector[-1] not in Data_set:
            Data_set[vector[-1]] = []
        Data_set[vector[-1]].append(vector)
    return Data_set

def Class_Feature(dataset):
    List = []
    for attribute in zip(*dataset):
        mean = sv.mean(attribute)
        SD = sv.stdev(attribute)
        List.append((mean,SD))
    List.pop(-1)
    return List

def Gaussian_Distribution(x,mean,sd):
    if sd == 0.0:
        sd = 0.0001
    exponent = -1*(math.pow((x-mean),2)/(sd*sd))/2
    Y = math.sqrt(1/(2*math.pi*sd*sd))*math.pow(math.e,exponent)
    return Y
    

def Class_Mean_Deviation(dataset):
    Data_Set = {}
    for label,instance in dataset.items():
        Data_Set[label] = []
        Data_Set[label].append(Class_Feature(instance))
    return Data_Set

def predict(Summary,Vector):
    CalculateProbability = {}
    bestLabel,bestProbabilty = None,-1
    for label,instance in Summary.items():
        instance = instance[0]
        CalculateProbability[label] = 1
        for i in range(len(instance)):
            mean,sd = instance[i]
            x = Vector[i]
            CalculateProbability[label] *= Gaussian_Distribution(x,mean,sd)

    for Label,Probability in CalculateProbability.items():
        if bestLabel is None or Probability > bestProbabilty:
            bestLabel = Label
            bestProbabilty = Probability

    return bestLabel
        

            
def Prediction_test_set(Summary,test):
    Prediction = []
    for i in range(len(test)):
        Result = predict(Summary,test[i][:len(test[i])-1])
        Prediction.append(Result)
    return Prediction

        
def accuracy(Prediction,Test):
    Correct = 0
    for i in range(len(Test)):
        if Prediction[i] == Test[i][-1]:
            Correct += 1
    return (Correct/float(len(Test))) * 100
            

DataSet = Data_Set.Load_Preprocess_Data('breast-cancer.data')
Train,Test = ProcessDataSet(DataSet,0.70)
print('Spliting the data: Train Size: {0},Test Size: {1}'.format(len(Train),len(Test)))
print("\n\n")
data = Seperate_By_Class(Train)
Summary = Class_Mean_Deviation(data)
Prediction = Prediction_test_set(Summary,Test)
print(Prediction)
Accuracy = accuracy(Prediction,Test)
print("\n\n")
print('With and Accuracy of {0}'.format(Accuracy))
