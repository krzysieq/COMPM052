import csv
import time
import numpy as np


def read_fold(file_path, return_qids=False):
    t_start = time.time()
    print("Reading {}".format(file_path))

    X = []; y = []; qids = []

    with open(file_path) as file:
        reader = csv.reader(file, delimiter=' ')

        for row in reader:
            label = int(row[0])
            qid = int(row[1].split(':')[1])
            features = [float(f.split(':')[1]) for f in row[2:-1]]

            X.append(features)
            y.append(label)
            qids.append(qid)

    print("Read {:d} vectors (took {:.1f} seconds).".format(len(y), time.time() - t_start))

    if return_qids:
        return np.array(X), np.array(y), np.array(qids)
    else:
        return np.array(X), np.array(y)
