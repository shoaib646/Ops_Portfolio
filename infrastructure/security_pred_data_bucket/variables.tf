variable "aws_region" {
  type    = string
  default = "ap-south-1"
}

variable "pred_data_bucket_name" {
  type    = string
  default = "security-datasource"
}

variable "aws_account_id" {
  type    = string
  default = "020261525478"
}

variable "force_destroy_bucket" {
  type    = bool
  default = true
}
