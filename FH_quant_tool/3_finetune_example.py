'''
This example finetune the data you privide.
Please make sure path is correct:
--config.checkpoint_dir
--config.ckpt

Time: 20210308
Author: jinyc339@fullhan.com

Fullhan All Rights Reserved
'''

from config import config


if config.mode == 0: # detect car and person
    import sys
    sys.path.append('./Car_Person')
if config.mode == 1: # detect person
    import sys
    sys.path.append('./Person')
if config.mode == 2: # detect face
    import sys
    sys.path.append('./Face')# make sure 'Face' dir is in place
    
import fullhan_nn
fullhan_nn.quant_train(config)
