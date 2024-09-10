# Terraform Project for S3, API Gateway, and Lambda

## Overview

This Terraform project sets up the following AWS resources:

- **Amazon S3**: Hosts a static website for the frontend.
- **Amazon API Gateway**: Exposes a Lambda function via HTTP endpoints.
- **AWS Lambda**: Performs text conversion by replacing hardcoded words with predefined values.


## Resources

### S3 Bucket

The S3 bucket is configured to serve a static website. It hosts the frontend application.

- **Bucket Name**: `euwest1-textconverter`
- **S3 endpoint**: `http://euwest1-textconverter.s3-website-eu-west-1.amazonaws.com`

### API Gateway

API Gateway is configured to route HTTP requests to the Lambda function. 


### Lambda Function

The Lambda function performs text conversion:
- **Conversion Logic**: Replaces predefined words with their corresponding values. config is hard coded in Lambda
- **Function Handler**: Defined in `app/backend.src.main.py`.

### TODO

- Implement CDN infront of the S3 for caching
- Implement WAF to protect CDN