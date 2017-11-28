import subprocess
import sys
import uuid

id = str(uuid.uuid4())

max_concurrent = 100
wake_up = 10 
max_requests = 1000

subprocess.call("locust --csv="+id+" --no-web -c "+str(max_concurrent)+" -r "+str(wake_up)+" -n "+str(max_requests)+" --host " + sys.argv[1], stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

with open(id+"_requests.csv", "r") as f:
    sys.stdout.write(f.read())
