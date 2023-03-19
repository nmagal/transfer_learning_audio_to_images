# Transfer Learning from Audio to Images
## Background
In [Improving Audio Tagging with Pretraining, Sampling, Labeling, and Aggregation](https://arxiv.org/pdf/2102.01243.pdf)
the authors discuss that using a pretrained model on ImageNet leads to greater performance boosts on music tagging tasks.
The intuition of this is that the low level features that the model learns from the ImageNet dataset can be relevant in the audio domain for finding acoustic edges.
Given this, I experiment with pretraining a resnet18 model on the MagnaTagATune Dataset and measure its performance during training on the target dataset of the Caltech256 dataset.

## Results
![Performance](https://github.com/nmagal/transfer_learning_audio_to_images/blob/main/images/eval.png)
Results do not show too much difference from pretraining and random initialization of a model, and in some cases the pretrained model actually performs worse than the randomly initialized model.
Therefore, it does not seem like there is an useful knowledge retained from the model by pretraining on the MagnaTagATune Dataset.
Results are shown in the image above. The number in front of each run indicates how much of the training data of the target dataset that the model was trained on
For example, pretrained_.07 indicates the pretrained model's performance using 70% of the Caltech256 dataset.

## File Structure
* `data:` This directory contains files relating to the MagnaTagATune Dataset.
  * `annotations_final.csv:` File containing labels and paths for MagnaTagATune Dataset.
  * `annotations_final_proces.csv:` Preprocessed file containg labels and paths for MagnaTagATune after dropping corrupted data entries and including only Top 50 tags.
  * `top50_tags.txt:` File containing Top 50 tags of the MagnaTagATune dataset
* `scripts`
  * `caltech_evaluation.ipynb:` File for evaluating pretrained models vs random initialization of model on the Caltech256 dataset.
  * `mel_extractor.py:` File for extracting mel spectrograms from mp3 files.
  * `preprocess_annotations.py:` File for preprocessing dataset to drop corrupted data entries and include only Top 50 Tags.
  * `pretraining.ipynb:` File for pretraining model on the MagnaTagATune dataset.

