# Microsoft Fabric CI/CD Sample

A sample repository for exploring continuous integration and continuous delivery (CI/CD) with Microsoft Fabric.

The goal is to demonstrate how Fabric item definitions can be version-controlled, reviewed, and promoted across development, test, and production workspaces.

## Current status

This repository is a starting point. It does not yet include Fabric item definitions, deployment scripts, or automated workflows. The workflow below describes the intended approach, not an already configured deployment.

## Prerequisites

- Access to a Microsoft Fabric tenant and workspaces with the capacity and permissions required for the features you use.
- A GitHub account with access to this repository.
- Fabric Git integration enabled by your tenant administrator, where required.
- Separate development, test, and production workspaces if you plan to demonstrate environment promotion.

Feature availability and supported item types vary. Check the Microsoft documentation linked below before configuring your environment.

## Getting started

1. Clone the repository:

   ```powershell
   git clone https://github.com/AmudaPalani/fabric-cicd.git
   Set-Location fabric-cicd
   ```

2. In your Fabric development workspace, open **Workspace settings > Git integration**.
3. Connect to GitHub, select this repository, and choose the branch and repository folder to synchronize.
4. Create or update supported Fabric items in the development workspace, then commit their definitions through Fabric Git integration.
5. Use feature branches and pull requests to review changes before merging into your main branch.
6. Configure a deployment approach to promote approved changes to test and production.

Connecting a workspace to Git does not by itself configure automated deployments.

## Intended CI/CD workflow

```text
Development workspace
        |
        v
Git branch -> Pull request -> Review and validation -> Main branch
                                                          |
                                                          v
                                                   Test workspace
                                                          |
                                                   Validate / approve
                                                          |
                                                          v
                                                Production workspace
```

- **Source control:** Store supported Fabric item definitions in Git.
- **Continuous integration:** Add checks to validate repository changes when a pull request is opened or updated.
- **Continuous delivery:** Promote approved changes using Fabric deployment pipelines or a separately configured API/script-based workflow.
- **Environment configuration:** Manage environment-specific connections, parameters, and deployment rules explicitly rather than assuming development settings work everywhere.

## Suggested repository layout

As the sample grows, it can use a structure such as:

```text
fabric-cicd/
|-- README.md
|-- fabric/               # Fabric-managed item definitions
|-- scripts/              # Validation and deployment scripts
`-- .github/
    `-- workflows/        # GitHub Actions CI/CD workflows
```

Only this README is currently provided. The other folders are suggestions and are not required by Fabric.

## Security and deployment considerations

- Do not commit credentials, access tokens, connection strings, or sensitive data.
- Use an approved identity and secret store for any automation you add.
- Grant deployment identities only the permissions they need.
- Validate changes in a non-production workspace before promoting them.
- Use approval gates for production deployments.
- Check Git integration and deployment support for each Fabric item type; support is not identical across features.

## Resources

- [Microsoft Fabric CI/CD overview](https://learn.microsoft.com/en-us/fabric/cicd/cicd-overview)
- [Fabric Git integration overview](https://learn.microsoft.com/en-us/fabric/cicd/git-integration/intro-to-git-integration)
- [Fabric deployment pipelines overview](https://learn.microsoft.com/en-us/fabric/cicd/deployment-pipelines/intro-to-deployment-pipelines)

## Disclaimer

This repository is intended for learning and demonstration. Review and adapt any future scripts, permissions, and deployment settings before using them in production.
