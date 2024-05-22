# Emirhan's Method for Deepfake Detection

## Introduction
BLIP is a Vision-Language Pre-training (VLP) framework known for its proficiency in both vision-language understanding and generation tasks. It utilizes a multimodal mixture of encoder-decoder models, along with a novel captioning and filtering method for managing noisy data. In this project, we employ BLIP to detect deepfake content effectively.

## Dataset

The dataset utilized in this project includes 300 randomly selected examples from the FF++ dataset. It comprises:
- 150 Deepfake examples
- 150 Real examples

These examples are selected from 50 different videos, with each video contributing 3 frames to the dataset. You can access the dataset at [this Kaggle link](https://www.kaggle.com/datasets/emirhanbilgic/ff-blip-dataset).

## Running the Code

Follow these steps to run the code:

1. Clone the repository.
2. Download the dataset from the provided link.
3. Execute the script by running the following command in your terminal:
   ```bash
   python3 script.py /path/to/your/dataset

## Results

The logs of the testing process can be seen via logs_for_fakes.txt and logs_for_reals.txt files.

Accuracy on DeepFakes: 0.58 (29 true, 21 false)
Accuracy on Real Images: 0.62 (31 true, 19 false)
Accuracy in Total: 0.60 (60 true, 40 false)

