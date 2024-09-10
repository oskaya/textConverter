include {
  path = find_in_parent_folders()
}

generate "providers" {
  path = "providers.tf"
  if_exists = "overwrite_terragrunt"
  contents = <<EOF
terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "~> 4"
    }
  }
}
provider "aws" {
  region = "eu-west-1"
  default_tags {
    tags = {
      Environment = "Test"
      CreatedBy   = "oskaya@windowslive.com"
      Project     = "TextConvert"
    }
  }
}
EOF
}