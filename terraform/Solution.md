## Installing Terraform

To get started with Terraform, you'll need to install it on your local machine.

### Using Homebrew (on macOS)
brew tap hashicorp/tap
brew install hashicorp/tap/terraform

Run `terraform init` in system to initialize terraform inside directory 


Working on `terraform.tf` `provider.tf` `ec2.tf`

# Terraform resource configuration file for EC2 instance
```
resource "aws_instance" "example" {
  ami           = "ami-abc123"
  instance_type = "t2.micro"

  vpc_security_group_ids = [aws_security_group.example.id]

  tags = {
    Name        = "My EC2 Instance",
    Environment = var.environment
  }
}

resource "aws_security_group" "example" {
  name        = "My Security Group"
  description = "Allow inbound traffic on port 22 and 80"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] // do not use this, instead refer to AWS documentation for CIDR blocks
  }

  egress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] // do not use this, instead refer to AWS documentation for CIDR blocks
  }
}
```
# Terraform provider configuration file
```
provider "aws" {
  region     = var.environment == "dev" ? "us-west-2" : "us-east-1"
}

data "aws_caller_identity" "current" {}
```
# Terraform output configuration file
```
output "instance_id" {
  value       = aws_instance.example.id
}

output "public_ip" {
  value       = aws_instance.example.public_ip
}

```