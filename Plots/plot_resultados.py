
import csv
import numpy as np
import matplotlib.pyplot as plt

filename = 'Sigmas_nnet_specz0a1.csv'

l = [] 

with open(filename, 'r') as f:
    if csv.Sniffer().has_header(f.read(2)):
        f.readline()
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        l.append(row)


hNeurons = np.asarray(l)[:,0]
hNeurons = hNeurons.astype(int)
data = [np.asarray(l)[0,1:], np.asarray(l)[1,1:], np.asarray(l)[2,1:], np.asarray(l)[3,1:], np.asarray(l)[4,1:], np.asarray(l)[5,1:], np.asarray(l)[6,1:], np.asarray(l)[7,1:], np.asarray(l)[8,1:], np.asarray(l)[9,1:], np.asarray(l)[10,1:]]


bp = plt.figure(1, figsize=(7,7),dpi=80, facecolor='w', edgecolor='k')
#bp.suptitle('Variacao do sigma em funcao do numero de neuronios ocultos', fontsize=14, fontweight='bold')

ax = bp.add_subplot(111)

ax.boxplot(data, labels=hNeurons, meanprops=dict(marker='D', markeredgecolor='black',
                      markerfacecolor='firebrick'), meanline=False, showmeans=True)

ax.set_title('Sigma para a NNET - Specz de 0.01 a 1')
ax.set_ylim([0,0.2])
ax.set_xlabel('# de Neuronios ocultos')
ax.set_ylabel('Sigma NMAD')

plt.show()


#*******************************************************************************************************************
#PARA O 2ª CONJUNTO DE DADOS
filename = 'Sigmas_nnet_specz0a7.csv'

l = [] 

with open(filename, 'r') as f:
    if csv.Sniffer().has_header(f.read(2)):
        f.readline()
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        l.append(row)

hNeurons = np.asarray(l)[:,0]
hNeurons = hNeurons.astype(int)
data = [np.asarray(l)[0,1:], np.asarray(l)[1,1:], np.asarray(l)[2,1:], np.asarray(l)[3,1:], np.asarray(l)[4,1:], np.asarray(l)[5,1:], np.asarray(l)[6,1:], np.asarray(l)[7,1:], np.asarray(l)[8,1:], np.asarray(l)[9,1:], np.asarray(l)[10,1:]]

bp = plt.figure(2, figsize=(7,7),dpi=80, facecolor='w', edgecolor='k')
#bp.suptitle('Variacao do sigma em funcao do numero de neuronios ocultos', fontsize=14, fontweight='bold')

ax = bp.add_subplot(111)

ax.boxplot(data, labels=hNeurons, meanprops=dict(marker='D', markeredgecolor='black',
                      markerfacecolor='firebrick'), meanline=False, showmeans=True)

ax.set_title('Sigma para a NNET - Specz 0.01 a 7')
ax.set_ylim([0,0.2])
ax.set_xlabel('# de Neuronios ocultos')
ax.set_ylabel('Sigma NMAD')

plt.show()

#*******************************************************************************************************************
#PARA O 3ª CONJUNTO DE DADOS
filename = 'Sigmas_mlp_specz0a1.csv'

l = [] 

with open(filename, 'r') as f:
    if csv.Sniffer().has_header(f.read(2)):
        f.readline()
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        l.append(row)

hNeurons = np.asarray(l)[:,0]
hNeurons = hNeurons.astype(int)
data = [np.asarray(l)[0,1:], np.asarray(l)[1,1:], np.asarray(l)[2,1:], np.asarray(l)[3,1:], np.asarray(l)[4,1:], np.asarray(l)[5,1:], np.asarray(l)[6,1:], np.asarray(l)[7,1:], np.asarray(l)[8,1:], np.asarray(l)[9,1:], np.asarray(l)[10,1:]]

bp = plt.figure(2, figsize=(7,7),dpi=80, facecolor='w', edgecolor='k')
#bp.suptitle('Variacao do sigma em funcao do numero de neuronios ocultos', fontsize=14, fontweight='bold')

ax = bp.add_subplot(111)

ax.boxplot(data, labels=hNeurons, meanprops=dict(marker='D', markeredgecolor='black',
                      markerfacecolor='firebrick'), meanline=False, showmeans=True)

ax.set_title('Sigma para a MLP Regressor - Specz 0.01 a 1')
ax.set_ylim([0,0.06])
ax.set_xlabel('# de Neuronios ocultos')
ax.set_ylabel('Sigma NMAD')

plt.show()

#*******************************************************************************************************************
#PARA O 4ª CONJUNTO DE DADOS
filename = 'Sigmas_mlp_specz0a7.csv'

l = [] 

with open(filename, 'r') as f:
    if csv.Sniffer().has_header(f.read(2)):
        f.readline()
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        l.append(row)

hNeurons = np.asarray(l)[:,0]
hNeurons = hNeurons.astype(int)
data = [np.asarray(l)[0,1:], np.asarray(l)[1,1:], np.asarray(l)[2,1:], np.asarray(l)[3,1:], np.asarray(l)[4,1:], np.asarray(l)[5,1:], np.asarray(l)[6,1:], np.asarray(l)[7,1:], np.asarray(l)[8,1:], np.asarray(l)[9,1:], np.asarray(l)[10,1:]]

bp = plt.figure(2, figsize=(7,7),dpi=80, facecolor='w', edgecolor='k')
#bp.suptitle('Variacao do sigma em funcao do numero de neuronios ocultos', fontsize=14, fontweight='bold')

ax = bp.add_subplot(111)

ax.boxplot(data, labels=hNeurons, meanprops=dict(marker='D', markeredgecolor='black',
                      markerfacecolor='firebrick'), meanline=False, showmeans=True)

ax.set_title('Sigma para a MLP Regressor - Specz 0.01 a 7')
ax.set_ylim([0,0.06])
ax.set_xlabel('# de Neuronios ocultos')
ax.set_ylabel('Sigma NMAD')

plt.show()