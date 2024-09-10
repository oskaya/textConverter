resource "aws_s3_bucket" "static_website" {
  bucket = var.bucket
}

resource "aws_s3_bucket_policy" "bucket_policy" {
  bucket = aws_s3_bucket.static_website.bucket
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect    = "Allow"
        Principal = "*"
        Action    = "s3:GetObject"
        Resource  = "${aws_s3_bucket.static_website.arn}/*"
      }
    ]
  })
}

resource "aws_s3_object" "index" {
  key                    = "index.html"
  bucket                 = aws_s3_bucket.static_website.id
  source                 = "${path.module}/../../../app/frontend/src/index.html"
  content_type           = "text/html" 
  depends_on             = [aws_s3_bucket_policy.bucket_policy]

}



resource "aws_s3_bucket_public_access_block" "public" {
  bucket = aws_s3_bucket.static_website.id
  block_public_acls       = true
  block_public_policy     = false
  ignore_public_acls      = true
  restrict_public_buckets = false
}

resource "aws_s3_bucket_website_configuration" "static_website" {
  bucket = aws_s3_bucket.static_website.id

  index_document {
    suffix = "index.html"
  }

  error_document {
    key = "error.html"
  }
}