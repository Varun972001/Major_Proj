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
    with open('..\crop_sys1\crop_sys1\model1.pkl', 'rb') as file:
        model = pickle.load(file)
    print("Pickle File Creation successfull")
    
    final_data=swap(final_data,3,5)
    final_data=swap(final_data,4,6)
    print(final_data)

    final_data1=np.array([final_data])
    
    prediction = model.predict(final_data1)
    print(prediction)

    if prediction == 0:
        return "apple"
    elif prediction == 1:
        return "banana"
    elif prediction == 2:
        return "blackgram"
    elif prediction == 3:
        return "chickpea"
    elif prediction == 4:
        return "coconut"
    elif prediction == 5:
        return "coffee"
    elif prediction == 6:
        return "cotton"
    elif prediction == 7:
        return "grapes"
    elif prediction == 8:
        return "jute"
    elif prediction == 9:
        return "kidneybeans"
    elif prediction == 10:
        return "lentil"
    elif prediction == 11:
        return "maize"
    elif prediction == 12:
        return "mango"
    elif prediction == 13:
        return "mothbeans"
    elif prediction == 14:
        return "mungbean"
    elif prediction == 15:
        return "muskmelon"
    elif prediction == 16:
        return "orange"
    elif prediction == 17:
        return "papaya"
    elif prediction == 18:
        return "pigeonpeas"
    elif prediction == 19:
        return "pomegranate"
    elif prediction == 20:
        return "rice"
    elif prediction == 21:
        return "watermelon"
    
    return prediction
    
    
    