output "bucket" {
    value =  module.core.bucket
}

output "lambda_arn" {
    value =  module.core.lambda_arn
}

output "apiGatewayUrl" {
  value = module.core.apiGatewayUrl
}