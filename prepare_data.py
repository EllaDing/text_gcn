#!/usr/bin/python
#-*-coding:utf-8-*-
import random
import re
dataset_name = 'test'
# sentences = ['Would you like a plain sweater or something else?​', 'Great. We have some very nice wool slacks over here. Would you like to take a look?']
# labels = ['Yes' , 'No' ]
# train_or_test_list = ['train', 'test']

import csv

sentences = []
labels = []

with open('../kaggle/train.csv', 'r') as f:
  reader = csv.reader(f)
  dataset = list(reader)
  random.shuffle(dataset)
  for row in dataset[1:]:
    question = row[1].lower()
    question = re.sub(r"[?|.|!]", r" ", question)
    question = re.sub("[\\n|\']", "", question)
    if len(question.split()) < 3:
      continue
    sentences.append(question)
    labels.append(row[2])

train_or_test_list = ['train'] * len(sentences)

# print(len(sentences), len(labels))
with open('../kaggle/test.csv', 'r') as f:
  reader = csv.reader(f)
  dataset = list(reader)
  for row in dataset[1:]:
    question = row[1].lower()
    question = re.sub(r"[?|.|!]", r" ", question)
    question = re.sub("[\\n|\']", "", question)
    if len(question.split()) < 3:
      print(question)
    sentences.append(question)
    labels.append('0')
    train_or_test_list.append('test')
    
  # labels.extend([row[2] for row in dataset[1:50001]])
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
