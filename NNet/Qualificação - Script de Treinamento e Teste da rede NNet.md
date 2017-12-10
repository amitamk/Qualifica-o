
#### Este é o script usado para rodar o treinamento e o teste para a rede NNet (R)

Definindo as bibliotecas:


```R
library(ggplot2)
library(nnet)
set.seed(999)
```

Lendo o conjunto de dados (em formato de data frame) e normalizando as colunas:


```R
redshifts <- read.csv("redshift_between0and1.csv")
#redshifts <- read.csv("redshift_between0and7.csv")
redshifts <- redshifts[c("u","g","r","i","z","redshift")]
redshifts <- as.data.frame(scale(redshifts))
npoints_train = as.integer(dim(redshifts)[1]*2/3) #definindo a quantidade de padrões de treinamento (2/3 do conjunto)
```

Preparando o arquivos de saída com os erros (sigmas):


```R
Sigmas <- data.frame(c(0),c(0),c(0),c(0),c(0),c(0),c(0),c(0),c(0),c(0),c(0))
names(Sigmas)<-c("neurons","sigma1","sigma2","sigma3","sigma4","sigma5","sigma6","sigma7","sigma8","sigma9","sigma10")
```

Loop de treinamento e teste para cada quantidade de neurônios ocultos:


```R
for(neurons in c(5,seq(10,100,10))){
  Sigma <- c() #inicializando o array de resultados

  #Loop para realizar 10 treinamentos/testes para cada # de neurônios
  for(i in seq(1,10)){
    samp <- c(sample(1:npoints_train,)) #embaralhando os índices dos padroões de entrada e saída para o treinamento
    nnet.fit <- nnet(redshift ~ ., data=redshifts, size=neurons, subset = samp, maxit = 10000) #configurando a rede NNet
    nnet.predict <- predict(nnet.fit, redshifts[-samp,]) #realizando o teste 
    redshiftsV <- redshifts[-samp,] #armazenando o conjunto utilizado no teste

    #calculando o valor de Sigma
    Sigma[i] <- 1.48*median(abs((nnet.predict-redshiftsV$redshift) - median(nnet.predict-redshiftsV$redshift))/(1+redshiftsV$redshift))
    
    #redshiftsV$predicted <- nnet.predict
    #redshiftsV$predicted <- NULL
  }

  newrow <- c(neurons,Sigma) #armazenando o sigma para a respectiva configuração de neurônios ocultos
  Sigmas <- rbind(Sigmas,newrow) #unindo a linha aos sigmas obtidos nos demais treinamentos
}
```

Gravando os sigmas no arquivo de saída


```R
write.csv(Sigmas, file = "Sigmas_nnet_between0and1.csv")
#write.csv(Sigmas, file = "Sigmas_nnet_between0and7.csv")

end.rcode-->
```
