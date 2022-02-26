#!/usr/bin/env python3
import os
import subprocess
def grade():
    print('obtained from here')
    subprocess.call("rm -f ./a.out", shell=True)
    retcode = subprocess.call("/usr/bin/g++ uploads/walk.cc", shell=True)
    if retcode:
        compile = False
        print("failed to compile walk.cc")
        grade = "Score: 0. Failed to compile."
        #exit, not sure how this was supposed to work
        return grade 
    else:
        compile = True
    subprocess.call("rm -f ./output", shell=True)
    retcode = subprocess.call("./test.sh", shell=True)
    if not compile:
        grade = "Score: " + str(retcode) + " out of 2 correct."
    else:
        grade = "Score: " + str(retcode) + " out of 2 correct."
    
    grade_output = "*************Original submission*************"
    grade = grade + '\n' + grade_output
    with open('uploads/walk.cc','r') as fs:
        grade_output = fs.read()
        grade = grade + '\n' + grade_output
    
    return grade