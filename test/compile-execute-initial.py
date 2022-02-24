#!/usr/bin/env python3
import os
import subprocess
print('obtained from here')
subprocess.call("rm -f ./a.out", shell=True)
retcode = subprocess.call("/usr/bin/g++ uploads/walk.cc", shell=True)
if retcode:
    print("failed to compile walk.cc")
    exit
subprocess.call("rm -f ./output", shell=True)
retcode = subprocess.call("./test.sh", shell=True)
grade = "Score: " + str(retcode) + " out of 2 correct."
print (grade)
grade_line = "*************Original submission*************"
grade = grade + '\n' + grade_line
print(grade_line)
with open('uploads/walk.cc','r') as fs:
    grade_line = fs.read()
    grade = grade + '\n' + grade_line
    print(grade_line)
    
with open('graded.txt', 'wb') as fh:
    fh.write(grade)
return grade