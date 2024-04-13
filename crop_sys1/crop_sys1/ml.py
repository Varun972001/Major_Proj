import pickle
import pandas as pd

def ml_func(final_data):
    try:
        with open('..\crop_sys1\crop_sys1\model.pkl', 'rb') as file:
            model1 = pickle.load(file)
        print("Pickle File Creation successfull")
        # index=[0]

        # prediction = model1.predict(final_data)
        # print(prediction)

        # if prediction==0:
        #     print("The Is Not A Malware")
        # else:
        #     print("The Is A Malware")   
        return final_data
    except Exception as e:
        print("Error Loading Pickle File")
        return "Try Again!!"
    