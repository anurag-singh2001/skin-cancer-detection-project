# skin-cancer-detection-project

## Introduction
Skin cancer is the proliferation of the abnormal cells most commonly found on sun-exposed skin. One of the most dangerous forms of cancer is generally caused by unrepaired deoxyribonucleic acid (DNA) inside skin cells that generates skin genetic abnormalities or mutations on the skin. Skin cancer spreads gradually to other regions of the body, it is more treatable in the early stages, which is why it is best identified early.Over the past few decades, skin cancer has become more common everywhere.
The main motive of this project is to help dermatologists diagnose skin cancer through images of skin lesions so that doctors predict cancer at an early stage and treat more patients.


## Dataset

Our Dataset consists of 2357 images of malignant and benign oncological diseases, which were formed from The International Skin Imaging Collaboration (ISIC). Using the exception of melanomas and moles, whose photos have a minor predominance, all images were sorted according to the categorization determined with ISIC, and all subgroups were divided into the same number of images.

Dataset link: https://www.kaggle.com/datasets/nodoubttome/skin-cancer9-classesisic

![output](https://user-images.githubusercontent.com/72223953/199020925-04116602-aa6b-4906-8c79-35ef117a021a.jpg)


## Algorithms used

In this project we have used traditional machine learning algorithms like SVM and KNN for classification of images of skin. In both the algorithm we have used hypertuning parameter which gives the best result, to select the best combinations of hypertuning parameters we have used gridsearchcv which is a technique for finding the optimal parameter values from a given set of parameters in a grid. SVM shows the accuracy around 75% and KNN shows 66% accuracy. Then we have used basic ANN and CNN for this dataset and at last we have use transfer learning in which we have used VGG16 and inceptionV3 models and both models shows accuracy around 86%

## Web Application

After the training the model on dataset we have build web application with help of flask framework as backend and HTML CSS for the frontend. In this application user can upload there image of affect skin then in result it shows whether you are suffering from skin cancer disesas or not or you have to consult your dcotor or not

![Screenshot (241)](https://user-images.githubusercontent.com/72223953/199036220-f248936c-627f-40f8-a4b4-98035b1fdc7a.png)
![Screenshot (244)](https://user-images.githubusercontent.com/72223953/199036999-fd55e8e7-1097-4716-b343-37dc756636ef.png)

