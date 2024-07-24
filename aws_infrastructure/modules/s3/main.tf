
resource "aws_s3_bucket" "s3_bucket" {
  bucket        = var.s3_name
  force_destroy = true
  tags = {
    Name = var.s3_name
  }
}

output "s3_id" {
  value = aws_s3_bucket.s3_bucket.id
}