#!/usr/bin/python
#-*-coding:utf-8-*-

dataset_name = 'gxd'
# sentences = ['Would you like a plain sweater or something else?​', 'Great. We have some very nice wool slacks over here. Would you like to take a look?']
# labels = ['Yes' , 'No' ]
# train_or_test_list = ['train', 'test']

import csv
import random

def separate_dataset_by_label(dataset):
    rows = [[], []]
    for row in dataset:
        rows[int(row[2])].append(row)
    return rows


def count(lst, item):
  n = 0
  for ele in lst:
    if ele == item:
      n += 1
  return n

with open('../kaggle/train.csv', 'r') as f:
  reader = csv.reader(f)
  dataset = list(reader)
  rows_separated_by_labels = separate_dataset_by_label(dataset[1:])
  n = min(len(rows_separated_by_labels[0]), len(rows_separated_by_labels[1]))
  print(n)
  rows = random.sample(rows_separated_by_labels[0], n) + random.sample(rows_separated_by_labels[1], n)
  random.shuffle(rows)
  sentences = [row[1] for row in rows]
  labels = [row[2] for row in rows]
  print(count(labels, '1'))
  print(count(labels, '0'))
  train_or_test_list = ['train'] * len(sentences)

with open('../kaggle/test.csv', 'r') as f:
	reader = csv.reader(f)
	dataset = list(reader)
	sentences1 = [row[1] for row in dataset[1:]]
	sentences.extend(sentences1)
	labels.extend(['0' for _ in dataset[1:]])
	train_or_test_list.extend(['test'] * len(sentences1))

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