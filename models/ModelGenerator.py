import time
import numpy as np
import json
import jsonpickle
from sklearn import metrics
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score, GridSearchCV

def predictions(args):
    pass


class ModelGenerator:
    _matrix: np.array

    def __init__(self, matrix: np.array):
        """
        This method initialize the matrix variable with ndarray read from csv file
        :param matrix: ndarray read from csv file
        """
        self._matrix = matrix

    def old_training(self):
        """
        This method trains the machine learning algorithm.
        It splits the matrix in two parts: one for train and one for test
        """
        targets = self._matrix[:, 0]
        new_matrix = self._matrix
        new_matrix = np.delete(new_matrix, 0, axis=1)
        X_train, X_test, y_train, y_test = train_test_split(new_matrix, targets
                                                            , test_size=0.20, shuffle=True)
        print("Preparing the model...")
        self.clf = self.create_model()
        print("Training...")
        self.clf.fit(X_train, y_train)

    def training(self):
        """
           This method trains the machine learning algorithm.
           It splits the matrix in two parts: one for train and one for test
           """
        # Save targets in targets array
        targets = self._matrix[:, 0]
        new_matrix = self._matrix
        # Delete column of targets
        new_matrix = np.delete(new_matrix, 0, axis=1)
        # Splitting matrix
        X_train, X_test, y_train, y_test = train_test_split(new_matrix, targets
                                                            , test_size=0.20, shuffle=True)

        kf = StratifiedKFold(n_splits=10)

        print("Preparing the model...")
        self.clf = self.create_model()

        # Training phase
        start_time = time.time()
        print("Training...")
        self.clf.fit(X_train, y_train)
        total_time = time.time() - start_time
        print("Total time training: ", total_time, "\n")

        # Stratified cross validation phase
        start_time = time.time()
        scores = cross_val_score(self.clf, new_matrix, targets, cv=kf, scoring="accuracy")
        total_time = time.time() - start_time
        print("Total time training stratified cross-validation :  k = 10: ", total_time, "\n")
        print("Metrics cross_validation", scores)
        print("Stratified cross_validation mean", scores.mean())

        # Testing phase
        predictions = self.clf.predict(X_test)
        score_pred = metrics.accuracy_score(y_test, predictions)
        print("Metrics in Test", score_pred)

        # Total results
        print(classification_report(y_test, predictions))
        tn, fp, fn, tp = confusion_matrix(y_test, predictions).ravel()
        print("True Negatives: ", tn)
        print("False Positives: ", fp)
        print("False Negatives: ", fn)
        print("True Positives: ", tp)

    def saving_model(self):
        """
        This method saves the model in a json file using jsonpickle
        """
        name = self.__class__.__name__[:-5]
        data = jsonpickle.encode(self.clf)

        with open("generated/" + name + 'Filter.json', 'w') as file:
            json.dump(data, file)

    def saving_model(self):
        """
        This method saves the model in a json file using jsonpickle
        """
        name = self.__class__.__name__[:-5]
        data = jsonpickle.encode(self.clf)

        with open("generated/" + name + 'Filter.json', 'w') as file:
            json.dump(data, file)

    def create_model(self):
        pass
