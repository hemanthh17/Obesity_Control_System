## Inspiration
We are living in a very busy world where we neglect our health and give more priority to work. Obesity is a dark disease that is conquering the lives of most of the young generation. We want to design a software application which youngsters and other age groups can use with ease and the output will give suggestions on what to do next. 


## What it does
The model uses datasets and predicts the obesity pattern in an individual based on the inputs given by him/her. This model applies Decision Trees algorithm on the datasets to predict the obesity pattern with an accuracy of 95%. The inputs taken from the individual are:

Age, Gender, Height, Family History with Overweight, Frequent consumption of high caloric food
Frequent consumption of vegetables, Number of main/heavy meals in a day, Consumption of food between meals, Tobacco Consumption, Drinking water consumption (Litres), Calories consumption monitoring, Physical activity frequency, Usage of electronic gadgets (hours), Consumption of alcohol, Mode of transportation to work

## How we built it
We used the dataset from Kaggle which helped us train the ML model and for interfacing we used Flask and HTML.

## Challenges we ran into
There are big companies like GOQII, FITBIT which have tried to implement fitness bands which track basic entities like steps, calories burned , heart rate and so on that have a motivational aspect to complete the target that has been set. For example 10000k steps a day, but having used these kinds of products we see the majority of them do not follow it. So we thought we will create an analyzer that will predict the type of obesity a person has and give an output with the consequences if it is not treated. 
  

## Accomplishments that we're proud of
We have included the majority of the factors and we have obtained a good accuracy and we feel this application will be useful for all. We also have learnt to deploy an ML model using Flask.

## What we learned
We learnt how to pipeline the ML model which will make the deployment of it easily. More than that we learnt about the Flask framework. Being this our first hackathon where we have used ML we learnt a lot.

## What's next for OBESITY PREDICTION ANALYSER
There are various other diseases such as BP,Sugar which is also claiming lives, we want to next build a healthy food recommender system which will suggest really healthy diets based on time, like for breakfast we can suggest diets which will satisfy all the requirements of nutrients. Post this we will also have a system that will recommend exercise such that the application impacts as many and you will see more fit people around you rather than. We also want to include sleep as a parameter for obesity and most of the datasets are ignored. We can include this as a third part application for most of the smart watches.

## How to run
Go to venv and execute app.py file you will have to connect to localhost http://127.0.0.1:5000/ and you will now be able to see the form. fill the form and the next page will give you the outcome. 
