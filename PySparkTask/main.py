from pyspark.sql import SparkSession

# Создаем сессию Spark
spark = SparkSession.builder.getOrCreate()

# Предположим, что у нас есть следующие датафреймы
products = spark.createDataFrame([('prod1',), ('prod2',), ('prod3',)], ['product_name'])
categories = spark.createDataFrame([('prod1', 'cat1'), ('prod1', 'cat2'), ('prod2', 'cat1')], ['product_name', 'category_name'])

# Объединяем датафреймы
df = products.join(categories, on='product_name', how='left')

# Получаем все пары «Имя продукта – Имя категории»
pairs = df.filter(df.category_name.isNotNull()).select('product_name', 'category_name')

# Получаем имена всех продуктов, у которых нет категорий
no_category = df.filter(df.category_name.isNull()).select('product_name')

# Выводим результаты
pairs.show()
no_category.show()

