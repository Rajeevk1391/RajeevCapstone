[![CircleCI](https://circleci.com/gh/Rajeevk1391/RajeevCapstone/tree/main.svg?style=svg)](https://circleci.com/gh/Rajeevk1391/RajeevCapstone/tree/main)

# It is Capstone Udacity project to demonstrate implemnting docker image and kubernetes using Circleci pipeline. In this project Circleci orbs has been used

circleci/kubernetes@0.11.2
circleci/aws-eks@dev:alpha
circleci/circleci-cli@0.1.2
# Project5 Cloud Devops Capstone Project Overview
 this project is having rolling out deployment on Kubernetes
 
# Project  Tasks
Steps in Completing This Project
 1: Scope and perpose of this Project
 2: Under this project, Circle CI have been used to implement the blue/green or rolling deployment.
 3: i have used AWS Kubernetes as a Service and build the Kubernetes cluster.
 4: Build your pipeline
 5: Test your pipeline

# Environment Setup:
1.Setup the Environment
 Created a cluster and Run `make install` to install the necessary dependencies
 
2.Lint the App make lint and install required dependencies using requirement.txt

 

clone git repo https://github.com/Rajeevk1391/RajeevCapstone.git
	Run `make install` to install the necessary dependencies
	Run make lint to test the dokcerfile and application.py file
	Create kuberenetes cluster
	test cluster
	deploy the docker image at kubernetes
	test the deployment
	rolling out the app update 

