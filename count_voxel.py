import nibabel as nib
import os 

FILE_PATH_NORMAL = 'C:/Users/yongl/Desktop/code/initial_Normal'
FILE_PATH_NPH = 'C:/Users/yongl/Desktop/code/initial_NPH'

normal_files = os.listdir(FILE_PATH_NORMAL)
nph_files = os.listdir(FILE_PATH_NPH)

for nf in normal_files:
    file = os.path.join(FILE_PATH_NORMAL, nf)
    nii = nib.load(file)
    mm = nii.header['pixdim'][1] * nii.header['pixdim'][2] * nii.header['pixdim'][3]
    mm = abs(mm)

    #sx, sy, sz = nii.header.get_zooms()
    #volume = sx * sy * sz
    
    img_np = nii.get_data()
    #print(img_np.shape)
    #print(file)

    ventricle_count = (img_np == 1).sum()

    #print('ventricle voxel count is {}, total ventricular vol is {} mm^3'.format(ventricle_count, ventricle_count * mm))

for nf in nph_files:
    file = os.path.join(FILE_PATH_NPH, nf)
    nii = nib.load(file)
    mm = nii.header['pixdim'][1] * nii.header['pixdim'][2] * nii.header['pixdim'][3]
    mm = abs(mm)

    #sx, sy, sz = nii.header.get_zooms()
    #volume = sx * sy * sz

    img_np = nii.get_data()
    #print(img_np.shape)
    print(file)

    ventricle_count = (img_np == 1).sum()

    print('ventricle voxel count is {}, total ventricular vol is {} mm^3'.format(ventricle_count, ventricle_count * mm))

    f = open('./NPHresults.txt', 'a')
    f.write(str(ventricle_count * mm) + '\n')
    f.close()

#three columns in sheet - subject/scan name, voxel count (ventricle count variable), voxel count multiplied by mm - ventricular volume