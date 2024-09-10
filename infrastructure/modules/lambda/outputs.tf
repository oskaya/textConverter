output "lambda_arn" {
  value = aws_lambda_function.lambda.arn
}

output "lambdaInvokeArn" {
  value = aws_lambda_function.lambda.invoke_arn
}

output lambdaFunctionName {
  value = aws_lambda_function.lambda.function_name
}