spark = SparkSession.builder.getOrCreate()

dfE = spark.read.format("csv").load("/home/alfredo_pomales/spark/escuelasPR.csv")

dfS = spark.read.format("csv").load("/home/alfredo_pomales/spark/studentsPR.csv")

dfEscuela = dfE.toDF("region","distrito","municipio","sid","nombre","nivel","cid")

dfStudent = dfS.toDF("region","distrito","sid","nombre","nivel","sexo","stid")

dfEscuela.filter(dfEscuela.region == "Arecibo").groupBy(dfEscuela.distrito, dfEscuela.municpio).count().show()
