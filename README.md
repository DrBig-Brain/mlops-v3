# End-to-End Streaming MLOps System for NYC Taxi Fare Prediction

## Problem Statement

Ride-hailing platforms require fast and accurate fare estimation to provide users with price transparency before booking a ride. Traditional machine learning projects often focus only on model training and overlook the challenges of deploying, monitoring, and maintaining models in production.

This project aims to build a production-ready MLOps system capable of training, deploying, monitoring, and continuously improving an XGBoost-based taxi fare prediction model. The system supports real-time inference, automated retraining, experiment tracking, model versioning, and cloud deployment while demonstrating modern MLOps best practices.

---

## Input

The prediction service accepts taxi ride information as input, including:

* Pickup Latitude
* Pickup Longitude
* Dropoff Latitude
* Dropoff Longitude
* Pickup Date & Time
* Passenger Count

Derived features:

* Trip Distance
* Hour of Day
* Day of Week
* Month
* Weekend Indicator

The system also receives continuous streaming ride requests for real-time inference.

---

## Output

The system returns:

* Estimated Taxi Fare
* Prediction Timestamp
* Model Version
* Request ID
* Prediction Latency

Additionally, the platform stores:

* Prediction Logs
* Performance Metrics
* Model Artifacts
* Drift Reports
* Experiment Metadata

---

## Pipeline

1. Data Ingestion

   * Load NYC Taxi dataset
   * Validate incoming records

2. Data Preprocessing

   * Handle missing values
   * Remove outliers
   * Feature engineering
   * Data validation

3. Model Training

   * Train XGBoost regression model
   * Hyperparameter tuning
   * Performance evaluation

4. Experiment Tracking

   * Log parameters
   * Log metrics
   * Store trained models using MLflow

5. Model Deployment

   * Register best-performing model
   * Serve model using FastAPI

6. Real-Time Prediction

   * Receive API requests
   * Generate fare prediction
   * Log predictions

7. Monitoring

   * Collect API metrics
   * Monitor latency and request volume
   * Visualize dashboards using Grafana

8. Drift Detection

   * Compare incoming data distribution with training data
   * Detect feature drift
   * Trigger retraining when required

9. Automated Retraining

   * Airflow executes scheduled training pipeline
   * Register newly trained model
   * Deploy latest production model

---

## Architecture

Client
↓
FastAPI REST API
↓
Prediction Service
↓
MLflow Model Registry
↓
XGBoost Model

Training Pipeline

NYC Taxi Dataset
↓
Data Validation
↓
Feature Engineering
↓
Model Training
↓
MLflow Tracking
↓
Model Registry

Monitoring

FastAPI
↓
Prometheus Metrics
↓
Grafana Dashboard

Automation

Airflow
↓
Scheduled Retraining
↓
Model Registration

Cloud Infrastructure

AWS EC2
AWS S3
AWS Lambda (optional)
AWS Kinesis (optional)
Docker Containers

---

## Tech Stack

### Machine Learning

* Python
* XGBoost
* Pandas
* NumPy
* Scikit-learn

### Backend

* FastAPI
* Uvicorn
* Pydantic

### MLOps

* MLflow
* Apache Airflow
* Docker

### Monitoring

* Prometheus
* Grafana

### Cloud

* AWS EC2
* AWS S3
* AWS Lambda
* AWS Kinesis (Streaming)

### Infrastructure

* Terraform
* Docker Compose

### Development

* Git
* GitHub
* Pytest
* GitHub Actions

---

## Expected Features

### Machine Learning

* Data preprocessing pipeline
* Feature engineering
* XGBoost regression model
* Automated evaluation
* Model versioning

### API

* REST API for predictions
* Request validation
* Exception handling
* Health check endpoint
* Interactive Swagger documentation

### MLOps

* MLflow experiment tracking
* Model Registry
* Automated retraining
* Airflow DAG scheduling
* Drift detection

### Monitoring

* API latency monitoring
* Request throughput
* Error rate monitoring
* Resource utilization
* Prediction logging

### Deployment

* Dockerized services
* Cloud deployment on AWS
* Infrastructure as Code using Terraform

### Future Improvements

* Real-time Kafka/Kinesis streaming
* Canary model deployment
* A/B model testing
* Feature Store integration
* Kubernetes deployment
* CI/CD pipeline for automatic deployment
