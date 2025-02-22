# main.tf

# Define AWS provider and set the region
provider "aws" {
  region = "us-east-1"
}

# Define an EC2 instance with a specific AMI and instance type
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"  # Replace with a valid AMI
  instance_type = "t2.micro"               # Smallest AWS instance for cost efficiency

  # Add a tag to identify the instance in AWS console
  tags = {
    Name = "TerraformInstance"
  }
}

