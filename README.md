# Automated Data Lineage and Impact Analysis for ML Pipelines

## Team 13 Project Report

---

# Abstract

Modern machine learning systems continuously evolve due to changes in datasets, feature engineering processes, and model retraining workflows. As ML systems become more complex, organizations face major challenges in tracking dataset evolution, reproducing experiments, understanding dependencies between datasets and models, and analyzing the downstream impact of upstream changes.

This project proposes an end-to-end automated data lineage and impact analysis framework using Apache Airflow, MLflow, and DVC. The system automates the ML workflow, tracks dataset versions, records machine learning experiments, stores lineage metadata, and identifies downstream models affected by data modifications.

The framework improves traceability, reproducibility, governance, and automation in machine learning pipelines. A Customer Churn dataset is used to demonstrate the complete workflow including dataset versioning, preprocessing, model training, experiment tracking, lineage storage, and impact analysis.

---

# 1. Introduction

Machine Learning pipelines involve multiple stages such as data ingestion, preprocessing, feature engineering, model training, evaluation, deployment, and monitoring. In real-world systems, datasets and models change frequently due to updates in business requirements and incoming data.

Managing these changes manually becomes difficult because:

- Dataset versions are hard to track
- Model reproducibility becomes challenging
- Dependencies between datasets and models are unclear
- Downstream impact of data changes is unknown
- Experiment history is difficult to maintain

Data lineage helps solve these problems by tracking the complete lifecycle of data from source to final output. Similarly, impact analysis helps identify downstream systems affected by upstream modifications.

This project implements a simplified but effective MLOps framework to automate lineage tracking and dependency analysis using modern tools such as Apache Airflow, MLflow, and DVC.

---

# 2. Problem Statement

In traditional machine learning workflows:

- Dataset changes are not tracked properly
- Different experiment versions are difficult to reproduce
- There is no centralized metadata management
- Teams cannot easily identify which models depend on which datasets
- Pipeline execution is often manual
- Debugging and governance become difficult

Without proper lineage tracking and automation, ML systems become unreliable and difficult to maintain.

The objective of this project is to design a system that:

- Tracks dataset versions automatically
- Automates ML pipeline execution
- Records machine learning experiments
- Maintains lineage metadata
- Performs impact analysis for downstream dependencies

---

# 3. Objectives

The main objectives of the project are:

1. Build an end-to-end machine learning pipeline
2. Implement dataset versioning using DVC
3. Automate workflow orchestration using Apache Airflow
4. Track machine learning experiments using MLflow
5. Store lineage metadata in SQLite
6. Perform downstream impact analysis
7. Improve reproducibility and traceability
8. Demonstrate ML governance concepts

---

# 4. Scope of the Project

The scope of the project includes:

- Dataset tracking and version control
- Data preprocessing automation
- Model training automation
- Experiment metadata tracking
- Lineage metadata generation
- Dependency mapping
- Impact analysis reporting

The project focuses on demonstrating MLOps concepts rather than building a production-scale platform.

---

# 5. Tools and Technologies Used

| Tool / Technology | Purpose |
|---|---|
| Python | Programming language |
| Apache Airflow | Workflow orchestration |
| MLflow | Experiment tracking |
| DVC | Dataset versioning |
| Scikit-learn | Machine learning algorithms |
| SQLite | Metadata storage |
| Pandas | Data preprocessing |
| Git | Source code version control |
| VS Code | Development environment |

---

# 6. System Architecture

The system architecture consists of multiple integrated components.

```text
Customer Churn Dataset
           ↓
DVC Dataset Versioning
           ↓
Apache Airflow Pipeline
           ↓
Data Preprocessing
           ↓
Feature Engineering
           ↓
Model Training
           ↓
MLflow Experiment Tracking
           ↓
Lineage Metadata Storage
           ↓
Impact Analysis Report
```

---

# 7. Dataset Description

The project uses the Customer Churn dataset.

Dataset Source:
https://www.kaggle.com/datasets/blastchar/telco-customer-churn

The dataset contains customer information such as:

- Customer demographics
- Internet services
- Payment methods
- Contract information
- Monthly charges
- Churn status

Target Variable:

- Churn

The dataset is suitable because:

- It contains multiple features
- It supports classification tasks
- It is easy to preprocess
- It demonstrates lineage clearly

---

# 8. Methodology

The implementation methodology is divided into multiple stages.

## 8.1 Dataset Versioning using DVC

DVC (Data Version Control) is used to track dataset versions similarly to Git.

Steps performed:

1. Initialize Git repository
2. Initialize DVC
3. Add dataset to DVC
4. Track metadata files in Git

Commands used:

```bash
git init
```

```bash
dvc init
```

```bash
dvc add data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv
```

Advantages:

- Dataset reproducibility
- Dataset lineage tracking
- Version comparison
- Collaboration support

---

## 8.2 Data Preprocessing

The preprocessing stage performs:

- Missing value removal
- Data cleaning
- Processed dataset generation

The cleaned dataset is stored inside:

```text
data/processed/cleaned.csv
```

Preprocessing improves:

- Data quality
- Training consistency
- Model accuracy

---

## 8.3 Machine Learning Model Training

The project uses a Random Forest Classifier.

Training stages:

1. Dataset loading
2. Label encoding
3. Train-test split
4. Model training
5. Prediction generation
6. Accuracy calculation

Evaluation Metric:

- Accuracy Score

The model is trained using Scikit-learn.

