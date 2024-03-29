from pyspark.sql import SparkSession
from pyspark.sql.functions import lit, DataFrame


def get_products_categories_relationships(products_df: DataFrame,
                                          categories_df: DataFrame,
                                          product_category_df: DataFrame):
    product_category_pairs_df = product_category_df.join(categories_df, "category_name", "left").join(products_df,
                                                                                                      "product_name",
                                                                                                      "left")

    products_with_no_categories_df = products_df.join(product_category_df, ["product_name"], "left_anti").withColumn(
        "category_name", lit(None))

    combined_df = product_category_pairs_df.select("product_name", "category_name").union(
        products_with_no_categories_df.select("product_name", "category_name"))

    return combined_df


def print_dataframe(title_before, dataframe: DataFrame):
    print(title_before)
    dataframe.show()


if __name__ == "__main__":
    spark = SparkSession.builder.appName("ProductCategoryPairs").getOrCreate()

    products_data = [
        ("product1",),
        ("product2",),
        ("product3",),
        ("product4",)
    ]

    categories_data = [
        ("category1",),
        ("category2",),
        ("category3",),
    ]

    product_category_data = [
        ("product1", "category1"),
        ("product1", "category2"),
        ("product2", "category2"),
        ("product4", "category3")
    ]

    products_df = spark.createDataFrame(products_data, ["product_name"])
    categories_df = spark.createDataFrame(categories_data, ["category_name"])
    product_category_df = spark.createDataFrame(product_category_data, ["product_name", "category_name"])

    combine_df = get_products_categories_relationships(products_df, categories_df, product_category_df)

    print_dataframe("All products and their categories", combine_df)

    spark.stop()
