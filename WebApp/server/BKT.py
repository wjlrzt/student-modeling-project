from hmmlearn.hmm import MultinomialHMM
import numpy as np


class BKT:
    """
    Implements the Bayesian Knowledge Tracing model. This only
    implements the Viterbi and EM algorithms. These may be used
    together to implement an Intelligent Tutoring System.
    """
    def __init__(self, observed):
        """
        Initializes the object and sets the internal state.

        Args:
            observed: array-like, shape (n_samples, n_features)
        """
        self.observed = np.array(observed)

        if len(self.observed.shape) == 1:
            self.observed = self.observed.reshape(-1, 1)
        # TODO: Check other parameters to this constructor
        self.model = MultinomialHMM(n_components=2, n_iter=100)

    def fit(self) -> None:
        """
        Fits the model to the observed states. Uses the EM algorithm
        to estimate model parameters.
        """
        self.model.fit(self.observed)

    def get_model_params(self) -> tuple:
        """
        Returns the model parameters. This must be run only after
        calling the `fit` function.

        Returns:
            (A, pi, B): The start probabilities, the transition
                        probabilities, and the emission probabilities.
        """
        return np.round_(self.model.startprob_, 2), np.round_(self.model.transmat_, 2), \
            np.round_(self.model.emissionprob_, 2)

    def predict(self, sequence) -> np.array:
        """
        Returns the most likely hidden state sequence corresponding to
        `sequence`.

        Args:
            sequence: List of observable states

        Returns:
            state_sequence: Array
        """
        return self.model.predict(sequence)
