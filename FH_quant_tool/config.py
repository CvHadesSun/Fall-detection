import numpy as np
import os
from easydict import EasyDict as edict

config = edict()
# 0: detect car and person, 1: detect person, 2: detect face
config.mode = 0 

# 1. generate tfrecord
config.ann_file_dir = './../dataset/label_files/'
config.image_file_dir = './../dataset/img_files/'
config.tfrecord_path = './data_person_car/person_car.tfrecords'
config.imgname_index_in_tfrecords = './data/shuffled_imgname.txt'
config.shuffle_enable = True

# 2. check tfrecords
config.save_pic_num = 10
config.save_pic_path = './output'

# 3.
# training paras
config.train_batch_size = 8  # batch size in each gpu
config.gpu_index = '0'
config.num_pic = 25000
config.each_epoch_steps = config.num_pic / (config.train_batch_size * len(config.gpu_index.split(",")))


config.learning_rate = [0.0, 0.0001, 0.00004, 0.00001, 0.000004, 0.000001]  # len(config.learning_rate) == len(config.lr_schedule) +1
config.lr_schedule = [100, 40 * config.each_epoch_steps, 60 * config.each_epoch_steps, 80 * config.each_epoch_steps, 112 * config.each_epoch_steps]
config.save_ckpt_every_n_steps = config.each_epoch_steps
config.training_steps = int(128 * config.each_epoch_steps)
config.ckpt = './checkpoints_person_car/model_finetune_iteration_2500000.bin'
config.loss_rate_classes = [1.0,1.0] #[person loss weight, car loss weight]   
# output path
config.checkpoint_dir = './checkpoints_person_car'

# 4. test
config.ckpt_test = './checkpoints_person_car/model_finetune_iteration_2500000.bin'
config.threshold = 0.3
# support (1) dir path (2) namelist .txt .pic with png|jpeg|jpg|tif|tiff|bmp
config.img_path_for_test = './../dataset/1176/rgb/'
config.output_txt_file = './output_fall_standing.txt'

# 5. generate nbg file
config.ckpt_to_nbg = './Car_Person/initial_fullhan_checkpoint_PersonCar.bin'
