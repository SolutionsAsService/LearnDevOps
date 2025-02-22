# Infrastructure as Code (IaC)

## Use Case Example:
Imagine a company managing cloud infrastructure manually. Every time a new server is needed, an engineer provisions it via the cloud console. This process is time-consuming and error-prone. Infrastructure as Code (IaC) automates infrastructure provisioning using declarative code, ensuring consistency, scalability, and repeatability.

A common tool for this is Terraform, which allows you to define infrastructure in a human-readable format and apply changes with version control.

## Security & DevOps Considerations:
Security: Use role-based access control (RBAC) to limit infrastructure modifications, encrypt secrets, and store state files securely (e.g., in AWS S3 with encryption).
DevOps: CI/CD pipelines can apply infrastructure changes automatically after review, ensuring all environments (dev, staging, production) remain consistent.
Assorted Code Example:
Example: Defining an AWS EC2 instance using Terraform.
