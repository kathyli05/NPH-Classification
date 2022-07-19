import os 
import sklearn as skl
import nibabel as nib
from matplotlib import pyplot as plt

path = "C:/Users/yongl/Desktop/code/rmp"

for x in ["train", "test", "validate"]:
    with open(f"rmp{x}NPH.txt") as f:
        file_content = f.readlines() 
        for f1 in file_content:
            data_path = path + "/" + f1.strip()
            img = nib.load(data_path) 
            data = img.get_fdata()
            print(data.shape)
            to_plot = data[0, -185, :]
        plt.imshow(to_plot)
        plt.axis('off')
        plt.show()
