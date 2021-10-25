### Codigo de R - Ejercicio 7
    library(dplyr) 
    library(readr)
    library(rpart)
    library(caret)
    library(doMC)

    # Limpiamos la consola
    cat("\014")
    # Limpiamos el entorno de R
    rm(list = ls())

    create_folds <- function(dataframe,n){
      # Obtenemos las filas del dataframe
      rows <- nrow(dataframe)
      # Calculamos la cantidad de "folds" que vamos a generar
      foldsLen <- ceiling(rows/n)
      # Dividimos el dataframe en la cantidad de folds calculados
      splittedData <- split(dataframe, sample(rep(1:n,foldsLen)))
      return(splittedData)
    }




    # Importamos el dataframe
    dataSet <- read_csv("../../arbolado-mza-dataset.csv")
    #View(dataSet)
    dataSet <- subset(dataSet, select=-c(id,ultima_modificacion,seccion,area_seccion,lat,long))
    View(dataSet)


    trainIndex <- createDataPartition(dataSet$inclinacion_peligrosa,p = 0.9, list = FALSE)
    trainSet  <- dataSet[trainIndex, ]
    testSet <- dataSet[-trainIndex, ]

    cross_validation(trainSet,10)


    # define training control
    train_control <- trainControl(method="cv", 
                              number=10, 
                              verboseIter=T,
                              classProbs=F,
                              allowParallel = TRUE

    ) 

    #View(trainSet)
    # Creamos la formula
    registerDoMC(cores=4)
    train_formula<-formula(inclinacion_peligrosa~.)

    trainSet %>% group_by(inclinacion_peligrosa) %>% summarise(n=n())
    trainSet$inclinacion_peligrosa <- as.factor(trainSet$inclinacion_peligrosa)
    testSet$inclinacion_peligrosa <- as.factor(testSet$inclinacion_peligrosa)


    # train the model 
    model <- train(x = trainSet, y = trainSet$inclinacion_peligrosa, method = "rpart", trControl = train_control)
    #model <- train(train_formula, data = trainSet, trControl = train_control, method = "rpart")

    print(model)

    # make predictions
    pred = predict(model,testSet)
    as.data.frame(pred)
    testSet$prediction = pred
    View(testSet)

    # summarize results
    confusionMatrix <- confusionMatrix(testSet$prediction,testSet$inclinacion_peligrosa)
    confusionMatrix










