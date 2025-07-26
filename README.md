# xgboost_model_docker_image
 
The repo is creating a Gunicorn flask app. This app is using a prometheus client to extract metric data including CPU, Memory and network input and output to monitor the app. This app could pass Json input to a model python file where xgboost model is trained to be used for predictions in real time. The config of this app could be adjusted to scale this app to handle more requests as needed, to remain open for multiple HTTP requests/responses and improve the throughput of this app, allowing it to handle more requests in a given time period. The github action is used to build a docker image for this app to be pushed into the public registry in ECR. 


# Home Project Overview  
This project is designed to receive requests from a source AWS account and provide prediction results based on an XGBoost model hosted in a target AWS account. The project is divided into several repositories, each serving a specific purpose:
Docker Image Creation:  
A Docker image of a Gunicorn Flask app is created and pushed to Amazon ECR. This image contains the XGBoost model for making predictions.  
Repository: [xgboost_model_docker_image.](https://github.com/ruihukuang/xgboost_model_docker_image.)  
EKS Cluster Deployment:  
An EKS cluster is deployed in private subnets within a VPC, equipped with a NAT Gateway and an Internet Gateway. This cluster is used to run the Gunicorn Flask apps created in Step 1.  
Repository: https://github.com/ruihukuang/EKS_XGboost   
Bastion Host Setup:  
A bastion host is deployed in a public subnet using EC2 to interact with the EKS cluster from Step 2 via kubectl. This host is used to deploy the Gunicorn Flask app into the EKS cluster.  
Repository: https://github.com/ruihukuang/Cognito_kubectl_AWS  
Load Balancer and App Deployment:  
Nginx is deployed as a load balancer, and Gunicorn apps are deployed into the EKS cluster using Argo, Helm, and kubectl from the bastion host. The Nginx load balancer's URL is used to receive requests from the source AWS account. The Gunicorn apps process these requests, perform calculations using the XGBoost model, and provide prediction results.  
Repository: https://github.com/ruihukuang/Argo_Helm_Xgboost_EKS    
Monitoring Setup:  
Prometheus and Grafana are deployed into the EKS cluster, and a dashboard is created in Grafana to monitor the Gunicorn apps.  
Repository: https://github.com/ruihukuang/prometheus_grafana_Argo_Helm
  


Purposes of this project and deployment related elements are shown in the graph below. 

<img width="1334" height="749" alt="image" src="https://github.com/user-attachments/assets/d08614a1-b4c7-4041-931d-0c2d79be6067" />



Results for this repo:

<img width="989" height="424" alt="image" src="https://github.com/user-attachments/assets/6d8da0c1-4491-4cde-98d5-8302eb22f4fc" />

