import pandas as pd
import numpy as np

def dataTrimmer(fn,start,speed,payload,test):
    fn = 'data/'+ fn + '.csv' #append stuff for the filename
    df = pd.read_csv(fn) #read into pandas data frame
    array = df.to_numpy() #go from data frame to numpy
    for j in range(array.shape[0]): #iterate over rows
        for k in range(array.shape[1]): #iterate over row elements
            elem = array[j,k] #pick out element
            if isinstance(elem, str): #if the element has brackets, act on it
                elem = float(elem.translate({ord(i): None for i in '()[]'}))
                array[j,k] = elem
    numels = array.shape[0]
    zeros = np.zeros((numels, 1))  # zeros column as 2D array
    array = np.hstack((array, zeros+start,zeros+speed,zeros+payload,zeros+test))   # append column
    return array

#array of filenames for the data
filenames = np.array(['ur5testresult_coldstart_fullspeed_payload4.5lb_1',
                      'ur5testresult_coldstart_fullspeed_payload4.5lb_2',
                      'ur5testresult_coldstart_fullspeed_payload4.5lb_3',
                      'ur5testresult_coldstart_halfspeed_payload4.5lb_1',
                      'ur5testresult_coldstart_halfspeed_payload4.5lb_2',
                      'ur5testresult_coldstart_halfspeed_payload4.5lb_3',
                      'ur5testresult_fullspeed_payload1.6lb_1',
                      'ur5testresult_fullspeed_payload1.6lb_2',
                      'ur5testresult_fullspeed_payload1.6lb_3',
                      'ur5testresult_fullspeed_payload4.5lb_1',
                      'ur5testresult_fullspeed_payload4.5lb_2',
                      'ur5testresult_fullspeed_payload4.5lb_3',
                      'ur5testresult_halfspeed_payload1.6lb_1',
                      'ur5testresult_halfspeed_payload1.6lb_2',
                      'ur5testresult_halfspeed_payload1.6lb_3',
                      'ur5testresult_halfspeed_payload4.5lb_1',
                      'ur5testresult_halfspeed_payload4.5lb_2',
                      'ur5testresult_halfspeed_payload4.5lb_3'])

#array of attributes for the data
#start      ,   speed   ,   payload   ,   test
#0cold 1hot  0half 1full 0 1.6 1 4.5   1 2 3
attributes = np.array([[0,1,1,1],#coldstart full 4.5
                       [0,1,1,2],
                       [0,1,1,3],
                       [0,0,1,1],#coldstart half 4.5
                       [0,0,1,2],
                       [0,0,1,3],
                       [1,1,0,1],#hotstart full 1.6
                       [1,1,0,2],
                       [1,1,0,3],
                       [1,1,1,1],#hotstart full 4.5
                       [1,1,1,2],
                       [1,1,1,3],
                       [1,0,0,1],#hotstart half 1.6
                       [1,0,0,2],
                       [1,0,0,3],
                       [1,0,1,1],#hotstart half 4.5
                       [1,0,1,2],
                       [1,0,1,3]])

fulldataset = np.empty(shape=[0, 77]) #empty array
for filenum in range(filenames.shape[0]): #iterate over all the files
    fn = filenames[filenum] #grab the filename from array
    attr = attributes[filenum] #grab the attributes from array
    start = attr[0]
    speed = attr[1]
    payload = attr[2]
    test = attr[3]
    dataarray = dataTrimmer(fn,start,speed,payload,test) #trim data into array
    fulldataset = np.vstack((fulldataset,dataarray)) #add array to full set
    
fulldf = pd.DataFrame(fulldataset)

fulldf.to_csv("data/robotArmData.csv", header=False, index=False)


# fn = 'ur5testresult_halfspeed_payload1.6lb_1'
# #fn = fn + '.csv'
# print(fn)
# #df = pd.read_csv(fn)
# #array = df.to_numpy()
# start = 1 #1 for hot for cold
# speed = 0 #1 for full 0 for half
# payload = 0 #1 for 4.5 0 for 1.6
# test = 1 # 1 2 or 3

# narray = dataTrimmer(fn,start,speed,payload,test)

# print(narray.shape)



# for j in range(array.shape[0]):
#     for k in range(array.shape[1]):
#         elem = array[j,k]
#         #print(elem)
#         if isinstance(elem, str):
#             # print(elem)
#             elem = float(elem.translate({ord(i): None for i in '()[]'}))
#             # print(elem)
#             array[j,k] = elem
# #print(array)
# print(array.shape)
# numels = array.shape[0]
# zeros = np.zeros((numels, 1))  # zeros column as 2D array
# array = np.hstack((array, zeros+start,zeros+speed,zeros+payload,zeros+test))   # append column

#print(array.shape)




