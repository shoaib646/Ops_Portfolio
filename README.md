# Ops_Portfolio

## **Objective**
The objective of this project is to develop an end-to-end Machine Learning Operations (MLOps) pipeline focused on the domain of **Cybersecurity**. This pipeline leverages **AWS cloud services** for scalable storage and deployment, coupled with a comprehensive local development setup to facilitate experimentation and robust model training workflows.

## **Use Case: Cybersecurity for URL Classification**
In the cybersecurity domain, **URL classification** plays a critical role in identifying malicious websites and protecting users from cyber threats such as phishing, malware, and ransomware. This project focuses on classifying URLs into malicious and benign categories using a machine learning approach.

### Key Challenges Addressed:
1. **Dynamic Nature of Threats**: URLs change frequently, making it challenging to maintain an up-to-date dataset.
2. **Scalability**: Large-scale datasets require robust pipelines for ingestion, validation, and processing.
3. **Performance**: Real-time applications demand models that are both accurate and efficient.

---

## **Agenda**
The following agenda outlines the focus areas of the project:

### **1. Data Security**
- Ensure secure handling of sensitive data using encrypted storage solutions like **MongoDB Atlas**.
- Enable secure data transfer using **AWS S3 buckets** with proper access control policies.

### **2. Feature Engineering and Transformation**
- Perform detailed **Exploratory Data Analysis (EDA)** to identify trends in URL-based features.
- Engineer features critical to classifying URLs, such as domain length, presence of suspicious characters, and WHOIS data.

### **3. Model Development**
- Utilize **XGBoost**, a robust and scalable classifier, to achieve high accuracy and handle class imbalances effectively.
- Conduct hyperparameter tuning to optimize performance metrics like F1 score, precision, and recall.

### **4. Automation Through MLOps**
- Integrate **CI/CD pipelines** using GitHub Actions and Terraform.
- Automate the end-to-end pipeline from data ingestion to model deployment.

### **5. Cloud Scalability**
- Leverage **AWS S3** for scalable artifact storage.
- Deploy and monitor the pipeline using **AWS Lambda** or other serverless architectures (future scope).

---

## **Directory Structure**
```
shoaib646-ops_portfolio/
├── README.md
├── Dockerfile
├── StartTraining.py
├── main.py
├── pushdata.py
├── requirements.txt
├── setup.py
├── .dockerignore
├── Notebook/
│   └── EDA.ipynb
├── airflow/
│   └── dags/
│       └── TrainingPipeline.py
├── networksecurity/
│   ├── cloud/
│   │   ├── __init__.py
│   │   └── s3_syncer.py
│   ├── components/
│   │   ├── DataIngestion.py
│   │   ├── DataTransformation.py
│   │   ├── DataValidation.py
│   │   ├── ModelEvaluation.py
│   │   ├── ModelRegistry.py
│   │   ├── ModelTraining.py
│   │   └── __init__.py
│   ├── constant/
│   │   ├── __init__.py
│   │   └── variables/
│   │       └── __init__.py
│   ├── entity/
│   │   ├── __init__.py
│   │   ├── artifact.py
│   │   └── config.py
│   ├── exception/
│   │   ├── __init__.py
│   │   └── exception.py
│   ├── logger/
│   │   ├── __init__.py
│   │   └── logger.py
│   ├── pipeline/
│   │   ├── TrainingPipeline.py
│   │   └── __init__.py
│   └── utils/
│       ├── __init__.py
│       ├── ML/
│       │   ├── __init__.py
│       │   ├── utils.py
│       │   ├── metric/
│       │   │   ├── __init__.py
│       │   │   └── classification_metric.py
│       │   └── model/
│       │       ├── __init__.py
│       │       └── estimator.py
│       └── Main/
│           ├── __init__.py
│           └── utils.py
└── .github/
    └── workflows/
        └── terraform.yaml
```

---

## **Getting Started**

### **1. Prerequisites**
- **Python 3.10+** installed.
- AWS CLI configured with appropriate credentials.
- Docker installed for containerization.
- MongoDB Atlas account.

### **2. Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/shoaib646/ops_portfolio.git
   cd ops_portfolio
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure environment variables:
   - Create a `.env` file in the root directory with the following:
     ```
     MONGO_URL=<Your MongoDB Connection URL>
     DB_NAME=<Database Name>
     COLLECTION_NAME=<Collection Name>
     AWS_ACCESS_KEY_ID=<Your AWS Access Key>
     AWS_SECRET_ACCESS_KEY=<Your AWS Secret Key>
     AWS_DEFAULT_REGION=<AWS Region>
     ```

### **3. Running the Pipeline**
- **Start Training**:
  ```bash
  python StartTraining.py
  ```
- **Run FastAPI Server**:
  ```bash
  python main.py
  ```
  Access the API documentation at [http://localhost:8000/docs](http://localhost:8000/docs).

---

## **Pipeline Stages**

### **1. Data Ingestion**
- Extract raw data from a CSV file.
- Push the data to MongoDB Atlas.

### **2. Data Validation**
- Validate schema and detect dataset drift.
- Generate validation reports.

### **3. Data Transformation**
- Preprocess data using KNN imputation.
- Generate transformed datasets and save the pipeline.

### **4. Model Training**
- Train the XGBoost classifier.
- Log metrics like F1 score, precision, and recall.

### **5. Model Evaluation**
- Compare the trained model with existing models.
- Log evaluation reports and metrics.

### **6. Model Registry**
- Save the best model to a versioned directory.

### **7. CI/CD Integration**
- Automate deployments with GitHub Actions and Terraform.

---

## **Key Features**
- **Secure Data Handling**: All data transfer operations are encrypted.
- **Scalable Cloud Integration**: Seamless integration with AWS services for artifact storage.
- **Automated MLOps**: Fully automated pipeline for training and deployment.
- **Detailed Logging**: Comprehensive logs for each pipeline stage.

---

## **Future Work**
- Implement real-time URL prediction using a deployed model.
- Enhance feature extraction with additional cybersecurity-specific metrics.
- Integrate AWS Lambda for serverless pipeline execution.

---

For further details or issues, contact **Shoaib Shaikh** at **cruzai.contact@gmail.com**.

