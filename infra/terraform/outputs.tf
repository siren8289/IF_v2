output "apply_creates_resources" {
  description = "기본 변수가 그대로면 false 다. AWS 호출로 자원을 만들지 않는다."
  value       = var.enable_iam || var.manage_ec2
}

output "deploy_role_name" {
  description = "enable_iam 이 켜진 계획에서만 역할 이름이 있다."
  value       = try(aws_iam_role.deploy[0].name, null)
}

output "recorded_instance_id" {
  description = "조회만 한다. 인스턴스를 바꾸지 않는다."
  value       = var.existing_instance_id == "" ? null : var.existing_instance_id
}
