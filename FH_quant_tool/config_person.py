import numpy as np
import os
from easydict import EasyDict as edict

config = edict()
# 0: detect car and person, 1: detect person, 2: detect face
config.mode = 1 

# 1. generate tfrecord
config.ann_file_dir = './ann_file/'
config.image_file_dir = './img_file/'
config.tfrecord_path = './data_person/person.tfrecords'
config.imgname_index_in_tfrecords = './data/shuffled_imgname.txt'
config.shuffle_enable = True

# 2. check tfrecords
config.save_pic_num = 10
config.save_pic_path = './pic_show'

# 3.
# training paras
config.train_batch_size = 8  # batch size in each gpu
config.gpu_index = '0, 1, 2, 3'

config.num_pic = 100000
config.each_epoch_steps = config.num_pic / (config.train_batch_size * len(config.gpu_index.split(",")))

config.learning_rate = [0.0, 0.0001, 0.00004, 0.00001]  # len(config.learning_rate) == len(config.lr_schedule) +1
config.lr_schedule = [100, 5 * config.each_epoch_steps, 10 * config.each_epoch_steps]
config.save_ckpt_every_n_steps = config.each_epoch_steps
config.training_steps = int(20 * config.each_epoch_steps)
config.ckpt = './Person/initial_fullhan_checkpoint_person.bin'

# output path
config.checkpoint_dir = './checkpoints_person'

# 4. test
config.ckpt_test = './Person/initial_fullhan_checkpoint_person.bin'
config.threshold = 0.3
# support (1) dir path (2) namelist .txt .pic with png|jpeg|jpg|tif|tiff|bmp
config.img_path_for_test = './img_file/'
config.output_txt_file = './output_Person.txt'

# 5. generate nbg file
config.ckpt_to_nbg = './Person/initial_fullhan_checkpoint_person.bin'
