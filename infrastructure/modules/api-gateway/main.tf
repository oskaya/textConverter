resource "aws_apigatewayv2_api" "http" {
  name          = var.apiGatewayName
  protocol_type = "HTTP"
  cors_configuration {
    allow_origins = toset(["*"])
    allow_headers = ["content-type"]
    allow_methods = toset(["*"])
  }
}

resource "aws_apigatewayv2_route" "convert" {
  api_id    = aws_apigatewayv2_api.http.id
  route_key = var.resourcePath
   target = "integrations/${aws_apigatewayv2_integration.lambda.id}"
}

resource "aws_apigatewayv2_integration" "lambda" {
  api_id           = aws_apigatewayv2_api.http.id  
  integration_type = "AWS_PROXY"
  connection_type           = "INTERNET"
  payload_format_version    = "2.0"
  integration_method        = "POST"
  integration_uri           = var.integratedLambdaInvokeArn
  
}

resource "aws_lambda_permission" "apigw" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = var.lambdaFuctionName
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_apigatewayv2_api.http.execution_arn}/*/*"
}

resource "aws_apigatewayv2_stage" "stage" {
  api_id = aws_apigatewayv2_api.http.id
  name   = "$default"
  auto_deploy = true
}

resource "aws_apigatewayv2_deployment" "example" {
  api_id      = aws_apigatewayv2_api.http.id
  description = "Example deployment"

  lifecycle {
    create_before_destroy = true
  }
}




