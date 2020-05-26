import json
import re
import sys
import subprocess,shlex
from subprocess import Popen, PIPE
import os


def count_whitespace(path):
  print("INSTALL THE PACKAGE {}".format(path))
  subprocess.check_call(['npm install',path], shell=True)  
  i=0
  proc = Popen(['npm','list'], stdout=PIPE, stderr=PIPE)
  stdout1, stderr1 = proc.communicate()
  #print(stdout1.decode("utf-8"))
  proc1 = Popen(['npm','list','--depth='+str(i)], stdout=PIPE, stderr=PIPE)
  stdout, stderr = proc1.communicate()
  while(stdout.decode("utf-8") != stdout1.decode("utf-8")):
    i=i+1
    proc1 = Popen(['npm','list','--depth='+str(i)], stdout=PIPE, stderr=PIPE)
    stdout, stderr = proc1.communicate()
    print(stdout.decode("utf-8"))
    print(i)
  #print(proc.decode("utf-8"))
  result={}
  result["check_id"] = "regession"
  result["path"] = path
  result["extra"] = {}
  result["extra"]["result"] = i 
  return result
  

all_results = []
all_results.append(count_whitespace(os.getcwd()))


with open("/analysis/output/output.json", "w") as output:
    output.write(json.dumps({"results": all_results}, sort_keys=True, indent=4))
