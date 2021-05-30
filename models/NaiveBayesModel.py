from sklearn.naive_bayes import MultinomialNB
from models.ModelGenerator import ModelGenerator


class NaiveBayesModel(ModelGenerator):

    def create_model(self):
        """
        This method returns the respective classifier
        :return: Multinomial Naive Bayes  classifier
        """
        return MultinomialNB()
