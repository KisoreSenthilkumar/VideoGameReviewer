Team Members:
Kisore Senthilkumar (50610194)
Harshita Itta (50605000)
Shashank Govindu (50594030)
Neeraj Gummadi(50594025)


Problem Statement:
The time and cost going into making video games is really high. During the beginning stage of the video game production cycle, if we are able to determine how the video game could potentially be received by observing previous releases of similar video games, it would help in altering ideas for the development team. We will be taking into consideration the scores, tags, genres, release time, etc of the games in dataset to help come to a conclusion about how the hypothesised game will be received. The idea also involves analysis of synopsis of the test game with similar games to see how it could possibly be received but it will be developed down the line.

Datasets obtained from https://www.kaggle.com/datasets/nikdavis/steam-store-raw

Kindly extract the files steam_app_data.csv and steamspy_data.csv from archive.zip for to load here

Comments of team members:

Kisore Senthilkumar 50610194:
Questions: 

How the genres listed for the game affect its rating. Will specific genres cause them to have a higher probability of a positive rating?

Code associated and Analysis location:
The code associated to this particular student can be found in 

a) 50610194_Phase2DataProcessing.ipynb file as the first section of code to preprocess the data 
b) 50610194_Phase2Models.ipynb file as the block of code where the analysis and modelling happened

Further output reports as PDF is available under the same names with the PDF extensions

Folder information:
The folder contains the 2 main code files and 2 PDF files as mentioned above
Then it contains two csv files 
a) "steam.csv" which is the dataset obtained after the end of phase 1 
b) "cleaned_data.csv" which contains the binary dataset to be used for the models 

References:

XGBoost documentation at https://xgboost.readthedocs.io/en/stable/

Random Forest Classifier documentation at https://scikit-learn.org/1.5/modules/generated/sklearn.ensemble.RandomForestClassifier.html

Harshita Itta 50605000:
Questions :

1) Can we classify games into different ownership levels (Low, High) based on their price?
2) Can we predict the log of ownership counts based on a game’s positive ratings and average playtime?

Code Associated and Analysis location :

50605000_Harshitha_Itta_phase2.ipynb - code and analysis are captured

The output is converted into pdf as :
50605000_Harshitha_Itta_phase2.pdf in same location

Folder information:
Folder has 1 ipynb code and analysis file , same is converted as 1 pdf file.
The derived dataset called steam.csv is attached.

References/Citations:
https://www.kaggle.com/code/prashant111/lightgbm-classifier-in-python ; https://www.analyticsvidhya.com/blog/2021/08/complete-guide-on-how-to-use-lightgbm-in-python/ ; https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.LGBMClassifier.html for LightGBM used in hypo 1

https://scikit-learn.org/dev/modules/generated/sklearn.linear_model.ElasticNet.html ; https://medium.com/@abhishekjainindore24/elastic-net-regression-combined-features-of-l1-and-l2-regularization-6181a660c3a5 for elasticnet used in hypo2

https://scikit-learn.org/dev/modules/generated/sklearn.ensemble.StackingRegressor.html https://www.analyticsvidhya.com/blog/2020/12/improve-predictive-model-score-stacking-regressor/ for stacking regressor used in hyo2

Shashank Govindu 50594030

Questions:

Q1]What is the relationship between the length of the "detailed_description" and the "score" of the game?

Q2]How do the "categories" affect the "score" of a game?

Code associated and Analysis location: The code associated to this particular student can be found in 50594030_Phase2.ipynb 

PDF is available under the same name with the PDF extension

Folder information:

The folder contains 1 code file and 1 PDF file as mentioned above

Then it contains 1 csv files
"df_cleaned_out.csv" which contains further cleaned dataset
(the csv file has been uploaded as rar to accomodate for the file size, kindly extract it)

One-Way ANOVA:

References:

Scipy documentation for ANOVA (scipy.stats module):
https://docs.scipy.org/doc/scipy/reference/stats.html#anova
ANOVA tutorial with scipy.stats:
https://www.statology.org/one-way-anova-python/
Polynomial Ridge Regression:

Scikit-learn Polynomial Features and Ridge Regression:
https://scikit-learn.org/stable/auto_examples/linear_model/plot_polynomial_interpolation.html
Polynomial Regression tutorial (with Ridge as an extension):
https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html
https://scikit-learn.org/stable/modules/linear_model.html#ridge-regression


Neeraj Gummadi 50594025

Questions:

Q1]Is there a significant difference in “score” between free games and paid games as indicated by the “price”?

Q2]Do games with more “supported_languages” tend to receive higher “scores”?

Code associated and Analysis location: The code associated to this particular student can be found in 50594025_Phase2.ipynb 

PDF is available under the same name with the PDF extension

Folder information:

The folder contains 1 code file and 1 PDF file as mentioned above

Then it contains one csv files


1) "df_cleaned_out.csv" which contains further cleaned dataset
(the csv file has been uploaded as rar to accomodate for the file size, kindly extract it)
Gradient Boosting Machine (GBM):

References:
Scikit-learn documentation on Gradient Boosting:
https://scikit-learn.org/stable/modules/ensemble.html#gradient-boosting
Gradient Boosting tutorial with scikit-learn:
https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regression.html
Logistic Regression:

Scikit-learn documentation on Logistic Regression:
https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
Logistic Regression tutorial with scikit-learn:
https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic.html



