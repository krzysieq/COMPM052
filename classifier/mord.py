import constants
import reader

import mord
import pickle


def train(X_train, y_train, alpha=1., save_as=None):
    model = mord.LogisticAT(verbose=3, max_iter=1000, alpha=alpha)
    model.fit(X_train, y_train)

    if save_as is not None:
        with open(save_as, "wb") as f:
            pickle.dump(model, f)

if __name__ == "__main__":
    X_train, y_train = reader.read_fold(constants.DATASET_PATH + "Fold1/train.txt")

    for alpha in [0., 0.5, 1., 1.5, 2]:
        train(X_train, y_train, alpha, "models/model_mord_{:.1f}.pkl".format(alpha))

