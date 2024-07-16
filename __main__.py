import sys
from ISLP import load_data

def HelloWorld():
  print('HelloWorld') 



def LoadAutoData(datasetname):   
    Auto = load_data(datasetname) 
    Columns = Auto.columns
    Size = Auto.shape
    What = Auto.describe().iloc[:,:4]
    print(What)
    #for column in Columns:
      #print(column)
    
       

   
if __name__ == '__main__':
    print("you passed {0}".format(sys.argv[1]))
    LoadAutoData(sys.argv[1])
