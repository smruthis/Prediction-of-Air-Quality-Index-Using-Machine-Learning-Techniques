# Prediction-of-Air-Quality-Index-Using-Machine-Learning-Techniques

**INTRODUCTION**

Air pollution is a global problem that affects public health, the environment, and the economy. In India, poor air quality is a particularly pressing issue that impacts millions of people. The goal of this project is to use data science techniques to analyze air quality data in Indian cities and develop insights into the factors that contribute to poor air quality.

The dataset used in this project contains information on air quality in Indian cities. It includes records of Air Quality Index (AQI) values and pollutant levels for the period from 2015 to 2020. The data was collected by the Central Pollution Control Board (CPCB), an Indian government agency responsible for monitoring and controlling pollution levels in the country.

The dataset contains information for 26 different cities in India, with varying numbers of observations per city. For each observation, the dataset includes the AQI value, as well as the concentrations of 12 different pollutants: PM2.5, PM10, NO, NO2, NOx, NH3, CO, SO2, O3, benzene, toluene, and xylene. The data is organized by city, year, month, day, quarter, day of the week, state, and zone. This dataset can be used to gain insights into air quality trends, and factors affecting air pollution, and to develop predictive models for future AQI values.

**EXPLORATORY DATA ANALYSIS**

Exploratory Data Analysis (EDA) is a crucial step in any data analysis project, as it helps to
identify patterns, relationships, and anomalies in the data. In this project, EDA was conducted on
a dataset containing records of AQIs and pollutant levels in various Indian cities. The data was
first cleaned and pre-processed, which involved checking for missing values, outliers, and
inconsistencies.

Histograms are used to identify the relationships between the different pollutants and AQI values,
while boxplots were used to visualize the distribution of the data and identify potential outliers.
Heatmaps are also used to identify spatial patterns and trends in air quality across different regions.
The EDA revealed several interesting insights about air quality in India. For example, it was found
that certain pollutants, such as PM2.5 and NO2, were consistently high across all cities, while
others, such as SO2 and CO, showed more variability. It was also found that air quality was
generally worse in the northern and eastern regions of India, with cities such as Delhi and Kolkata
having particularly high AQI values.
Overall, the EDA helped to identify important trends and patterns in the data, which informed
subsequent analysis and modeling efforts. By gaining a deeper understanding of the data, we were
able to develop more accurate predictive models and make more informed recommendations for
policy interventions aimed at reducing air pollution and improving public health.

**DATA PREPROCESSING**

Data pre-processing is a crucial step in data analysis that involves transforming raw data into a
format that is suitable for analysis. It typically involves cleaning, transforming, and restructuring
data to ensure that it is accurate, complete, and relevant for analysis.The following steps were done:

1. Null value handling
2. Encoding
3. Feature Engineering
4. Feature Reduction
5. Feature Scaling
6. Normalization

**MODEL BUILDING**

As part of model creation, we have first splitted our dataset mainly to two:

⦁ Training Set

⦁ Validation Set

The training set is again divided into training and testing data.We have splitted the training
dataset such that training data accounts for 75% of training set and testing data accounts for 25%
of training set.
The Validation Set contains data which is taken on the condition that the target column for this
data contains null values.

In this project I have used the Random Forest Regressor for modelling as I got maximum accuracy
from Random Forest Regressor as 0.909.


**CODE**: https://github.com/smruthis/Prediction-of-Air-Quality-Index-Using-Machine-Learning-Techniques/blob/main/AQI%20CODE.ipynb





