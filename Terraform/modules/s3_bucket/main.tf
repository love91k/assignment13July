resource "aws_s3_bucket" "mybucket" {
   bucket =  "${var.bucket_name}"
   acl = "private"
   versioning {
      enabled = false
   }
}

resource "aws_s3_bucket_object" "s3_folder" {
    bucket   = aws_s3_bucket.mybucket.id
    acl      = "private"
    key      = "${var.folder_name}"
}
