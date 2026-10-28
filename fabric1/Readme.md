# Fabric1: Hello CI/CD

The smallest possible Fabric CI/CD test. Everything happens inside Fabric. You don't need GitHub Actions, scripts, or Azure setup.

## What is Fabric, in one minute

- **Workspace**: a folder in Fabric that holds your items. You'll use two of them: **Dev** and **Test**.
- **Notebook**: a page of code that you run in Fabric. This folder has one notebook, `nb_sales_summary`.
- **Git integration**: links a workspace to a folder in a Git repo. Your Dev workspace is already linked to this `fabric1` folder.
- **Deployment pipeline**: a Fabric screen that copies items from Dev to Test.

## How this maps to CI/CD

| CI/CD idea | In this example |
| --- | --- |
| Code in source control | `nb_sales_summary` stored in `fabric1` |
| Commit a change | Fabric **Source control > Commit** |
| Deploy to the next environment | Fabric **Deployment pipeline > Deploy** (Dev to Test) |

## Steps

### 1. Get the notebook into Dev

1. Open your **Dev** workspace (the one synced to `fabric1`).
2. Click **Source control**, then **Update all** to pull the latest version from Git.
3. Open `nb_sales_summary` and click **Run all**. You should see:

   ```text
   Sales report v1
   East: 1500
   West: 1950
   ```

### 2. Make a change and commit it (CI)

1. In the notebook, change `version = "v1"` to `version = "v2"`.
2. Add a new region: `sales = {"East": 1500, "West": 1950, "North": 900}`.
3. Run it again. You should now see `v2` and a `North: 900` line.
4. Click **Source control**, enter the message `Update to v2`, and click **Commit**.
5. On GitHub, open the commit history of this repo. Your change to `notebook-content.py` is there.

### 3. Deploy Dev to Test (CD)

1. Create an empty workspace named something like `fabric1-test`.
2. In Fabric, go to **Workspaces > Deployment pipelines** and create a new pipeline.
3. Assign your Dev workspace to the **Development** stage and `fabric1-test` to the **Test** stage.
4. Select `nb_sales_summary` and click **Deploy** to Test.
5. Open the notebook in `fabric1-test` and click **Run all**. You should see `v2` and `North: 900`.

## You're done when

- GitHub shows your `Update to v2` commit.
- The notebook in Test prints `Sales report v2` with `North: 900`.

## Cleanup

Delete the Test workspace and the deployment pipeline when you no longer need them.
