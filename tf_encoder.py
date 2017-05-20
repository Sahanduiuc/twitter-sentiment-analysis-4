import numpy as np
import pickle
from vocabulary import Vocabulary


class TfEncoder:
    def __init__(self, vocab):
        self.vocab = vocab

    """
    Encode each line in source_filename and dump the encoding to dest_filename.
    """
    def encode(self, source_filename, dest_filename):
        encoding = None
        with open(source_filename) as f:
            lines = [line.strip() for line in f.readlines()]
            encoding = list(map(self.vocab.get_tf_encoding, lines))
            print(len(encoding), encoding[0].shape)
            encoding = np.array(encoding)
            print(encoding.shape)

        with open(dest_filename, "wb") as fout:
            pickle.dump(encoding, fout)


if __name__ == "__main__":
    voc = Vocabulary("data/vocab.pkl")
    encoder = TfEncoder(voc)
    encoder.encode(
        "data/small_train.txt",
        "data/tf_encoded_small_train.pkl")

    with open("data/tf_encoded_small_train.pkl", "rb") as f:
        enc = pickle.load(f)
        print(enc.shape)
        print(np.sum(enc[:10], axis=1))
