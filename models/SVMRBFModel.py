from sklearn import svm
from models.ModelGenerator import ModelGenerator


class SVMRBFModel(ModelGenerator):

    def create_model(self):
        """
        This method returns the respective classifier
        :return: SVM RBF kernel classifier
        """
        return svm.SVC(kernel='rbf')
