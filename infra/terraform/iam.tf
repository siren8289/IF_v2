data "tls_certificate" "github" {
  count = var.enable_iam ? 1 : 0
  url   = "https://token.actions.githubusercontent.com"
}

resource "aws_iam_openid_connect_provider" "github" {
  count           = var.enable_iam ? 1 : 0
  url             = "https://token.actions.githubusercontent.com"
  client_id_list  = ["sts.amazonaws.com"]
  thumbprint_list = [data.tls_certificate.github[0].certificates[0].sha1_fingerprint]
}

data "aws_iam_policy_document" "github_trust" {
  count = var.enable_iam ? 1 : 0

  statement {
    actions = ["sts:AssumeRoleWithWebIdentity"]

    principals {
      type        = "Federated"
      identifiers = [aws_iam_openid_connect_provider.github[0].arn]
    }

    condition {
      test     = "StringEquals"
      variable = "token.actions.githubusercontent.com:aud"
      values   = ["sts.amazonaws.com"]
    }

    condition {
      test     = "StringLike"
      variable = "token.actions.githubusercontent.com:sub"
      values   = ["repo:${var.github_repository}:ref:refs/heads/main"]
    }
  }
}

resource "aws_iam_role" "deploy" {
  count              = var.enable_iam ? 1 : 0
  name               = "if-v2-gha-deploy"
  assume_role_policy = data.aws_iam_policy_document.github_trust[0].json
}

data "aws_iam_policy_document" "deploy" {
  count = var.enable_iam ? 1 : 0

  statement {
    sid = "ReadCaller"
    actions = [
      "sts:GetCallerIdentity",
    ]
    resources = ["*"]
  }

  statement {
    sid = "SeeThisInstance"
    actions = [
      "ssm:DescribeInstanceInformation",
    ]
    resources = ["*"]
  }

  statement {
    sid = "CommandThisInstanceOnly"
    actions = [
      "ssm:SendCommand",
    ]
    resources = [
      "arn:aws:ec2:${var.aws_region}:${var.account_id}:instance/${var.existing_instance_id}",
      "arn:aws:ssm:${var.aws_region}::document/AWS-RunShellScript",
    ]
  }

  statement {
    sid = "ReadOwnCommand"
    actions = [
      "ssm:GetCommandInvocation",
      "ssm:ListCommandInvocations",
      "ssm:CancelCommand",
    ]
    resources = [
      "arn:aws:ssm:${var.aws_region}:${var.account_id}:*",
    ]
  }
}

resource "aws_iam_role_policy" "deploy" {
  count  = var.enable_iam ? 1 : 0
  name   = "if-v2-ssm-deploy"
  role   = aws_iam_role.deploy[0].id
  policy = data.aws_iam_policy_document.deploy[0].json
}
