import constants
import metrics
import reader
import pickle
import numpy as np


def test(model_file, X_test, y_test):
    with open(model_file, "rb") as f:
        model = pickle.load(f)

    y_pred = model.predict(X_test)

    acc = metrics.accuracy_score(y_test, y_pred)
    err = metrics.mean_absolute_error(y_test, y_pred)
    print("Accuracy: {:.4f}".format(acc))
    print("Mean absolute error: {:.4f}".format(err))


def get_predictions(model_file, X_test, qids, save_as):
    with open(model_file, "rb") as f:
        model = pickle.load(f)

    y_pred = model.predict(X_test)

    out = []

    for qid in np.unique(qids):
        query_docs = qids == qid
        order = np.argsort(y_pred[query_docs])[::-1]
        out += ["{:d}\t{:d}".format(qid, rank) for rank in order]

    out = "\n".join(out)

    with open(save_as, "w") as f:
        f.write(out)


if __name__ == "__main__":
    # X_test, y_test = reader.read_fold(constants.DATASET_PATH + "Fold1/test.txt")
    # test("models/model_ovr_fold1_1.pkl", X_test, y_test)

    X_test, y_test, qids = reader.read_fold(constants.DATASET_PATH + "Fold1/test.txt", True)
    get_predictions("models/model_ovr_fold1_1.pkl", X_test, qids, "scores/test_ovr")
    get_predictions("models/model_mord_1.5.pkl", X_test, qids, "scores/test_mord_1.5")
