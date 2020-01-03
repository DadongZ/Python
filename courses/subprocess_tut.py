
import subprocess

p1 = subprocess.run('ls -la', shell=True)

##stdout
p1 = subprocess.run(['ls',  '-la', './log'], stdout=subprocess.PIPE)
print(p1.stdout.decode())

with open("./log/output.txt", "w") as f:
    p1 = subprocess.run(['ls',  '-la'], stdout=f)

##output as an input for another
p1 = subprocess.run(['cat', './log/output.txt'], stdout = subprocess.PIPE)
p2 = subprocess.run(['grep', 'py', './log/output.txt'], stdout = subprocess.PIPE, input=p1.stdout)

print(p2.stdout.decode())

p1 = subprocess.run('cat ./log/output.txt | grep py$', stdout = subprocess.PIPE, shell=True)
print(p1.stdout)