---

## 8.4 Experiment Tracking using MLflow

MLflow is used to track:

- Experiment runs
- Hyperparameters
- Accuracy metrics
- Model artifacts
- Model metadata

The following items are logged:

- Model name
- Accuracy
- Experiment ID
- Run ID
- Model artifact

Benefits:

- Experiment reproducibility
- Centralized tracking
- Model comparison
- Easy debugging

---

## 8.5 Workflow Automation using Apache Airflow

Apache Airflow automates the execution of ML pipeline tasks.

The Airflow DAG contains:

1. Preprocessing task
2. Training task
3. Lineage tracking task

Pipeline Flow:

```text
Preprocess Data
       ↓
Train Model
       ↓
Store Lineage Metadata
```

Airflow provides:

- Workflow scheduling
- Task dependency management
- Monitoring interface
- DAG visualization

---

## 8.6 Lineage Metadata Tracking

Lineage metadata is stored using SQLite.

Metadata includes:

| Dataset Version | Processed File | Model | Accuracy |
|---|---|---|---|
| v1 | cleaned.csv | RandomForest | 0.85 |

The metadata table helps identify:

- Which model used which dataset
- Which transformations were applied
- Which experiments correspond to each dataset version

---

## 8.7 Impact Analysis

Impact analysis identifies downstream systems affected by upstream changes.

Example:

If dataset version changes:

```text
Dataset v1 → Dataset v2
```

Affected components:

- Processed datasets
- Feature transformations
- Machine learning models
- Experiment runs

Recommended action:

```text
Retrain affected models
```

This improves:

- Governance
- Reliability
- Pipeline maintenance

---

# 9. Project Folder Structure

```text
team13_project/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── preprocess.py
│   ├── train.py
│   ├── lineage.py
│   └── impact_analysis.py
│
├── airflow_dags/
│   └── pipeline.py
│
├── metadata/
│   └── lineage.db
│
├── models/
├── screenshots/
├── reports/
│
├── requirements.txt
└── README.md
```

---

# 10. Implementation Details

## 10.1 Preprocessing Script

The preprocessing script:

- Reads raw dataset
- Removes missing values
- Generates cleaned dataset

Output:

```text
cleaned.csv
```

---

## 10.2 Training Script

The training script performs:

- Data encoding
- Train-test splitting
- Random Forest training
- Accuracy evaluation
- MLflow logging

Output:

- Accuracy score
- Trained model
- Experiment metadata

---

## 10.3 Lineage Script

The lineage script:

- Creates SQLite database
- Creates lineage table
- Inserts lineage metadata

Output:

```text
lineage.db
```

---

## 10.4 Impact Analysis Script

The impact analysis script:

- Detects dataset version changes
- Identifies affected models
- Recommends retraining

Sample Output:

```text
Dataset version changed
Affected Model: RandomForest
Recommended Action: Retrain Model
```

---

# 11. Results and Outputs

The project successfully demonstrates:

- Dataset version tracking using DVC
- Automated pipeline orchestration using Airflow
- Experiment tracking using MLflow
- Lineage metadata storage
- Impact analysis reporting

Generated Outputs:

1. DVC-tracked dataset
2. MLflow experiment logs
3. Airflow DAG execution
4. SQLite lineage database
5. Impact analysis report

---

# 12. Advantages of the System

The proposed system provides several advantages:

## 12.1 Reproducibility

Every dataset version and experiment can be reproduced.

## 12.2 Automation

Airflow automates pipeline execution.

## 12.3 Traceability

Lineage metadata improves tracking of dependencies.

## 12.4 Governance

Impact analysis improves ML governance.

## 12.5 Experiment Management

MLflow maintains centralized experiment tracking.

---

# 13. Limitations

Current limitations include:

- Small-scale implementation
- Local environment only
- No cloud deployment
- Basic impact analysis
- Single dataset usage
- Limited visualization

---

# 14. Future Enhancements

Possible future improvements:

- Real-time lineage tracking
- Cloud integration (AWS/GCP/Azure)
- Kubernetes deployment
- CI/CD integration
- Advanced dashboard visualization
- Automated retraining triggers
- Feature store integration
- Graph-based lineage visualization

---

# 15. Applications

The proposed framework can be applied in:

- Banking systems
- Healthcare analytics
- Recommendation systems
- Fraud detection systems
- Telecom analytics
- E-commerce platforms
- Enterprise MLOps systems

---

# 16. Conclusion

This project successfully demonstrates an automated data lineage and impact analysis framework for machine learning pipelines using Apache Airflow, MLflow, and DVC.

The framework automates machine learning workflows, tracks dataset versions, records experiment metadata, stores lineage information, and identifies downstream impacts caused by data modifications.

The system improves reproducibility, traceability, governance, and automation in ML pipelines. Even though the implementation is simplified, it effectively demonstrates important MLOps concepts used in modern machine learning systems.

The project provides a strong foundation for scalable and production-level lineage management systems.

---

# References

1. Apache Airflow Documentation
https://airflow.apache.org/

2. MLflow Documentation
https://mlflow.org/

3. DVC Documentation
https://dvc.org/

4. Scikit-learn Documentation
https://scikit-learn.org/

5. Customer Churn Dataset
https://www.kaggle.com/datasets/blastchar/telco-customer-churn

6. Pandas Documentation
https://pandas.pydata.org/

7. SQLite Documentation
https://www.sqlite.org/docs.html

