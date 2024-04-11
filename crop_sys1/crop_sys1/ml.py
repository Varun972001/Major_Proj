import pickle
import pandas as pd

def ml_func(data):
    with open('..\crop_sys1\crop_sys1\model.pkl', 'rb') as file:
        model1 = pickle.load(file)
    print("Pickle File Creation successfull")
        # index=[0]
        # data1=pd.DataFrame(data,index=index)

        # prediction = model1.predict(data1)
        # print(prediction)

        # if prediction==0:
        #     print("The Is Not A Malware")
        # else:
        #     print("The Is A Malware")   
    return data