import pickle
import pandas as pd
import numpy as np

def swap(final_data,i,j):
    temp=0
    temp=final_data[i]
    final_data[i]=final_data[j]
    final_data[j]=temp
    return final_data

def ml_func(final_data):
    # try:
    with open('..\crop_sys1\crop_sys1\model1.pkl', 'rb') as file:
        model = pickle.load(file)
    print("Pickle File Creation successfull")
        # index=[0]
    
    final_data=swap(final_data,3,5)
    final_data=swap(final_data,4,6)
    print(final_data)

    final_data1=np.array([final_data])
    
    prediction = model.predict(final_data1)
    print(prediction)

        # if prediction==0:
        #     print("The Is Not A Malware")
        # else:
        #     print("The Is A Malware")   
    return prediction
    # except Exception as e:
    #     print("Error Loading Pickle File")
    #     return "Try Again!!"
    