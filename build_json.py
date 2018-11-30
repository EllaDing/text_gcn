import sys
import json
import pickle as pkl
import networkx as nx
import numpy as np
from networkx.readwrite import json_graph


dataset = 'R8'
train_proportion = 0.8


def load_data(dataset_str):
    print("Loading data...")

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
    return x, y, tx, ty, allx, ally, adj


def build_graph(allx, tx, ally, ty, adj):
    print("Building graph...")

    n = adj.shape[0]

    # Build label
    full_y = np.concatenate((ally, ty))
    assert full_y.shape[0] == n
    label = {}
    n_document = 0
    last_train_document = 0
    val_begin = 0
    val_end = 0
    for i in range(n):
        label[str(i)] = full_y[i].tolist()
        if sum(full_y[i].tolist()) > 0:
            n_document += 1
            last_document = i
            if val_end == 0 and sum(full_y[i + 1].tolist()) == 0:
                val_end = i
    val_begin = int(val_end * train_proportion)

    print("document: {} {}".format(n_document, last_document))
    print(val_begin, val_end)

    # Build ID map
    id_map = {}
    for i in range(n):
        id_map[str(i)] = i

    # Build feature
    feats = np.concatenate((allx.todense(), tx.todense()))
 
    # Build graph
    G = nx.Graph()
    n_train = int(allx.shape[0] * train_proportion)
    print(allx.shape)
    #for i in range(n_train):
        #G.add_node(i, val=False, test=False)
        #print(label[str(i)])
    for i in range(allx.shape[0]):
        G.add_node(i, val=(i >= val_begin and i <= val_end), test=False)
        #print(label[str(i)])
    for i in range(allx.shape[0], n):
        G.add_node(i, val=False, test=True)
    # TODO: add edge weight
    for i in range(n):
        for j in adj[i].indices:
            G.add_edge(i, j)

    return G, label, feats, id_map


def save_graph(G, label, feats, id_map):
    print("Saving graph...")

    G_json = json_graph.node_link_data(G)
    with open("data/" + dataset + "-G.json", "w") as f:
        json.dump(G_json, f)

    with open("data/" + dataset + "-class_map.json", "w") as f:
        json.dump(label, f)

    np.save("data/" + dataset + "-feats.npy", feats)

    with open("data/" + dataset + "-id_map.json", "w") as f:
        json.dump(id_map, f)


if __name__ == '__main__':
    #adj, features, y_train, y_val, y_test, train_mask, val_mask, test_mask = load_data(dataset)
    x, y, tx, ty, allx, ally, adj = load_data(dataset)
    G, label, feats, id_map = build_graph(allx, tx, ally, ty, adj)
    save_graph(G, label, feats, id_map)
