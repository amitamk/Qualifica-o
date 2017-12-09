
# coding: utf-8

# #### Este é o script usado para rodar o treinamento e o teste para a rede MLP Regressor, do Scikit-Learn 
# Criado no Jupyter com Python 2 por Amita Muralikrishna

# Definindo os pacotes:

# In[1]:


from sklearn.neural_network import MLPRegressor
import csv
import numpy as np
import random as rd


# Definindo a função que calculará o valor de SigmaNMAD para os padrões de teste:

# In[2]:


def sigmaNMAD(photoz, specz):
    err = (abs((photoz - specz) - np.median(photoz - specz)))/(1+specz)
    return 1.48*np.median(err)


# Lendo o conjunto de dados:

# In[3]:


#filename = 'redshift_between0and1.csv'
filename = 'redshift_between0and7.csv'

l = []

with open(filename, 'r') as f:
    if csv.Sniffer().has_header(f.read(2)):
        f.readline()
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        l.append(row)


# Abrindo um arquivo para salvar os valores de erro (sigmaNMAD) após os testes para cada configuração diferente de # de neurônios ocultos (10 configurações):

# In[4]:


#f = open('Sigmas_mlp_specz0a1.csv', 'w')
f = open('Sigmas_mlp_specz0a7.csv', 'w') #arquivo de saída com valores de erros (sigmasNMAD)
f.writelines('Neurons,Sigma1,Sigm2,Sigma3,Sigma4,Sigma5,Sigma6,Sigma7,Sigma8,Sigma9,Sigma10\n') #rótulos para o arquivo de saída

n = [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100] #10 diferentes quantidades de neurônios ocultos


# Loop de treinamento e teste para cada quantidade de neurônios ocultos (10 valores):

# In[6]:


for neurons in n:

    l = rd.sample(np.asarray(l),len(np.asarray(l))) #embaralhando as linhas dos padrões de entrada
    
    npoints_train = len(l)*2/3 #definindo quantidade de padrões para o treinamento (2/3 do conjunto de dados)
 
    X = np.asarray(l)[0:npoints_train,0:5] #separando os padrões de entrada para o treinamento
    y = np.asarray(l)[0:npoints_train,5] #separando as saídas desejadas para o treinamento
    
    sigmaS = '' #inicializando a string com sigmas para o teste i
    sigma = [] #inicializando o array sigma para o teste i
    
    #Loop de 10 treinamentos e testes para cada configuração de # de neurônios ocultos
    for i in range(10):
        hunits = (neurons,) #quantidade de neurônios ocultos para o treinamento i 
        
        #Configurando a MLP Regressor
        nnr = MLPRegressor(hidden_layer_sizes=hunits, activation='tanh', 
                           solver='adam', alpha=0.0001, batch_size='auto', 
                           learning_rate='constant', learning_rate_init=0.001, 
                           power_t=0.5, max_iter=1000, shuffle=True, 
                           random_state=None, tol=0.0001, verbose=False, 
                           warm_start=False, momentum=0.9, nesterovs_momentum=True, 
                           early_stopping=False, validation_fraction=0.1, 
                           beta_1=0.9, beta_2=0.999, epsilon=1e-08)
    
        nnr.out_activation_='relu' #definindo a função de ativação para a camada de saída
       
        nnr.fit(X,y) #treinando a rede
    
        Xq = np.asarray(l)[npoints_train:,0:5] #definindo os padrões de entrada para a fase de teste (1/3 do conjunto de dados)
        photoz = nnr.predict(Xq) #testando a rede para o treinamento i
        
        Zq = np.asarray(l)[npoints_train:,5] #definindo as saídas desejadas para comparação na fase de teste
        
        sigma.append(sigmaNMAD(photoz, Zq)) #calculando e armazenando o sigma obtido no teste i no array sigma
        sigmaS += ',' + str(sigma[-1]) # concatenando o último sigma calculado em uma string para gravar no arquivo de saída
             
    f.writelines(str(neurons)+sigmaS+'\n')  #gravando no arquivo de saída os sigmas (obtidos nos 10 testes) e 
                                            #a qtde de neurônios ocultos
               
f.close() #fechando o arquivo com resultados.


# Fim de Script: Arquivo de saída gerado!
