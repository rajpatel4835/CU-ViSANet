import glob
import cv2
 
# get the path/directory
folder_dir = 'data/DIV2K/DIV2K_LR_bicx2/'
new='data/DIV2K/DIV2K_LR/'
# iterate over files in
# that directory
for images in glob.iglob(f'{folder_dir}/*'):
   a=cv2.imread(images)
   new_path=new+images[-10:-6]+'.png'
   cv2.imwrite(new_path,a)