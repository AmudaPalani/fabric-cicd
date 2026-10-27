# Fabric1: Simple CI/CD Test Use Case

This folder is connected to a Microsoft Fabric development workspace.

Use it to test a basic Fabric CI/CD flow with one Lakehouse and one Notebook.

## Scenario

A notebook creates a small sales summary table in a Lakehouse.

You will:

1. Create the items in a development workspace.
2. Commit them to Git from Fabric.
3. Make a small notebook change.
4. Review the change in GitHub.
5. Deploy the change to a test workspace and confirm the new result.

## Prerequisites

- A development workspace connected to this repository folder: `fabric1`.
- A test workspace with permissions to deploy and run items.
- A deployment pipeline that maps the development workspace to the test workspace, or another configured deployment method.

## Step 1: Sync the Fabric items

This folder includes source definitions for:

- Lakehouse: `lh_sales_cicd`
- Notebook: `nb_sales_summary`

In the development workspace, open **Source control** and update from Git. After sync, open `nb_sales_summary` and attach `lh_sales_cicd` as its default Lakehouse.

The notebook contains this code:

```python
from pyspark.sql import Row
from pyspark.sql import functions as F

version = "v1"

sales = spark.createDataFrame([
    Row(region="East", product="Laptop", amount=1200),
    Row(region="West", product="Laptop", amount=1500),
    Row(region="East", product="Monitor", amount=300),
    Row(region="West", product="Monitor", amount=450),
])

summary = (
    sales.groupBy("region")
    .agg(F.sum("amount").alias("total_sales"))
    .withColumn("pipeline_version", F.lit(version))
    .withColumn("processed_at", F.current_timestamp())
)

summary.write.mode("overwrite").format("delta").saveAsTable("sales_summary")

display(spark.table("sales_summary").orderBy("region"))
```

Run the notebook. Expected result:

| region | total_sales | pipeline_version |
| --- | ---: | --- |
| East | 1500 | v1 |
| West | 1950 | v1 |

## Step 2: Commit Fabric binding changes

1. Open **Source control** in the development workspace.
2. Commit any Notebook metadata changes created by attaching the Lakehouse.
3. Use commit message: `Bind sales notebook to Lakehouse`.

Do not manually rename or edit Fabric `logicalId` values.

## Step 3: Make a reviewable change

Create a feature branch for the change if your Git workflow requires pull requests.

In `nb_sales_summary`, change:

```python
version = "v1"
```

to:

```python
version = "v2"
```

Then add this sales row:

```python
Row(region="North", product="Laptop", amount=900),
```

Run the notebook in development. Expected result:

| region | total_sales | pipeline_version |
| --- | ---: | --- |
| East | 1500 | v2 |
| North | 900 | v2 |
| West | 1950 | v2 |

Commit the change from Fabric with message: `Update sales sample to v2`.

## Step 4: Review and merge

1. Open a pull request in GitHub if you used a feature branch.
2. Confirm the notebook diff includes the `v2` version and `North` row.
3. Merge after review.
4. Update the development workspace from Git if Fabric shows incoming changes.

## Step 5: Deploy and validate in test

1. Deploy the Lakehouse and Notebook from development to test.
2. In test, confirm `nb_sales_summary` uses the test `lh_sales_cicd` Lakehouse.
3. Run the notebook in test.
4. Confirm the test `sales_summary` table matches the `v2` expected result.

## Success criteria

- Fabric item definitions are committed under `fabric1`.
- The notebook change is visible and reviewable in Git.
- The deployed test notebook runs successfully.
- The test table contains `North` and `pipeline_version = v2`.

## Cleanup

Remove the test items or tables when finished if they are no longer needed.