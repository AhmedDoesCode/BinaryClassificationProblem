#b	2308.0	0.00115	u	g	i	v	35	t	t	9	f	g	56.0	742	560000.0	t	0	
import pandas as pd
import numpy as np
from sklearn import preprocessing
import pickle
import joblib
import sys


class Predict():
    def predict(data_list):
        
        all_keys = ["variable1", "variable2", "variable3", "variable4", "variable5","variable6","variable7","variable8", "variable9", "variable10", "variable11", "variable12", "variable13", "variable14","variable15", "variable17", "variable18", "variable19"]
        
        
        print(len(data_list))
        print(len(all_keys))
        
        data = {all_keys[x]:data_list[x] for x in range(len(data_list))}
        
        label_indexes = [0,3,4,5,6,8,9,11,12,16]


        
        label_keys = ["variable1", "variable4", "variable5", "variable6", "variable7","variable9","variable10","variable12", "variable13", "variable18"]
        
        for key in all_keys:
            if key not in label_keys:
                data[key] = float(data[key])

        #load encoder

        encoder = preprocessing.LabelEncoder()
        encoder.classes_ = np.load('classes.npy', allow_pickle=True)

        
        for key in label_keys:
            data[key] = encoder.transform([data[key]])

        #load normalizer
        scaler = joblib.load("scaler.save")

        input_list = []
        for key in all_keys:
            input_list.append(data[key])

        input_list.append(0)
        input_list = np.array(input_list)
        input_list = scaler.transform([input_list])

        loaded_model = pickle.load(open("finalized_model.sav", 'rb'))

        input_list = input_list[0][:-2]
        result = loaded_model.predict([input_list])
        
        if result == [1.]:
            print("Yes")
            return "yes"
        else:
            print("No")
            return "no"
        #predict





#input = ["b",3017.0,0.00065,"u","g","cc","v",3125,"t","t",8,"f","g",330.0,1200,3300000.0,"t",0]
#Predict.predict(input)


'''
if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("usage: python predict.py [list,of,features]")
        sys.exit(1)
    print(sys.argv[1])
    input = sys.argv[1]
    Predict.predict(eval(input))
'''
'''
input = {
        "variable1": "b",
        "variable2": 3017.0,
        "variable3": 0.00065,
        "variable4": "u",
        "variable5": "g",
        "variable6": "cc",
        "variable7": "v",
        "variable8": 3125,
        "variable9": "t",
        "variable10": "t",
        "variable11": 8,
        "variable12": "f",
        "variable13": "g",
        "variable14": 330.0,
        "variable15": 1200,
        "variable17": 3300000.0,
        "variable18": "t",
        "variable19": 0
        }

Predict.predict(input)
'''