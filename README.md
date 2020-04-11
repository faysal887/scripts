# Utility scripts
This repository contains various useful scripts for data science projects.

## jupyter_init.ipynb
- A jupyter boilerplate for data science projects.
- Functionalities:
  - Collapsible sections
  - Auto reload of imported file if it is modified
  - Ignore warnings
  - Select max rows and columns to print when printing complete dataframe
  - Change cells width
  - Install jupyter dark theme
  - Save/load pickle files

## send_email.py
- Send email in python with attachment
- Allows mulitple receivers
- Allows multiple attachments

## randomforest_optimal.ipynb
- Random forest code with randomsearch and gridsearch for finding optimal parameters.

## fasttext_optimal_classify.ipynb
- Fasttext code with with autotune for finding optimal parameters.

## fasttext_classify_bagging.ipynb
- Bagging for NLP data with fasttext, also used for EDA to check on which categories we are performing good.

## rf_modeling.ipynb
- RF classification complete notebook (source: fastai ml1).

## rf_interpretation.ipynb
- Data Interpretation using RF complete notebook (source: fastai ml1).

## fastai_utils.py
- FastAi required functions to run notebooks without fastai installation.

## find_validation_set.ipynb
- Notebook for finding optimal validation set. This technique is very useful for kaggle competitions where test scores are kaggle scores after submission. This will help us in finding a good validation set according to the hidden kaggle's test set.
