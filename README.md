[![CircleCI](https://circleci.com/gh/Rajeevk1391/RajeevCapstone/tree/main.svg?style=svg)](https://circleci.com/gh/Rajeevk1391/RajeevCapstone/tree/main)

# It is Capstone Udacity project to demonstrate implemnting docker image and kubernetes using Circleci pipeline.

  aws-cli: circleci/aws-cli@2.0.3
  
  kubernetes: circleci/kubernetes@0.12.0
  
  aws-eks: circleci/aws-eks@1.1.0
  
  
 #Project5 Cloud Devops Capstone Project Overview
  This project is having Amazon EKS fr creating  Kubernetes cluster
 
# Project  Tasks
Steps in Completing This Project
 1: Scope and perpose of this Project
 
 2: Under this project, Circle CI have been used to implement the rolling out  deployment.
 
 3: I have used AWS Kubernetes as a Service and build the Kubernetes cluster.
 
 4: Build your pipeline
 
 5: Test your pipeline

# Environment Setup:
1.Setup the Environment
 Created a cluster and Run `make install` to install the necessary dependencies
 
2.Lint the App make lint and install required dependencies using requirement.txt

3.Create kuberenetes cluster (EKS cluster)
 Install the eksctl tool
   mkdir -p eksctl_download
   curl --silent --location --retry 5 "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C eksctl_download
   chmod +x eksctl_download/eksctl
   SUDO=""
   if [ $(id -u) -ne 0 ] && which sudo > /dev/null ; then
   SUDO="sudo"
   fi
   $SUDO mv eksctl_download/eksctl /usr/local/bin/
   rmdir eksctl_download

4.test5ng the cluster
  
5.deploy the docker image at kubernetes

6.test the deployment
     kubectl get svc
     kubectl get nodes
     kubectl get deployment
     kubectl get pods
     
7.rolling out the app update 

