# xgboost_model_docker_image
 
The repo is creating a Gunicorn flask app. This app is using a prometheus client to extract metric data including CPU, Memory and network input and output to monitor the app. This app could pass Json input to a model python file where xgboost model is trained to be used for predictions in real time. The config of this app could be adjusted to scale this app to handle more requests as needed, to remain open for multiple HTTP requests/responses and improve the throughput of this app, allowing it to handle more requests in a given time period. The github action is used to build a docker image for this app to be pushed into the public registry in ECR. 

Context 

This repo is a part of a project. This project is to receive requests from a source AWS account to provide prediction results based on a xgboost model in a target AWS account. 

To achieve this goal, the following repos are created for different purposes.    
1 A docker image of a Gunicorn flask app is created and pushed into ECR in this repo.

2 Deploy a EKS cluster in private subnets in VPC with a Nat gateway and an Internet gateway. The EKS is used to run Gunicorn flask apps based on the step 1. The related repo is https://github.com/ruihukuang/EKS_XGboost.

3 Deploy a bastion host in a public subnet in EC2 to interact with the EKS cluster in step 2 using Kubectl. This bastion host is used to deploy the Gunicorn flask app based on the step 1 into the EKS created in step 2. The related repo is https://github.com/ruihukuang/Cognito_kubectl_AWS.

4 Deploy Nginx as a load balancer and Gunicorn apps based on step 1 into EKS created in step 2 using Argo, Helm, Kubectl on the bastion host created in step 3. The URL of this Nginx load balancer is used to receive requests from a source AWS account. Th Gunicorn apps are used to process requests, do calculation based on a xgboost model and provide prediction results. The related repo is https://github.com/ruihukuang/Argo_Helm_Xgboost_EKS.

5 Deploy Prometheus and Grafana into EKS and create a dashboard in Grafana to monitor Gunicorn apps based on step 1. The related repo is https://github.com/ruihukuang/prometheus_grafana_Argo_Helm.
  


Purposes of this project and deployment related elements are shown in the graph below. 

<img width="1334" height="749" alt="image" src="https://github.com/user-attachments/assets/d08614a1-b4c7-4041-931d-0c2d79be6067" />



Results for this repo:

<img width="989" height="424" alt="image" src="https://github.com/user-attachments/assets/6d8da0c1-4491-4cde-98d5-8302eb22f4fc" />

