# Authentication Service (User Login & JWT Token Management)

## Use Case:
Handles user authentication and JWT token issuance for secure access to other services.

## Security & DevOps Considerations

Password Hashing: Uses bcrypt for secure password storage.
JWT Expiry: Limits token lifetime to one hour to reduce misuse.
Secret Management: Uses Kubernetes Secrets to store the JWT secret.

Kubernetes Secrets: Stores sensitive JWT secret keys securely.
Scalability: Multiple replicas ensure high availability.
