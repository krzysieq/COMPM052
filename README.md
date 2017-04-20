# COMPM052: Information Retrieval and Data Mining Project

## Group 23 / Project 2
* Archit Sachdeva
* Georgi Georgiev
* Krzysztof Wroblewski

## Code Structure
`classifier/`
- `constants.py` -- use to set the dataset path
- `logistic_regression.py` -- our implementation of a binary logistic regression classifier
- `metrics.py` -- our implementation of metrics used during training and validation
- `mord.py` -- trains and evaluates an ordinal regression model; requires the `mord` package
- `multiclass.py` -- our implementation of one-vs-rest classification; contains a wrapper that can be used with any binary classifier
- `predict.py` -- uses a previously trained model to generate a ranking file, or simply evaluate on a test set
- `reader.py` -- contains code for reading and parsing dataset files
- `train.py` -- trains the logistic regression model

`eval.py` -- contains evaluation code and our implementation of ERR and NDCG metrics
