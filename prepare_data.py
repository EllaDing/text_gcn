#!/usr/bin/python
#-*-coding:utf-8-*-
import random

dataset_name = 'include_test'
# sentences = ['Would you like a plain sweater or something else?​', 'Great. We have some very nice wool slacks over here. Would you like to take a look?']
# labels = ['Yes' , 'No' ]
# train_or_test_list = ['train', 'test']

import csv

with open('../kaggle/train.csv', 'r') as f:
  reader = csv.reader(f)
  dataset = list(reader)
  random.shuffle(dataset)
  sentences = [row[1] for row in dataset[1080000:]]
  labels = [row[2] for row in dataset[1080000:]]
  train_or_test_list = ['train'] * len(sentences)

print(len(sentences), len(labels))
with open('../kaggle/test.csv', 'r') as f:
	reader = csv.reader(f)
	dataset = list(reader)
	sentences1 = [row[1] for row in dataset[1:]]
	# labels.extend([row[2] for row in dataset[1:50001]])
	sentences.extend(sentences1)
	labels.extend(['0' for _ in dataset[1:]])
	train_or_test_list.extend(['test'] * len(sentences1))

print(len(sentences), len(train_or_test_list), len(labels))
meta_data_list = []

for i in range(len(sentences)):
    meta = str(i) + '\t' + train_or_test_list[i] + '\t' + labels[i]
    meta_data_list.append(meta)

meta_data_str = '\n'.join(meta_data_list)
print(len(meta_data_list))
f = open('data/' + dataset_name + '.txt', 'w')
f.write(meta_data_str)
f.close()

corpus_str = '\n'.join(sentences)
print(len(sentences))
f = open('data/corpus/' + dataset_name + '.txt', 'w')
f.write(corpus_str)
f.close()
