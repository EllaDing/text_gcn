from utils import parse_index_file
import csv

dataset = 'gxd'

test_index = parse_index_file("data/{}.test.index".format(dataset))

with open("prediction.txt", "r") as f:
    pred = eval(f.read())

reordered_pred = [0 for _ in pred]

a = 1000000000
b = 0

for i in range(len(test_index)):
    a = min(a, test_index[i])
    b = max(b, test_index[i])

for i in range(len(test_index)):
    reordered_pred[test_index[i] - a] = pred[i]

print(a, b)

with open("submission.txt", "w") as f:
    f.write(str(reordered_pred))

with open('../kaggle/prediction1.csv', 'r') as f:
    reader = csv.reader(f)
    dataset = list(reader)
    pred = [int(row[1]) for row in dataset[1:]]
    print(len(pred))

with open('../kaggle/prediction1.txt', 'w') as f:
    f.write(str(pred))