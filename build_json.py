import sys
import pickle as pkl


dataset = 'gxd'

def load_data(dataset_str):
    names = ['x', 'y', 'tx', 'ty', 'allx', 'ally', 'adj']
    objects = []
    for i in range(len(names)):
        with open("data/ind.{}.{}".format(dataset_str, names[i]), 'rb') as f:
            if sys.version_info > (3, 0):
                objects.append(pkl.load(f, encoding='latin1'))
            else:
                objects.append(pkl.load(f))

    x, y, tx, ty, allx, ally, adj = tuple(objects)
    print(x.shape, y.shape, tx.shape, ty.shape, allx.shape, ally.shape)
    print(adj.shape)
    print(adj[0])

if __name__ == '__main__':
    #adj, features, y_train, y_val, y_test, train_mask, val_mask, test_mask = load_data(dataset)
    load_data(dataset)