# Transfer Learning from Audio to Images
## Background
In [Improving Audio Tagging with Pretraining, Sampling, Labeling, and Aggregation](https://arxiv.org/pdf/2102.01243.pdf)
the authors discuss that using a pretrained model on ImageNet leads to greater performance boosts on music tagging tasks.
The intuition of this is that the low level features that the model learns from the ImageNet dataset can be relevant in the audio domain for finding acoustic edges.
Given this, I experiment with pretraining a resnet18 model on the MagnaTagATune Dataset and measure its performance during training on the target dataset of the Caltech256 dataset.

## Results
Results do not show too much difference from pretraining and random initializing a model.
Therefore, it does not seem like there is an useful knowledge retained from the model by pretraining on the MagnaTagATune Dataset.
Results are shown in the image above. The number in front of each run indicates how much of the training data of the target dataset that the model was trained on
For example, pretrained_.07 indicates the pretrained models performance using 70% of the Caltech256 dataset.
