# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 13:03:40 2020

@author: AartiK
"""




import pandas as pd
from datetime import datetime
from datetime import timedelta
import requests
import time
import random


def HR_gen():    
    user = 1
    heart_rate= random.randint(60,65)
    date = datetime.today().strftime("%Y-%m-%d")
    time = datetime.now().isoformat()   
    
    return [user, heart_rate, date , time]



if __name__ == '__main__':
   # workspace: realtime workspace ,  dataset : ECG_data(Url) ,  dashboard : ECG_dashboard
   REST_API_URL= "https://api.powerbi.com/beta/707118c9-65c0-45b3-a435-33efe37cf0cc/datasets/e3b1187e-76de-4dcd-92a1-1b5e1b396e0e/rows?noSignUpCheck=1&key=TVLVxIizyrQwOZN9YP8r1TKRwLsRnxlujUjIquS452edGp4qXi9e9QeqX6ts0ICCTrQToE8ph4lHM4AKD1zfOw%3D%3D"
   while True:
        beats = []  # empty list to add continus data
        for i in range(1):   # executes only once for iteration purpose 
             beat = HR_gen()
             beats.append(beat)
             print("Current heart beat" , beats)     
    
        print("step1")
       
        #header for framing data
        HEADER = ["user", "heart_rate", "date" , "time"]
   
        data_df =  pd.DataFrame(beats ,columns = HEADER)
        data_json = bytes(data_df.to_json(orient='records'), encoding='utf-8') 
        req = requests.post(REST_API_URL, data_json)
        print("json dataset" , data_json) 
        print("Data posted in Power BI API")
        time.sleep(3)
