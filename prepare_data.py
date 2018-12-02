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

def clean_text(x):

    x = str(x)
    for punct in "/-'":
        x = x.replace(punct, ' ')
    for punct in '&':
        x = x.replace(punct, ' {punct} ')
    for punct in '?!.,"#$%\'()*+-/:;<=>@[\\]^_`{|}~' + '“”’':
        x = x.replace(punct, '')

    x = re.sub('[0-9]{5,}', '#####', x)
    x = re.sub('[0-9]{4}', '####', x)
    x = re.sub('[0-9]{3}', '###', x)
    x = re.sub('[0-9]{2}', '##', x)
    return x

def _get_mispell(mispell_dict):
    mispell_re = re.compile('(%s)' % '|'.join(mispell_dict.keys()))
    return mispell_dict, mispell_re


mispell_dict = {'colour':'color',
                'centre':'center',
                'didnt':'did not',
                'doesnt':'does not',
                'isnt':'is not',
                'shouldnt':'should not',
                'favourite':'favorite',
                'travelling':'traveling',
                'counselling':'counseling',
                'theatre':'theater',
                'cancelled':'canceled',
                'labour':'labor',
                'organisation':'organization',
                'wwii':'world war 2',
                'citicise':'criticize',
                'instagram': 'social medium',
                'whatsapp': 'social medium',
                'snapchat': 'social medium'

                }
mispellings, mispellings_re = _get_mispell(mispell_dict)

def replace_typical_misspell(text):
    def replace(match):
        return mispellings[match.group(0)]

    return mispellings_re.sub(replace, text)

with open('../kaggle/train.csv', 'r') as f:
  reader = csv.reader(f)
  dataset = list(reader)
  random.shuffle(dataset)
  for row in dataset[1070000:]:
    question = replace_typical_misspell(clean_text(row[1].lower()))
    question = re.sub("\\n", "", question)
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
    question = replace_typical_misspell(clean_text(row[1].lower()))
    question = re.sub("\\n", "", question)
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
