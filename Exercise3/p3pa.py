spark = SparkSession.builder.getOrCreate()

dfE = spark.read.format("csv").load("/home/alfredo_pomales/spark/escuelasPR.csv")

dfS = spark.read.format("csv").load("/home/alfredo_pomales/spark/studentsPR.csv")

dfEscuela = dfE.toDF("region","distrito","municipio","sid","nombre","nivel","cid")

dfStudent = dfS.toDF("region","distrito","sid","nombre","nivel","sexo","stid")

dfEscuela.join(dfStudent,'sid').filter(dfEscuela.nivel == "Superior").filter(dfStudent.sexo == "M").filter((dfEscuela.municipio == "Ponce") | (dfEscuela.municpio == "San Juan")).show()
