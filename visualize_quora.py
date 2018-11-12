import matplotlib.pyplot as plt
import pandas as pd

from nltk.corpus import stopwords
from wordcloud import WordCloud

train = pd.read_csv('../input/train.csv')
sincere_questions = train[train['target'] == 0]['question_text']
insincere_questions = train[train['target'] == 1]['question_text']

stop_words = set(stopwords.words('english'))

sincere_vocab = {}
insincere_vocab = {}

for question in sincere_questions:
    for word in question.split(' '):
        word = word.lower()
        if word in stop_words:
            continue
        if word in sincere_vocab:
            sincere_vocab[word] += 1
        else:
            sincere_vocab[word] = 1

for question in insincere_questions:
    for word in question.split(' '):
        word = word.lower()
        if word in stop_words:
            continue
        if word in insincere_vocab:
            insincere_vocab[word] += 1
        else:
            insincere_vocab[word] = 1

sincere_vocabulary = sorted(sincere_vocab.items(), reverse=True, key=lambda kv: kv[1])
insincere_vocabulary = sorted(insincere_vocab.items(), reverse=True, key=lambda kv: kv[1])    

sincere_score = {}
for word, count in sincere_vocabulary:
    sincere_score[word] = count / insincere_vocab.get(word, 1)

wordcloud_sincere = WordCloud(width = 800, height = 800,background_color ='white', min_font_size = 10)
wordcloud_sincere.generate_from_frequencies(sincere_score) 
  
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud_sincere) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
plt.show() 

insincere_score = {}
for word, count in insincere_vocabulary:
    insincere_score[word] = count / sincere_vocab.get(word, 1)

wordcloud_insincere = WordCloud(width = 800, height = 800,background_color ='white', min_font_size = 10)
wordcloud_insincere.generate_from_frequencies(insincere_score) 
  
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud_insincere) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
plt.show()    