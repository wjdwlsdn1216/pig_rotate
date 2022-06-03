import cv2
import re
import os
import json
import math

def remove_path(json_file):
    fix_path = re.sub('/DL_data_big/EdgeFarm_pig/Tracking/autolabel_rootpath/room2_act2','.',json_file)
    return fix_path

def load_json(json_path):
    with open(json_path,'r') as json_file:
        file = json.load(json_file)    
    return file
        
def put_ellipse_image(json_path):
    json_file = load_json(json_path)
    img_path = remove_path(json_file[0]['file_path'])
    img = cv2.imread(img_path)
    for i in range(len(json_file)):
        cx = json_file[i]['cx']
        cy = json_file[i]['cy']
        width = json_file[i]['width']
        height = json_file[i]['height']
        radian = json_file[i]['radian']
        
        img = cv2.ellipse(img,(int(cx),int(cy)),(int(width/2),int(height/2)),radian*(180/math.pi),0,360,(255,0,0))
    return img
    

if __name__ == "__main__":
    path = './label_confirm'  
    json_list = os.listdir(path)

    for file in json_list:
        json_path = os.path.join(path,file)
        img = put_ellipse_image(json_path)
        num = re.sub(r'[^0-9]','',json_path)
        print(num)
        cv2.imwrite('./save_image/' + str(num).zfill(5) + '.jpg',img)
    

