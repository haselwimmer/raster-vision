from os.path import join

from sklearn.metrics import fbeta_score
import numpy as np

from rastervision.common.settings import TRAIN
from rastervision.common.utils import save_json, load_json

TRAIN_THRESHOLDS = 'train_thresholds'


def load_thresholds(run_path):
    return np.array(load_json(join(run_path, 'thresholds.json')))


def save_thresholds(run_path, thresholds):
    save_json(thresholds.tolist(), join(run_path, 'thresholds.json'))


def compute_model_output(model, options, generator):
    y_true_list = []
    y_probs_list = []

    split_gen = generator.make_split_generator(
        TRAIN, target_size=None,
        batch_size=options.batch_size, shuffle=False, augment_methods=None,
        normalize=True, only_xy=False)

    sample_count = 0
    for batch_ind, batch in enumerate(split_gen):
        batch_y_probs = model.predict(batch.x)
        for sample_ind in range(batch.x.shape[0]):
            file_ind = batch.file_inds[sample_ind]

            y_probs = batch_y_probs[sample_ind, :]
            y_probs_list.append(np.expand_dims(y_probs, axis=0))

            y_true = generator.tag_store.get_tag_array([file_ind])[0, :]
            y_true_list.append(np.expand_dims(y_true, axis=0))

            sample_count += 1

        if (options.nb_eval_samples is not None and
                sample_count >= options.nb_eval_samples):
            break

    y_true = np.concatenate(y_true_list, axis=0)
    y_probs = np.concatenate(y_probs_list, axis=0)

    return y_true, y_probs


def optimize_thresholds(y_true, y_probs):
    nb_tags = y_true.shape[1]
    best_thresholds = np.ones((nb_tags,)) * 0.2
    y_preds = y_probs > np.expand_dims(best_thresholds, axis=0)
    best_f2 = fbeta_score(y_true, y_preds, beta=2, average='samples')

    for tag_ind in range(nb_tags):
        thresholds = np.copy(best_thresholds)
        for tag_thresh in np.arange(0, 1.0, 0.01):
            thresholds[tag_ind] = tag_thresh
            y_preds = y_probs > np.expand_dims(thresholds, axis=0)
            f2 = fbeta_score(y_true, y_preds, beta=2, average='samples')
            if f2 > best_f2:
                best_f2 = f2
                best_thresholds = np.copy(thresholds)

    return best_thresholds


def train_thresholds(run_path, model, options, generator):
    # Finding the correct thresholds seems to result in a small decrease in
    # test performance. I'm not sure what's going on, so for now
    # I'm commenting this out and setting thresholds to a default of 0.2 to
    # maintain the previous performance.
    
    # y_true, y_probs = compute_model_output(model, options, generator)
    # thresholds = optimize_thresholds(y_true, y_probs)
    thresholds = 0.2 * np.ones((len(generator.dataset.all_tags),))
    save_thresholds(run_path, thresholds)