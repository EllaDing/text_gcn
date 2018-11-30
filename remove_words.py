from nltk.corpus import stopwords
import nltk
from nltk.wsd import lesk
from nltk.corpus import wordnet as wn
from utils import clean_str, loadWord2Vec
import sys

# nltk.download()
stop_words = set(stopwords.words('english'))
print(stop_words)

# Read Word Vectors
# word_vector_file = 'data/glove.6B/glove.6B.200d.txt'
# vocab, embd, word_vector_map = loadWord2Vec(word_vector_file)
# word_embeddings_dim = len(embd[0])

dataset = 'test'

doc_content_list = []
f = open('data/corpus/' + dataset + '.txt', 'rb')
# f = open('data/wiki_long_abstracts_en_text.txt', 'r')
for line in f.readlines():
    doc_content_list.append(line.strip().decode('latin1'))
f.close()


word_freq = {}  # to remove rare words

for doc_content in doc_content_list:
    temp = clean_str(doc_content)
    words = temp.split()
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

clean_docs = []
i = 0

for doc_content in doc_content_list:
    temp = clean_str(doc_content)
    words = temp.split()
    doc_words = []
    for word in words:
        # and word in word_vector_map
        if word not in stop_words and word_freq[word] >= 4: #word not in stop_words and word_freq[word] >= 5
            doc_words.append(word)
    doc_str = ' '.join(doc_words).strip()
    if len(doc_str) == 0 and i < 10:
        i += 1
        print(doc_content, temp, words)
    if len(doc_str) == 0:
        if len(temp) == 0:
            clean_docs.append(doc_content)
        else: clean_docs.append(temp)
    else:
        clean_docs.append(doc_str)
    if len(doc_str) == 0 and i < 10:
        i += 1
        print(clean_docs[-3:])
clean_corpus_str = '\n'.join(clean_docs)
print('total lines:', len(clean_docs))
f = open('data/corpus/' + dataset + '.clean.txt', 'w')
#f = open('data/wiki_long_abstracts_en_text.clean.txt', 'w')
f.write(clean_corpus_str)
f.close()

min_len = 10000
aver_len = 0
max_len = 0 

f = open('data/corpus/' + dataset + '.clean.txt', 'r')
#f = open('data/wiki_long_abstracts_en_text.txt', 'r')
k = 0
lines = f.readlines()
for line in lines:
    line = line.strip()
    temp = line.split()
    if len(temp) == 0:
        print(temp, clean_docs[k], doc_content_list[k])
    k += 1
    aver_len = aver_len + len(temp)
    if len(temp) < min_len:
        min_len = len(temp)
    if len(temp) > max_len:
        max_len = len(temp)
f.close()
aver_len = 1.0 * aver_len / len(lines)
print('min_len : ' + str(min_len))
print('max_len : ' + str(max_len))
print('average_len : ' + str(aver_len))
print('total line:', len(lines))
