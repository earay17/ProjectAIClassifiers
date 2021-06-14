import time
import numpy as np

from models.NaiveBayesModel import NaiveBayesModel
from models.RandomForestModel import RandomForestModel
from models.SVMLinearModel import SVMLinearModel
from models.SVMPolyModel import SVMPolyModel
from models.SVMRBFModel import SVMRBFModel
from models.SVMSigmoidModel import SVMSigmoidModel


def generate_model(model, matrix):
    """
    This function generates a model given a matrix
    :param model: Specific model to be created
    :param matrix: The input data of a model, a matrix
    """
    print("------------ Generating model: ", model.__name__, " ------------")
    clf_model = model(matrix)
    start_time = time.time()
    clf_model.training()
    clf_model.saving_model()
    total_time = time.time() - start_time
    print("Total time: ", total_time, "\n")


matrix = np.genfromtxt('generated/matrix.csv', delimiter=' ', comments='#')
np_matrix = np.array(matrix)
models = [NaiveBayesModel, RandomForestModel, SVMPolyModel, SVMSigmoidModel, SVMRBFModel]
for model in models:
    generate_model(model, np_matrix)
