# xgboost_model_docker_image

Context: 

This repo is to train xgboost model and then use it to make predictions. The repo is creating a Gunicorn flask app. This app is using a prometheus client to extract metric data including CPU, Memory and network input and output to monitor the app. This app could pass Json input to a model python file where xgboost model is trained to be used for predictions in real time. The config of this app could be adjusted to scale this app to handle more requests as needed, to remain open for multiple HTTP requests/responses and improve the throughput of this app, allowing it to handle more requests in a given time period. The github action is used to build a docker image for this app to be pushed into the public registry in ECR. 

results:

<img width="989" height="424" alt="image" src="https://github.com/user-attachments/assets/6d8da0c1-4491-4cde-98d5-8302eb22f4fc" />

