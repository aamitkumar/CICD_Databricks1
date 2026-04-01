# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# MAGIC %sql
# MAGIC create or refresh streaming table st_orders
# MAGIC as
# MAGIC select * from stream(samples.tpch.orders)

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Create MV
# MAGIC CREATE OR REPLACE MATERIALIZED VIEW agg_orders
# MAGIC AS
# MAGIC SELECT
# MAGIC     count(o_orderkey) as cnt_orders,
# MAGIC     o_orderstatus
# MAGIC FROM LIVE.st_orders
# MAGIC group by o_orderstatus
