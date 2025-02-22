# Product Catalog Service (Retrieve & Manage Products)
Use Case:
Allows users to fetch product details and add new products to the system.

## Security & DevOps Considerations
Input Validation: Prevents SQL injection & XSS attacks.
Rate Limiting: Mitigates denial-of-service (DoS) attacks by controlling request rates.

Scalability: Runs multiple replicas for high availability.
CI/CD Pipeline: Automatically builds and deploys Docker images upon changes.
