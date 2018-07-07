from dal.JobDal import JobDal
from util.AppUtil import AppUtil
from .HttpService import HttpService
import time


class JobService:

    def __init__(self):
        self.jobDal = JobDal()

    def handle_job(self, file_params):
        file_path = AppUtil.create_file(file_params["file_stream"],file_params["file_id"] + file_params["file_name"])

        # This sleep is just to simulate a call
        time.sleep(5)

        payload = {
            "status":"processed",
            "result":'{"Algo1":"50","Algo2":"100"}',
            "localFilePath" : file_path
        }

        # Post result to firebase
        HttpService.send_request("https://outlaystore.firebaseio.com/files/" + file_params["file_id"] + "/.json", http_method='PATCH', params="params", payload=payload)
