# Descrição do processo para o download dos dados do CasJobs (SDSS):

Para ter acesso à criação da query de busca e ao download dos conjuntos de dados, é necessário seguir os seguintes passos:

1) Criar uma conta (gratuita) no CasJobs, acessando: http://portal.sciserver.org/login-portal/Account/Register;

2) Realizar o acesso com a conta criada: http://portal.sciserver.org/login-portal/;

3) Clicar na opcão "CasJobs";

4) Clicar na aba "Query" e criar a query de acordo com as colunas e tabelas desejadas. No caso dos conjuntos utilizados neste trabalho, utilizou-se as seguintes queries:
  4.1) Primeiro conjunto de dados (100.000 galáxias de specz entre 0.01 e 7):
      SELECT TOP 100000 p.dered_u as u, p.dered_g as g, p.dered_r as r, p.dered_i as i, p.dered_z as z, s.z as redshift 
      INTO specTableVO
      FROM Galaxy AS p, SpecObj AS s
      WHERE p.objid = s.bestObjID 
      AND p.mode = 1 
      AND p.clean = 1 
      AND p.nChild = 0 
      AND p.type = 3 
      AND s.zWarning = 0 
      AND s.class = 'GALAXY' 
      AND s.z > 0.01
      AND s.zErr/s.z*100 < 0.05 
      AND p.dered_u > 0 AND p.dered_g > 0 AND p.dered_r > 0 AND p.dered_i > 0 AND p.dered_z > 0
  
  4.2) O segundo conjunto de dados foi baixado como um subconjunto do primeiro (50.000 galáxias com specz entre 0.01 e 1):
      SELECT TOP 50000 * INTO redshift_between0and1
      FROM specTableVO
      WHERE redshift > 0 AND redshift < 1
 
5) Cada query deve ser individualmente executada, clicando em "Submit";

6) Na aba MyDB, optar pela tabela criada ao lado esquerdo, e na parte central optar pelo tipo do arquivo (escolheu-se CSV) e clicar em "Download", e

7) Finalmente, na página que será aberta ("Output"), escolher o arquivo criado e clicar em "Download" para salvar o arquivo.

Quaisquer dúvidas ou sugestões podem ser enviadas ao endereço de e-mail: amita.mk@gmail.com.
