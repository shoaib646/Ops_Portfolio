# Work Breakdown Structure (WBS) for Capstone Project

## 1. Project Management
- **1.1 Project Initiation**
  - Define project objectives and scope.
  - Identify stakeholders.
- **1.2 Project Planning**
  - Develop project timeline and milestones.
  - Perform risk assessment and mitigation planning.
- **1.3 Documentation**
  - Maintain README and project documentation.
  - Record meeting notes and decisions.

## 2. Environment Setup & Configuration
- **2.1 System Setup**
  - Install Python 3.10+, Docker, and AWS CLI.
  - Set up local development environment.
- **2.2 Dependency Management**
  - Install dependencies using `pip install -r requirements.txt`.
- **2.3 Configuration**
  - Create a `.env` file with MongoDB Atlas and AWS credentials.
  - Configure environment variables (`MONGO_URL`, `DB_NAME`, `COLLECTION_NAME`, etc.).

## 3. Data Pipeline Development
- **3.1 Data Ingestion**
  - Extract data from CSV using pushdata.py.
  - Convert CSV to JSON and push records to MongoDB Atlas.
  - Validate file existence and data integrity before insertion.
- **3.2 Data Validation**
  - Validate data schema.
  - Detect anomalies and dataset drift.
  - Generate data validation reports.
- **3.3 Data Transformation**
  - Apply pre-processing (e.g. KNN imputation and feature engineering).
  - Prepare transformed datasets for training.

## 4. Model Development & Evaluation
- **4.1 Model Training**
  - Configure and train XGBoost classifier.
  - Perform hyperparameter tuning.
- **4.2 Model Evaluation**
  - Evaluate model performance against benchmarks.
  - Log metrics (F1 score, precision, recall) and generate evaluation reports.
- **4.3 Model Registry**
  - Save and version the best-performing model.
  - Maintain an organized model registry.

## 5. Deployment & CI/CD Integration
- **5.1 Deployment Preparation**
  - Containerize the application using Docker.
  - Plan AWS deployment (integrate AWS Lambda for serverless execution).
- **5.2 CI/CD Pipeline**
  - Set up CI/CD using GitHub Actions and Terraform.
  - Integrate automated testing.
- **5.3 Monitoring & Logging**
  - Implement detailed logging (using networksecurity/logger/logger.py).
  - Set up monitoring for deployed services.

## 6. Cloud Integration & AWS Services
- **6.1 MongoDB Atlas Integration**
  - Use pushdata.py to ingest initial CSV data into MongoDB Atlas.
- **6.2 AWS Services Integration**
  - Configure AWS S3 for scalable artifact and data storage.
  - Prepare AWS Lambda (or similar) for deployment of the pipeline in a serverless manner.
- **6.3 Security & Compliance**
  - Secure data transfer between local system, MongoDB Atlas, and AWS services.
  - Implement access control and credential management.

## 7. Post-Deployment & Future Enhancements
- **7.1 Performance Monitoring**
  - Continuously monitor model performance.
- **7.2 Scalability Enhancements**
  - Expand integration with AWS S3, Lambda, and possibly API Gateway.
- **7.3 Future Work**
  - Implement real-time URL prediction.
  - Enhance feature extraction with additional cybersecurity-specific metrics.

---

# Project Workflow

Below is a high-level workflow diagram for the end-to-end pipeline:

```mermaid
graph LR
    A[Data Ingestion via pushdata.py] --> B[Data Validation]
    B --> C[Data Transformation]
    C --> D[Model Training (XGBoost)]
    D --> E[Model Evaluation & Registry]
    E --> F[CI/CD Integration (GitHub Actions & Terraform)]
    F --> G[Deployment Preparation]
    G --> H[AWS Services Integration]
    H --> I[Deployment to AWS (Lambda/S3)]
```

**Workflow Details:**

1. **Data Ingestion via pushdata.py**  
   - Load CSV using pushdata.py.
   - Convert CSV data to JSON and push to MongoDB Atlas.
   - Log the successful insertion of records.

2. **Data Validation**  
   - Validate the ingested data to ensure correctness and integrity.

3. **Data Transformation**  
   - Preprocess and transform the data for model training.

4. **Model Training (XGBoost)**  
   - Train the XGBoost classifier using the processed data.
   - Tune hyperparameters and log training metrics.

5. **Model Evaluation & Registry**  
   - Evaluate the new model against benchmarks.
   - Save the best-performing model in a versioned registry.

6. **CI/CD Integration**  
   - Integrate automated tests and deployment using GitHub Actions and Terraform pipelines.

7. **Deployment Preparation & AWS Services Integration**  
   - Containerize the application.
   - Utilize AWS S3 for storage and configure AWS Lambda for serverless execution.
   - Ensure secure communication between components.

8. **Final Deployment**  
   - Deploy the complete pipeline, making the model available for inference and monitoring.
