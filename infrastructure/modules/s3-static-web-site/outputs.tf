output bucket {
    value = { "bucket_name" :aws_s3_bucket.static_website.bucket,
               "s3httpendpoint": "http://${aws_s3_bucket_website_configuration.static_website.website_endpoint}" 
            }
}