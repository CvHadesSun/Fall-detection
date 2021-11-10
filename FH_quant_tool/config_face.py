import numpy as np
import os
from easydict import EasyDict as edict

config = edict()
# 0: detect car and person, 1: detect person, 2: detect face
config.mode = 2 

# 1. generate tfrecord
config.ann_file_dir = './ann_file/'
config.image_file_dir =  './img_file/'
config.tfrecord_path = "./data_face/"
config.imgname_index_in_tfrecords =  './data/shuffled_imgname' #dir

config.shuffle_enable = True

# 2. check tfrecords
config.save_pic_num = 100
config.save_pic_path = './pic_show'

# 3.
# training paras
config.train_batch_size = 16 # only support one GPU
config.gpu_index = '0'

config.num_pic = 4800
config.each_epoch_steps = config.num_pic / (config.train_batch_size * len(config.gpu_index.split(",")))

config.learning_rate = [0.0, 0.001, 0.0004,0.0001,0.00004,0.00001] 
config.lr_schedule = [100, 40 * config.each_epoch_steps,60 * config.each_epoch_steps,80 * config.each_epoch_steps,
                      112 * config.each_epoch_steps]
config.save_ckpt_every_n_steps = int(config.each_epoch_steps)
config.training_steps = int(128 * config.each_epoch_steps)
config.ckpt = './Face/initial_fullhan_checkpoint_face.bin'

# output path
config.checkpoint_dir = './ckpt'




# 4. test
config.ckpt_test = './Face/initial_fullhan_checkpoint_face.bin'
config.threshold = 0.05
# support (1) dir path (2) namelist .txt .pic with png|jpeg|jpg|tif|tiff|bmp
config.img_path_for_test = './img_file/'
config.output_txt_file = 'output.txt'


# 5. generate nbg file
config.ckpt_to_nbg = './Face/initial_fullhan_checkpoint_face.bin'
