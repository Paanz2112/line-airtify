import requests
import logging
from datetime import datetime
import pytz
from os import environ as env
from dotenv import load_dotenv
load_dotenv()

thaitz = pytz.timezone('Asia/Bangkok')
url = env['NOTIFY_URL']

def line_notify (**kwargs):
    print(url+m)
    m = f"""\n Airflow Dag Status Notification 
        From Baby vm \n
        Dag => {kwargs["dag_id"]} 
        Task id => {kwargs["task_id"]}
        Job id => {kwargs["job_id_"]} 
        Execution Day => {thaitz.localize(kwargs["exec_date"].strftime('%Y-%m-%d'))} 
        Exceution Time => {thaitz.localize(kwargs["exec_date"].strftime('%H:%M:%S'))}
        End Execution Day => {thaitz.localize((kwargs["end_date"]).strftime('%Y-%m-%d'))} 
        End Execution Time => {thaitz.localize((kwargs["end_date"]).strftime('%H:%M:%S'))} 
        Dag duration => {kwargs["dag_duration"]} second
        Dag status => {kwargs["dag_state"]}"""

    if kwargs["dag_state"] == "success":
        params = {"message": m,"stickerPackageId":446,"stickerId":1989}
    elif kwargs["dag_state"] == "success":
        params = {"message": m,"stickerPackageId":446,"stickerId":2000}
    elif kwargs["dag_state"] == "failed":
        params = {"message": m,"stickerPackageId":446,"stickerId":2008}
    
    x = requests.post(url, params=params,headers={"Content-Type":"application/x-www-form-urlencoded","Authorization":f"""Bearer {env['NOTIFY_TOKEN']}"""})
    print("Alert messess status: ",x)


# line_notify()