# text_gcn

Text Graph Convolutional Networks for Quora Insincere Questions Classification.

# Require

Python 2.7 or 3.6

Tensorflow >= 1.4.0

# Reproduing Results

1. Run `prepare_data.py`

2. Run `python remove_words.py`

3. Run `python build_graph.py`

4. Run `python train.py`

# Input data

We use the data provided on Kaggle: https://www.kaggle.com/c/quora-insincere-questions-classification/data.
The training data includes the question that was asked, and whether it was identified as insincere (target = 1). The ground-truth labels contain some amount of noise: they are not guaranteed to be perfect.
