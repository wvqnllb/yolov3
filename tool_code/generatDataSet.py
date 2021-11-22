# -*- coding: utf-8 -*-  
import os
import random
import shutil

def file_name(file_dir):  
  for _, _, files in os.walk(file_dir):
    return files

def spilt(files, shuffle = False, ratio = 0.1):
    n_total = len(files)
    offset = int(n_total * ratio)
    if n_total == 0 or offset < 1:
        return [], files
    if shuffle:
        random.shuffle(files)
    test_files = files[:offset]
    train_files = files[offset:]
    return test_files, train_files

file_dir = "../../safety_helmet/images"
files = file_name(file_dir)
small_files = files[:50]

test_files, train_files = spilt(files, True, 0.1)
train_file_handler = open('../../safety_helmet/train.txt', mode='w')
test_file_handler = open('../../safety_helmet/test.txt', mode='w')

for train_file in train_files:
    train_file_handler.write('./images/'+train_file+'\n')
    shutil.move('../../safety_helmet/images/'+train_file, '../../safety_helmet/images/train')
    train_label = train_file[0: len(train_file)-3] + 'txt'
    shutil.move('../../safety_helmet/labels/' + train_label, '../../safety_helmet/labels/train')
for test_file in test_files:
    test_file_handler.write('./images/'+test_file+'\n')
    shutil.move('../../safety_helmet/images/' + test_file, '../../safety_helmet/images/val')
    test_label = test_file[0: len(test_file) - 3] + 'txt'
    shutil.move('../../safety_helmet/labels/' + test_label, '../../safety_helmet/labels/val')
train_file_handler.close()
test_file_handler.close()

####  small data set generator ####
# small_test_files, small_train_files = spilt(small_files, True, 0.2)
# small_train_file_handler = open('../../small/train.txt', mode='w')
# small_test_file_handler = open('../../small/test.txt', mode='w')
# for train_file in small_train_files:
#     small_train_file_handler.write('./images/'+train_file+'\n')
#     shutil.move('../../small/images/'+train_file, '../../small/images/train')
#     train_label = train_file[0: len(train_file)-3] + 'txt'
#     shutil.move('../../small/labels/' + train_label, '../../small/labels/train')
# for test_file in small_test_files:
#     small_test_file_handler.write('./images/'+test_file+'\n')
#     shutil.move('../../small/images/' + test_file, '../../small/images/val')
#     test_label = test_file[0: len(test_file) - 3] + 'txt'
#     shutil.move('../../small/labels/' + test_label, '../../small/labels/val')
#
# small_train_file_handler.close()
# small_test_file_handler.close()