# Capstone (Portfolio) Project

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
  <!-- Access the API documentation at [http://localhost:8000/docs](http://localhost:8000/docs). -->

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

## **About Data**

The provided data appears to be a sample from a dataset used for phishing website detection. Each row in the dataset represents a website, and each column represents a feature or attribute of the website that can be used to determine whether it is legitimate or a phishing attempt. The last column, "Result," indicates whether the website is legitimate (1) or a phishing site (-1). Let's break down each feature:

1. **having_IP_Address**: Indicates whether the URL contains an IP address. Phishing websites often use IP addresses instead of domain names. (-1 indicates presence of IP address, 1 indicates absence).

2. **URL_Length**: The length of the URL. Longer URLs can be a sign of phishing. (1 indicates normal length, -1 indicates suspicious length).

3. **Shortining_Service**: Indicates whether a URL shortening service is used. Phishers often use these services to hide the actual URL. (1 indicates no shortening service, -1 indicates use of shortening service).

4. **having_At_Symbol**: Presence of "@" symbol in the URL. This is uncommon in legitimate URLs. (1 indicates absence, -1 indicates presence).

5. **double_slash_redirecting**: Indicates whether the URL contains "//" after the protocol (http, https). (-1 indicates presence, 1 indicates absence).

6. **Prefix_Suffix**: Indicates whether the domain name includes a hyphen. Phishers often use hyphens to create misleading domain names. (-1 indicates presence, 1 indicates absence).

7. **having_Sub_Domain**: Number of subdomains in the URL. More subdomains can indicate phishing. (-1 indicates many subdomains, 1 indicates few or none).

8. **SSLfinal_State**: Indicates the state of the SSL certificate. Legitimate sites usually have valid SSL certificates. (-1 indicates no SSL or invalid SSL, 1 indicates valid SSL).

9. **Domain_registeration_length**: Length of time the domain has been registered. Phishing sites often have short registration periods. (-1 indicates short registration, 1 indicates long registration).

10. **Favicon**: Indicates whether the favicon is loaded from the same domain. Phishing sites often use external favicons. (1 indicates same domain, -1 indicates different domain).

11. **port**: Indicates whether the URL uses non-standard ports. Phishing sites may use unusual ports. (1 indicates standard ports, -1 indicates non-standard ports).

12. **HTTPS_token**: Presence of "HTTPS" token in the domain part of the URL. Phishers may use this to trick users. (-1 indicates presence, 1 indicates absence).

13. **Request_URL**: Indicates whether the objects (images, scripts, etc.) are loaded from the same domain. Phishing sites often load objects from different domains. (1 indicates same domain, -1 indicates different domains).

14. **URL_of_Anchor**: Indicates whether the anchor tags in the HTML point to the same domain. Phishing sites often use external links. (-1 indicates many external links, 1 indicates few or none).

15. **Links_in_tags**: Indicates whether the meta, script, and link tags point to the same domain. (1 indicates same domain, -1 indicates different domains).

16. **SFH**: Server Form Handler. Indicates where the form data is submitted. Phishing sites often submit data to external domains. (-1 indicates external submission, 1 indicates internal submission).

17. **Submitting_to_email**: Indicates whether the form submits data to an email address. Legitimate sites rarely do this. (-1 indicates presence, 1 indicates absence).

18. **Abnormal_URL**: Indicates whether the URL is abnormal (e.g., not matching the domain name). (-1 indicates abnormal, 1 indicates normal).

19. **Redirect**: Number of redirects. Phishing sites often use multiple redirects. (0 indicates no redirects, 1 indicates one redirect, -1 indicates multiple redirects).

20. **on_mouseover**: Indicates whether the onmouseover event changes the status bar. Phishing sites often use this to hide the actual URL. (1 indicates absence, -1 indicates presence).

21. **RightClick**: Indicates whether right-click is disabled. Phishing sites often disable right-click to prevent users from inspecting elements. (1 indicates enabled, -1 indicates disabled).

22. **popUpWidnow**: Indicates whether pop-up windows are used. Phishing sites often use pop-ups. (1 indicates absence, -1 indicates presence).

23. **Iframe**: Indicates whether iframes are used. Phishing sites often use iframes to hide malicious content. (1 indicates absence, -1 indicates presence).

24. **age_of_domain**: Age of the domain. Older domains are usually more trustworthy. (-1 indicates young domain, 1 indicates old domain).

25. **DNSRecord**: Indicates whether the DNS record is available. Phishing sites often have missing or incomplete DNS records. (-1 indicates missing, 1 indicates available).

26. **web_traffic**: Indicates the amount of web traffic. Legitimate sites usually have more traffic. (-1 indicates low traffic, 1 indicates high traffic).

27. **Page_Rank**: Google's PageRank of the website. Higher PageRank indicates a more trustworthy site. (-1 indicates low PageRank, 1 indicates high PageRank).

28. **Google_Index**: Indicates whether the site is indexed by Google. Phishing sites are often not indexed. (-1 indicates not indexed, 1 indicates indexed).

29. **Links_pointing_to_page**: Number of links pointing to the page. More links usually indicate a more legitimate site. (-1 indicates few links, 1 indicates many links).

30. **Statistical_report**: Indicates whether the site is reported in statistical reports as phishing. (-1 indicates reported, 1 indicates not reported).

31. **Result**: The final classification of the website. (-1 indicates phishing, 1 indicates legitimate).

In the provided sample data, the values for each feature are given for a single website, and the "Result" column indicates that this website is classified as a phishing site (-1).





## **Future Work**
- Implement real-time URL prediction using a deployed model.
- Enhance feature extraction with additional cybersecurity-specific metrics.
- Integrate AWS Lambda for serverless pipeline execution.

---

For further details or issues, contact **Shoaib Shaikh** at **cruzai.contact@gmail.com**.

