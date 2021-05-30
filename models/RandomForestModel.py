from models.ModelGenerator import ModelGenerator
from sklearn.ensemble import RandomForestClassifier


class RandomForestModel(ModelGenerator):

    def create_model(self):
        """
        This method returns the respective classifier
        :return: Random Forest classifier
        """
        return RandomForestClassifier(max_depth=2, random_state=0)