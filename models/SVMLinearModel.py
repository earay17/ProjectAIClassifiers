from models.ModelGenerator import ModelGenerator
from sklearn import svm


class SVMLinearModel(ModelGenerator):
    def create_model(self):
        """
        This method returns the respective classifier
        :return: SVM linear kernel classifier
        """
        return svm.SVC(kernel='linear')
