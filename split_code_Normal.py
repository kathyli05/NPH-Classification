import os

import sklearn as skl
from sklearn.model_selection import train_test_split

path = "C:/Users/yongl/Desktop/code/Normal"
data = os.listdir("C:/Users/yongl/Desktop/code/Normal")

print(len(data))
x_train, x_test = train_test_split(data, test_size=0.2, random_state=15)
x_train, x_validate = train_test_split(x_train, test_size=0.2, random_state=25)
print(len(x_train))
print(len(x_validate))
print(len(x_test))

file1 = open(os.path.join(path + 'testNormal.txt'), "w")
for i in x_test:
    file1.write(str(i) + "\n")
file1.close()

file1 = open(os.path.join(path + 'trainNormal.txt'), "w")
for i in x_train:
    file1.write(str(i) + "\n")
file1.close()

file1 = open(os.path.join(path + 'validateNormal.txt'), "w")
for i in x_validate:
    file1.write(str(i) + "\n")
file1.close()