import cv2
import os
from tqdm import tqdm

def draw_box(img,box):
    x1,y1,w,h = box

    cv2.rectangle(img,(int(x1),int(y1)),(int(x1+w),int(y1+h)),(255,255,0),2)
    return img


def load_output(txt_file,format='png'):
    output={}
    fp=open(txt_file,'r')
    data=fp.readlines()

    # for i in range(0,len(data),2):
    i=0
    for i in range(len(data)):
        if format in data[i]:
            continue
        label=data[i].rstrip().split(',')

        file_name = data[i-1].rstrip().split(',')[0]
        if format not in file_name:
            continue

        file_name=file_name.split('/')[-1]
        # print(file_name)
        label[0]=int(label[0])
        label[1]=float(label[1])
        label[2]=int(label[2])
        label[3]=int(label[3])
        label[4]=int(label[4])
        label[5]=int(label[5])
        output[file_name] = label

    return output
        


    
def process(data_dir,file_name,label,save_path):
    color1=(255,255,0)
    color0=(255,0,0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img=cv2.imread(os.path.join(data_dir,file_name))
    clc=label[0]
    conf=label[1]
    box=label[2:]
    x1,y1,w,h = box

    if clc:
        cv2.rectangle(img,(int(x1),int(y1)),(int(x1+w),int(y1+h)),color1,2)
    else:
        cv2.rectangle(img,(int(x1),int(y1)),(int(x1+w),int(y1+h)),color0,2)

    img = cv2.putText(img, str(clc), (x1-10, y1-10), font, 1.2, (0, 0, 255), 2)
    img = cv2.putText(img, str(conf), (x1+w+10, y1-10), font, 1.2, (0, 0, 255), 2)

    cv2.imwrite(os.path.join(save_path,file_name),img)



# img=cv2.imread("dataset/img_files/722_rgb_0458.png")


# # 0.998709,70,24,50,119
# # 0.999218,186,105,68,102
# # 0.881618,92,203,165,36
# bbox=[92,203,165,36]

# img = draw_box(img,bbox)

# cv2.imwrite('./test.jpg',img)

# load_output('FH_quant_tool/output_fall_standing.txt')

output_file='FH_quant_tool/output_fall_standing.txt'
data_dir='dataset/1176/rgb'
save_path='./output'

def main():
    output=load_output('FH_quant_tool/output_fall_standing.txt')

    for file in tqdm(output.keys()):
        process(data_dir,file,output[file],save_path)

    
main()