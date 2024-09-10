output bucket {
    value = module.s3_static_website.bucket
}

output "lambda_arn" {
  value = module.lambda.lambda_arn
}

output lambdaFunctionName {
  value = module.lambda.lambdaFunctionName
}

output "apiGatewayUrl" {
  value = module.apiGateway.api_gateway_url
}