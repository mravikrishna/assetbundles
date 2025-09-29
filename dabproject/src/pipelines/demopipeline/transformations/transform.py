import dlt

@dlt.table
def transformer():
    return spark.range(10)