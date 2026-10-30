# 기본 계획(enable_iam=false, manage_ec2=false)은 AWS 자원을 만들지 않는다.
# 기존 서버는 EC2 한 대에서 compose.yaml 을 실행한다. RDS, ALB, NAT 는 없다.

data "aws_instance" "current" {
  count       = var.existing_instance_id == "" ? 0 : 1
  instance_id = var.existing_instance_id
}

resource "aws_instance" "app" {
  count         = var.manage_ec2 ? 1 : 0
  ami           = data.aws_ami.ubuntu[0].id
  instance_type = var.instance_type

  metadata_options {
    http_tokens = "required"
  }

  root_block_device {
    volume_type = "gp3"
    volume_size = 30
    encrypted   = true
  }

  tags = {
    Name = "if-v2"
  }
}

data "aws_ami" "ubuntu" {
  count       = var.manage_ec2 ? 1 : 0
  most_recent = true
  owners      = ["099720109477"]

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04-amd64-server-*"]
  }
}
