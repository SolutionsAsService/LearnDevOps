# LearnDevOps

LearnDevOps is a set of short, hands-on tracks on the DevOps practices most teams meet
first: automated delivery, GitOps, infrastructure as code, microservices and monitoring.
Each track has a readme with a use case, security and DevOps notes, and example files you
can read or run.

## The tracks

- **[CI/CD](CI-CD/readme.md)**: automated build, test and deploy, with secrets in GitHub Secrets and a rollback strategy.
- **[GitOps](GitOps/readme.md)**: Kubernetes state declared in Git and synced to the cluster with ArgoCD or Flux.
- **[IaC](IaC/readme.md)**: cloud infrastructure defined in Terraform, with encrypted remote state and state locking.
- **[Microservices](Microservices/E-Commerce/readme.md)**: five service examples (AuthService, DistributedSystems, E-Commerce, ProductCatalog, ServerlessApplications).
- **[Monitoring](Monitoring/readme.md)**: logs and metrics with Prometheus and Grafana, and alerts sent to Slack or PagerDuty.

## How to use it

```bash
git clone https://github.com/SolutionsAsService/LearnDevOps
cd LearnDevOps
```

Open the readme of the track you want, then look at the example files in that track's folder
(for example `CI-CD/deploy.yml`, `IaC/main.tf` or `Monitoring/prometheus.yml`). Each readme says
what the example is for and which security and DevOps points it illustrates.

The landing page, `index.html`, shows the five tracks as one path and links to each readme.

## Contributing

Bug reports, corrections, docs and fixes are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT. See [LICENSE](LICENSE).
