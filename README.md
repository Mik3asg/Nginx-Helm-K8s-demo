# Deploying Dual Nginx Instances with Helm on Minikube

## Overview

This guide covers:

- Setting up a Minikube Kubernetes cluster
- Manually creating a Helm chart to deploy two Nginx instances
- Automating the deployment process using a Python script
- Testing and accessing the deployed Nginx instances

## Prerequisites

- Minikube installed
- Helm installed
- NGINX Ingress Controller enabled:
  - `minikube addons enable ingress`
  - `kubectl get pods -n ingress-nginx`

## Steps

### 1. Set up Minikube
- Start Minikube cluster: `minikube start`
- Verify it is running: `minikube status`

---

### 2. Manually create Helm chart
#### Create a new Project directory and Helm Chart structure:
- Create a new project directory: `mkdir multi_nginx_instances_demo`
- Create the directory structure as follows:
  ```bash
  ~/multi_nginx_instances_helm_demo$ tree
  .
  └── nginx-instances
      ├── Chart.yaml
      ├── templates
      │   ├── deployment.yaml
      │   ├── ingress.yaml
      │   └── service.yaml
      └── values.yaml

  2 directories, 5 files
  ``` 
#### Configure Helm template files
- Populate template files: `deployment.yaml`, `service.yaml`, `ingress.yaml` as per provided configuration files
- Configure `values.yaml` and `Chart.yaml`

#### Create a new namespace 
- Create a new `nginx-instances-helm` namespace and switch minikube context to newly created namespace:
  ```bash
  kubectl create namespace nginx-instances-helm
  kubectl config set-context --current --namespace=nginx-instances-helm

#### Install the Helm Chart
- Run `helm install first-release ./nginx-instances`
    - Note - usage: `helm install [NAME] [CHART]`

#### Verify deployment

- Check helm release status: `helm list`
- Verify deployed resources using:
  ```bash
  kubectl get deployment
  kubectl get pods
  kubectl get service
  kubectl get ingress
  ```
#### Create local DNS entries

- Lookup the external IP address as reported by minikube
  ```bash
  minikube ip
  192.168.49.2 # <!-- Please use your Minikube IP -->
  ```
- Edit the `/etc/hosts` file with `sudo vi /etc/hosts`
- Add the following DNS entries
  ```bash
  192.168.49.3    customer100.example.com
  192.168.49.2    customer200.example.com
  ```

#### Test solution
- Access Nginx instances via ingress hostnames and Test with `curl` or web browser
  -  `curl http://customer100.example.com`
  -  `curl http://customer200.example.com`

#### Cleanup

- Delete Helm release: `helm uninstall <release_name>`

---
### 3. Automate Helm chart deployment
We've created an 'automation' directory housing a script named `helm-install-script.py`. 
Our task involves using the helm files, previously manually created and stored in the 'nginx-instances/' directory as per the directory structure provided.

The purpose of the script is to read the helm files from the 'nginx-instances' directory and subsequently deploy the nginx resources (including deployment, service, ingress).
However, in case of deletion or upgrades of the helm resources, we'll rely on the helm CLI.   
  
#### Create a directory for hosting script

Here's the directory structure for reference:
```bash
~/multi_nginx_instances_helm_demo$ tree
.
├── automation
│   └── helm-install-script.py
└── nginx-instances
    ├── Chart.yaml
    ├── templates
    │   ├── deployment.yaml
    │   ├── ingress.yaml
    │   └── service.yaml
    └── values.yaml

3 directories, 6 files
```
- Create `automation/` directory in `~/multi_nginx_instances_helm_demo`
- Create `helm-install-script.py` script under `automation/` directory and populated it as per the script provided 
- Run script to deploy chart 
  ```bash
  python3 helm-install-script.py <chart_dir> <release_name>
  ```

#### Verify deployment

- Check helm release status: `helm list`
- Verify deployed resources using:
  ```bash
  kubectl get deployment
  kubectl get pods
  kubectl get service
  kubectl get ingress
  ```

#### Test solution
- Access Nginx instances via ingress hostnames and Test with `curl` or web browser
  -  `curl http://customer100.example.com`
  -  `curl http://customer200.example.com`

#### Cleanup

- Delete Helm release: `helm uninstall <release_name>`

## Summary

This guide showed manual Helm chart creation and automated deployment of multiple Nginx services on Kubernetes.
