# LSH and Blooms Filter for multi-label classification
Performing a multilabel classification using locality sensitive hashing and Blooms filter

# Datasets Used
* <a href="https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge"> Jigsaw Toxic Comment classification </a>
* <a href="https://archive.ics.uci.edu/ml/datasets/DeliciousMIL%3A+A+Data+Set+for+Multi-Label+Multi-Instance+Learning+with+Instance+Labels"> DeliciousMIL </a>

# Description about each file

Delicious Blooms.ipynb - Multilabel classification on DeliciousMIL Dataset using only Blooms Filter </br>
Delicious LSH.ipynb - Multilabel classification on DeliciousMIL Dataset using only locality sensitive hashing </br>
Delicious LSH + Blooms.ipynb - Multilabel classification on DeliciousMIL Dataset using both locality sensitive hashing and Blooms Filter </br>
Jigsaw Blooms.ipynb - Multilabel classification on Jigsaw Dataset using only Blooms Filter </br>
Jigsaw LSH.ipynb - Multilabel classification on Jigsaw Dataset using only locality sensitive hashing </br>
Jigsaw LSH + Blooms.ipynb - Multilabel classification on Jigsaw Dataset using both locality sensitive hashing and Blooms Filter </br>
delicious_data.csv - preprocessed csv for DeliciousMIL data </br>
blooms_filter.py - Contains the class BloomsFilter which is imported in all the Jupyter notebooks to implements BloomsFilter
