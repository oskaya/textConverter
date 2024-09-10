module s3_static_website {
    source = "./modules/s3-static-web-site"
    bucket = "euwest1-textconverter"
    apiGatewayUrl = module.apiGateway.api_gateway_url
}

module lambda {
    source = "./modules/lambda" 
    function_name = "textConverter"
    lambda_role = "textConverterLambda"
}


module "apiGateway" {
    source = "./modules/api-gateway"
    apiGatewayName = "textConverter"
    resourcePath = "POST /convert"
    integratedLambdaInvokeArn = module.lambda.lambdaInvokeArn
    lambdaFuctionName = module.lambda.lambdaFunctionName
}