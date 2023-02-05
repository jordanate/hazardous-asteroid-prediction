# Hazardous Asteroid Classification

![asteroid](https://github.com/jordanate/hazardous-asteroid-prediction/blob/main/images/asteroid.jpg)

### Deployed Model:
https://jordanate-hazardous-asteroid-prediction-model-zab2dk.streamlit.app/

##### By: Jordana Tepper

## Project Description

This project aims to build a model that can classify an asteroid as hazardous to Earth (1) or not hazardous to Earth (0) using predictor variables such as the minimum and maximum diameter of the asteroid, absolute magnitude, minimum orbit intersection distance (MOID), and perihelion distance.

I decided to use recall as my primary metric because a false negative (classifying an asteroid as NOT hazardous when it is) is more costly than a false positive (classifying an asteroid as hazardous when it is NOT).

The final model from my project produced a recall score of 1.00.

### Definitions:
* **Absolute Magnitude**: The visual magnitude an observer would record if the asteroid were placed 1 Astronomical Unit (au) away, and 1 au from the Sun and at a zero phase angle [(NASA)](https://cneos.jpl.nasa.gov/glossary/h.html)   
* **Minimum Orbit Intersection Distance (MOID)**: The distance between the closest points of the osculating orbits of two bodies [(_Monthly Notices of the Royal Astronomical Society_)](https://academic.oup.com/mnras/article/479/3/3288/5039662) 
* **Perihelion Distance**: An orbit’s closest point to the Sun [(NASA)](https://cneos.jpl.nasa.gov/glossary/perihelion.html)

## Results

### Feature Importances

<p align = 'center'>
  <img width = '800' height = '600' src="https://github.com/jordanate/hazardous-asteroid-prediction/blob/main/images/feature_importances.png"> 
</p>

This visualization displays the importance scores for each predictor variable. A higher score indicates higher importance, and a lower score indicates lower importance.

### Confusion Matrix

<p align = 'center'>
  <img width = '720' height = '570' src="https://github.com/jordanate/hazardous-asteroid-prediction/blob/main/images/confusion_matrix.png"> 
</p>

This confusion matrix shows 0 false negatives and 3 false positives.

### ROC-AUC

<p align = 'center'>
  <img width = '720' height = '570' src="https://github.com/jordanate/hazardous-asteroid-prediction/blob/main/images/roc-auc.png"> 
</p>

This graph shows a ROC-AUC score of 1.00.


## Repository Structure

```
├── .ipynb_checkpoints
├── data
├── images
├── .gitignore
├── .jovianrc
├── README.md
├── hazardous-asteroid-prediction.ipynb
├── model.py
└── model6.pkl
```
