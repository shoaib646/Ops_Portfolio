terraform {
  backend "s3" {
    bucket = "security-tf-state"
    key    = "tf_state"
    region = "ap-south-1"
  }
}

module "security_ec2" {
  source = "./security_ec2"
}

module "security_model" {
  source = "./security_model_bucket"
}

module "security_ecr" {
  source = "./security_ecr"
}

module "security_pred_data" {
  source = "./security_pred_data_bucket"
}