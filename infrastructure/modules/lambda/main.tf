data "aws_iam_policy_document" "assume_role" {
  statement {
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }

    actions = ["sts:AssumeRole"]
  }
}

data "aws_iam_policy_document" "lambda_logging" {
  statement {
    effect = "Allow"

    actions = [
      "logs:CreateLogGroup",
      "logs:CreateLogStream",
      "logs:PutLogEvents",
    ]

    resources = ["arn:aws:logs:*:*:*"]
  }
}
resource "aws_iam_role" "iam_for_lambda" {
  name               = var.lambda_role
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
}

resource "aws_iam_role_policy" "lambda_logging_policy" {
  name   = "${var.lambda_role}_logging"
  role   = aws_iam_role.iam_for_lambda.id
  policy = data.aws_iam_policy_document.lambda_logging.json
}

data "archive_file" "lambda" {
  type        = "zip"
  source_dir= "${path.module}/../../../app/backend/src"
  output_path = "lambda_function_payload.zip"
}

resource "aws_lambda_function" "lambda" {
  filename      = "lambda_function_payload.zip"
  function_name = var.function_name
  role          = aws_iam_role.iam_for_lambda.arn
  handler       = "main.lambda_handler"
  architectures = ["arm64"]
  source_code_hash = data.archive_file.lambda.output_base64sha256
  timeout = 10
  runtime = "python3.10"
  environment {
    variables = {
      LOG_LEVEL = var.LOG_LEVEL
    }
  }
}








