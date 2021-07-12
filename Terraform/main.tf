terraform {
  required_version = ">= 0.12"
}

provider "aws" {
  region = var.aws_region
}


module "s3_bucket" {
  source = "./modules/s3_bucket"
  bucket_name = var.bucket_name
  folder_name = var.folder_name
}

