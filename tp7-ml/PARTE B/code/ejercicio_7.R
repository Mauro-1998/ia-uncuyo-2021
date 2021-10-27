# Limpiamos la consola
cat("\014")
# Limpiamos el entorno de R
rm(list = ls())
library(dplyr) 
library(readr)
library(rpart)
library(caret)
library(randomForest)
library(naivebayes)
library(doMC)

registerDoMC(cores = 4)

# Importamos el dataframe
testSet <- read_csv("arbolado-mza-dataset-test.csv")
trainSet <- read_csv("arbolado-mza-dataset.csv")

trainSet$inclinacion_peligrosa <- as.factor(trainSet$inclinacion_peligrosa)

treesID <- testSet$id
treesID

#View(dataSet)
# Vamos a limpiar el conjunto de datos trainSet
trainSet <- subset(trainSet, select=-c(id,ultima_modificacion,lat,long,area_seccion))
testSet <- subset(testSet, select=-c(id,ultima_modificacion,lat,long,area_seccion))
View(trainSet)
View(testSet)
# Balanceamos las cargas para evitar que el algoritmo se sesgue nos quedaremos con 4000 registros de los que no tienen inclinacion peligrosa

estables <- trainSet[trainSet$inclinacion_peligrosa == 0, ] 
no_estables <- trainSet[trainSet$inclinacion_peligrosa == 1, ]

nrow(estables)
nrow(no_estables)

prob <- (nrow(no_estables)*100/nrow(estables))/100
indice_estables <- createDataPartition(estables$especie,p=prob ,list=FALSE)
estables <- estables[indice_estables,]
nrow(estables)
nrow(no_estables)

# Juntamos los dataframes balanceados
trainSet <- rbind(estables,no_estables)
nrow(trainSet)

# Mezclamos las filas del dataframe
trainSet <- trainSet[sample(nrow(trainSet)),]
#trainSet <- merge(trainSet,trainSet)
nrow(trainSet)
trainSet %>% group_by(inclinacion_peligrosa) %>% summarise(n=n())
View(trainSet)


# Agregamos variables categoricas para mejorar el modelo
promedio <- mean(trainSet$circ_tronco_cm)
incremento <- promedio/2 # Generamos 4 puntos equidistantes a partir del promedio
trainSet <- trainSet %>% mutate(circ_tronco_cm_cat= ifelse(`circ_tronco_cm`<= incremento,'Bajo',
                                                           ifelse(`circ_tronco_cm`> incremento & `circ_tronco_cm` <= 2*incremento, 'Medio',
                                                                  ifelse(`circ_tronco_cm` > 2*incremento & `circ_tronco_cm` <= 3*incremento, 'Alto','Muy Alto'))))

promedio <- mean(testSet$circ_tronco_cm)
incremento <- promedio/2 # Generamos 4 puntos equidistantes a partir del promedio
testSet <- testSet %>% mutate(circ_tronco_cm_cat= ifelse(`circ_tronco_cm`<= incremento,'Bajo',
                                                           ifelse(`circ_tronco_cm`> incremento & `circ_tronco_cm` <= 2*incremento, 'Medio',
                                                                  ifelse(`circ_tronco_cm` > 2*incremento & `circ_tronco_cm` <= 3*incremento, 'Alto','Muy Alto'))))

View(trainSet)
View(testSet)


# define training control
ctrl_fast <- trainControl(method="cv", number=10, verboseIter=T, classProbs=F, allowParallel = TRUE)

View(trainSet)


train_formula<-formula(inclinacion_peligrosa ~  .)
model_caret<- train(train_formula, data = trainSet, method = "rf", trControl = ctrl_fast)


inclinacion_peligrosa <- predict(model_caret,testSet)
newSet <- data.frame(id = treesID,inclinacion_peligrosa = inclinacion_peligrosa)
View(newSet)


newSet %>% group_by(inclinacion_peligrosa) %>% summarise(n=n())

write.csv(newSet,file="envio.csv",row.names = FALSE)






















