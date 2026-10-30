variable "aws_region" {
  type        = string
  description = "기존 배포 리전. deploy.yml 의 AWS_REGION 과 같다."
  default     = "ap-northeast-2"
}

variable "github_repository" {
  type        = string
  description = "OIDC 를 허용할 GitHub 저장소. owner/name."
  default     = "siren8289/IF_v2"
}

variable "existing_instance_id" {
  type        = string
  description = "이미 떠 있는 EC2. 비어 있으면 인스턴스를 조회하거나 만들지 않는다."
  default     = ""
}

variable "account_id" {
  type        = string
  description = "IAM ARN 에 쓸 계정 번호. enable_iam 이 false 이면 사용하지 않는다."
  default     = ""
}

variable "enable_iam" {
  type        = bool
  description = "true 면 GitHub OIDC 역할과 최소 SSM 권한을 만든다. 승인 없이 켜지 않는다."
  default     = false
}

variable "manage_ec2" {
  type        = bool
  description = "true 면 새 EC2 를 만든다. 기존 서버를 바꾸지 않도록 기본값은 false."
  default     = false
}

variable "instance_type" {
  type        = string
  description = "manage_ec2 를 켠 경우에만 쓰는 크기. 현재 서버 크기는 이 저장소에 없다."
  default     = "t3.small"
}
