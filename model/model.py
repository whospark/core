import abc

import numpy as np
import tensorflow as tf
from easy_model_saving import model_saver

from constants import MODEL_CHECKPOINTS_DIR, MODEL_INPUT_TENSOR_NAME, MODEL_OUTPUT_TENSOR_NAME
from model.model_helpers import ModelOutput


class Model:
    def __init__(self):
        pass

    @abc.abstractmethod
    def call(self, *args, **kwargs):
        raise Exception('Abstract method.')


class TensorflowModel(Model):
    def __init__(self):
        super().__init__()
        self.sess = tf.Session()
        with self.sess:
            last_step = model_saver.restore_graph_variables(MODEL_CHECKPOINTS_DIR)
        assert last_step != 0, 'No checkpoints have been found. Please train a model first.'
        self.output_tensor = model_saver.get_tensor_by_name(MODEL_OUTPUT_TENSOR_NAME)
        self.input_tensor = model_saver.get_tensor_by_name(MODEL_INPUT_TENSOR_NAME)

    def call(self, *args, **kwargs):
        close_prices = args[0]['last'].values.astype(np.float)
        feed_dict = {self.input_tensor: close_prices}
        out = self.sess.run(self.output_tensor, feed_dict=feed_dict)
        buy, sell, hold = out
        return ModelOutput(buy_confidence=buy, sell_confidence=sell, hold_confidence=hold)


class RandomCoinModel(Model):
    def __init__(self):
        super().__init__()

    def call(self, *args, **kwargs):
        # Toy model!
        buy, sell, hold = np.random.dirichlet(np.ones(3))
        return ModelOutput(buy_confidence=buy, sell_confidence=sell, hold_confidence=hold)
