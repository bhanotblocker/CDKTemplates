# IAM Permissions for Redshift Data Warehouse Deployment

This document outlines the necessary IAM permissions required for deploying the Redshift Data Warehouse stack using AWS CDK.

## 1. **Redshift Permissions**
The following permissions are required to manage the Amazon Redshift cluster:

- `redshift:CreateCluster`
- `redshift:DeleteCluster`
- `redshift:DescribeClusters`
- `redshift:ModifyCluster`
- `redshift:AuthorizeClusterSecurityGroupIngress`
- `redshift:RevokeClusterSecurityGroupIngress`
- `redshift:AuthorizeSnapshotAccess`
- `redshift:RevokeSnapshotAccess`

## 2. **S3 Permissions**
The following permissions are needed for creating and managing S3 buckets and objects used for ETL processes:

- `s3:CreateBucket`
- `s3:DeleteBucket`
- `s3:PutObject`
- `s3:GetObject`
- `s3:ListBucket`
- `s3:PutBucketPolicy`
- `s3:DeleteObject`

## 3. **IAM Permissions**
These permissions are required to create and manage IAM roles and policies associated with Redshift and Glue:

- `iam:CreateRole`
- `iam:DeleteRole`
- `iam:AttachRolePolicy`
- `iam:DetachRolePolicy`
- `iam:PassRole`
- `iam:GetRole`
- `iam:PutRolePolicy`
- `iam:DeleteRolePolicy`

## 4. **VPC Permissions**
Permissions needed to create and manage the VPC and related networking components for the Redshift cluster:

- `ec2:CreateVpc`
- `ec2:DeleteVpc`
- `ec2:CreateSubnet`
- `ec2:DeleteSubnet`
- `ec2:CreateInternetGateway`
- `ec2:AttachInternetGateway`
- `ec2:CreateNatGateway`
- `ec2:DeleteNatGateway`
- `ec2:CreateRouteTable`
- `ec2:AssociateRouteTable`
- `ec2:CreateRoute`

## 5. **Glue Permissions (Optional)**
If Glue is used for ETL processes, these permissions are needed:

- `glue:CreateDatabase`
- `glue:DeleteDatabase`
- `glue:CreateCrawler`
- `glue:DeleteCrawler`
- `glue:StartCrawler`
- `glue:StopCrawler`
- `glue:GetCrawler`
- `glue:GetDatabases`

## Notes
- Ensure that the IAM user or role deploying the stack has all the above permissions to avoid deployment issues.
- If using AWS managed policies, the following policies can be considered:
  - `AmazonRedshiftFullAccess`
  - `AmazonS3FullAccess` or `AmazonS3ReadOnlyAccess` (depending on requirements)
  - `AWSGlueServiceRole`
  - `AmazonEC2FullAccess`
  - `IAMFullAccess`

Always review and apply the principle of least privilege when granting these permissions.
