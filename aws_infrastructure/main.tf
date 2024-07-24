terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = var.region
}

module "s3_bucket" {
  source = "./modules/s3"

}

resource "aws_s3_object" "mlflow_artifacts" {
  bucket       = module.s3_bucket.s3_id
  key          = "mlflow/"
  content_type = "application/x-directory"
  content      = ""
}


resource "aws_s3_object" "historical_data" {
  bucket       = module.s3_bucket.s3_id
  key          = "historical/"
  content_type = "application/x-directory"
  content      = ""
}