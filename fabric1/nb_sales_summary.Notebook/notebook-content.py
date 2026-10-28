# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

version = "v1"

sales = {"East": 1500, "West": 1950}

print(f"Sales report {version}")
for region, total in sales.items():
    print(f"{region}: {total}")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
