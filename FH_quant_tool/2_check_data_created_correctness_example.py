'''
This example show images with annotations in tfrecords
Time: 20201218
Author: jinyc339@fullhan.com

Fullhan All Rights Reserved
'''
from config import config

if config.mode == 0: # detect car&person or person
    import sys
    sys.path.append('./tool') 
if config.mode == 1: # detect car&person or person
    import sys
    sys.path.append('./tool')     
if config.mode == 2: # detect face
    import sys
    sys.path.append('./Face')# make sure 'Face' dir is in place


import fullhan_nn

fullhan_nn.save_img_from_tfrecords(config)