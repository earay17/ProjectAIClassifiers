from models.ModelGenerator import ModelGenerator
from sklearn import svm

class SVMSigmoidModel(ModelGenerator):

    def create_model(self):
        """
        This method returns the respective classifier
        :return: SVM sigmoid kernel classifier
        """
        return svm.SVC(kernel='sigmoid')
