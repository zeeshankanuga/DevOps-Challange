# Banking Application

## Project Overview

This project is a **Banking Application** developed using the **Spring Boot Framework**.  
The application is used to manage banking operations such as customer management and account handling.

The backend database used in this project is **MySQL Server**.  
To ensure consistency across different environments, the application is containerized using **Docker** and deployed on a **Kubernetes Cluster**.

---

# Technology Stack

- Spring Boot
- MySQL
- Docker
- Kubernetes
- Docker Hub
- YAML

---

# Database Details

The project contains the following database tables:

## Customer Table

The `customer` table stores customer-related information such as:

- Customer ID
- Customer Name
- Address
- Mobile Number
- Email

## Account Table

The `account` table stores account-related information such as:

- Account Number
- Account Type
- Account Balance
- Customer ID

---

# Application Services

The project includes the following services:

- Banking Application Service
- MySQL Database Service

A separate service for the MySQL database has been created to establish communication between the application and the database.

---

# Docker Deployment Steps

## 1. Create Docker Image

Create a Docker image of the application using the following command:

```bash
docker build -t bankapp .
```

---

## 2. Tag Docker Image

Tag the Docker image before pushing it to Docker Hub:

```bash
docker tag bankapp zeeshankanuga/bankapp:latest
```

---

## 3. Push Docker Image to Docker Hub

Push the Docker image to Docker Hub:

```bash
docker push zeeshankanuga/bankapp:latest
```

---

# Kubernetes Deployment Steps

## 1. Create Namespace

Create a namespace for the banking application:

```bash
kubectl create namespace bankapp
```

---

## 2. Deploy MySQL Database

Deploy the MySQL database in the Kubernetes cluster:

```bash
kubectl apply -f mysql-deployment.yaml
```

---

## 3. Deploy Persistent Volume and Persistent Volume Claim

Deploy PV and PVC for MySQL database storage:

```bash
kubectl apply -f mysql-pv.yaml
kubectl apply -f mysql-pvc.yaml
```

---

## 4. Deploy ConfigMap and Secret

Deploy ConfigMap and Secret for MySQL configuration:

```bash
kubectl apply -f mysql-configmap.yaml
kubectl apply -f mysql-secret.yaml
```

### ConfigMap

ConfigMap is used to store:

- Database Name
- Database Host
- Application Configuration

### Secret

Secret is used to store sensitive information such as:

- MySQL Username
- MySQL Password

---

## 5. Deploy Banking Application

Deploy the Spring Boot banking application in Kubernetes:

```bash
kubectl apply -f bankapp-deployment.yaml
```

---

## 6. Deploy Service for Front Application

Expose the application using Kubernetes Service:

```bash
kubectl apply -f bankapp-service.yaml
```

---

# Features

- Customer Management
- Account Management
- MySQL Database Integration
- Docker Containerization
- Kubernetes Deployment
- Persistent Data Storage
- Secure Configuration Management

---

# Benefits of Docker and Kubernetes

## Docker

- Consistent application environment
- Easy container management
- Lightweight deployment

## Kubernetes

- Automatic scaling
- Self-healing containers
- Load balancing
- High availability

---

# Conclusion

This Banking Application demonstrates how modern DevOps tools like Docker and Kubernetes can be integrated with a Spring Boot application.

The project provides:

- Scalable deployment
- Secure configuration management
- Persistent database storage
- Containerized architecture

This setup makes the application reliable, portable, and easy to deploy in cloud-native environments.