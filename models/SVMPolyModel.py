from models.ModelGenerator import ModelGenerator
from sklearn import svm


class SVMPolyModel(ModelGenerator):

    def create_model(self):
        """
        This method returns the respective classifier
        :return: SVM polynomial kernel classifier
        """
        return svm.SVC(kernel='poly')