EDA do trabalho referente ao Exame de Qualificação
================
Amita Muralikrishna

-   [Explorando os dados de 100k galáxias do survey SSDS:](#explorando-os-dados-de-100k-galáxias-do-survey-ssds)
-   [Resumo de cada coluna](#resumo-de-cada-coluna)
-   [Histograma de cada banda fotométrica e do redshift](#histograma-de-cada-banda-fotométrica-e-do-redshift)
-   [Boxplot de cada banda fotométrica e do redshift](#boxplot-de-cada-banda-fotométrica-e-do-redshift)
-   [Redshifts e Erros de redshift](#redshifts-e-erros-de-redshift)
-   [Correlação entre cada banda fotométrica e o redshift](#correlação-entre-cada-banda-fotométrica-e-o-redshift)

Explorando os dados de 100k galáxias do survey SSDS:
----------------------------------------------------

``` r
dados <- read.csv(file="goodsample.csv", header=TRUE, sep=",", stringsAsFactors=FALSE)
str(dados)
```

    ## 'data.frame':    97214 obs. of  10 variables:
    ##  $ objid       : num  1.24e+18 1.24e+18 1.24e+18 1.24e+18 1.24e+18 ...
    ##  $ ra          : num  205 205 205 205 205 ...
    ##  $ dec         : num  -0.727 -0.651 -0.683 -0.735 -0.702 ...
    ##  $ u           : num  21.8 23 18.8 20 20.4 ...
    ##  $ g           : num  20.7 21.2 16.9 18.2 18.6 ...
    ##  $ r           : num  19.3 19.4 16 17.3 17.5 ...
    ##  $ i           : num  18.6 18.7 15.6 16.9 17 ...
    ##  $ z           : num  18.2 18.3 15.2 16.6 16.7 ...
    ##  $ redshift    : num  0.4994 0.4268 0.0894 0.088 0.1437 ...
    ##  $ redshift_err: num  1.21e-04 8.89e-05 1.53e-05 1.85e-05 2.85e-05 ...

Resumo de cada coluna
---------------------

``` r
summary(dados)
```

    ##      objid                 ra               dec                 u        
    ##  Min.   :1.238e+18   Min.   :  5.603   Min.   :-8.73124   Min.   :14.41  
    ##  1st Qu.:1.238e+18   1st Qu.:133.854   1st Qu.: 0.04536   1st Qu.:20.02  
    ##  Median :1.238e+18   Median :175.185   Median : 2.62218   Median :22.48  
    ##  Mean   :1.238e+18   Mean   :169.324   Mean   :24.53038   Mean   :22.14  
    ##  3rd Qu.:1.238e+18   3rd Qu.:210.424   3rd Qu.:53.25691   3rd Qu.:23.91  
    ##  Max.   :1.238e+18   Max.   :348.902   Max.   :68.54227   Max.   :29.41  
    ##        g               r               i               z        
    ##  Min.   :12.48   Min.   :11.57   Min.   :11.14   Min.   :10.84  
    ##  1st Qu.:18.31   1st Qu.:17.45   1st Qu.:17.03   1st Qu.:16.73  
    ##  Median :21.04   Median :19.42   Median :18.70   Median :18.29  
    ##  Mean   :20.34   Mean   :19.01   Mean   :18.31   Mean   :17.93  
    ##  3rd Qu.:22.04   3rd Qu.:20.49   3rd Qu.:19.56   3rd Qu.:19.11  
    ##  Max.   :27.21   Max.   :23.50   Max.   :24.33   Max.   :28.15  
    ##     redshift        redshift_err      
    ##  Min.   :0.01002   Min.   :-6.000000  
    ##  1st Qu.:0.13533   1st Qu.: 0.000026  
    ##  Median :0.40443   Median : 0.000086  
    ##  Mean   :0.37714   Mean   :-0.000175  
    ##  3rd Qu.:0.54105   3rd Qu.: 0.000151  
    ##  Max.   :7.01124   Max.   : 0.004852

Histograma de cada banda fotométrica e do redshift
--------------------------------------------------

``` r
par(mfrow=c(1, 5))
#title(main="Histogram of u (blue)")
hist(dados$u, xlim = c(10,30), ylim = c(0,40000),xlab = "u")
hist(dados$g, xlim = c(10,30), ylim = c(0,40000),xlab = "g")
hist(dados$r, xlim = c(10,30), ylim = c(0,40000),xlab = "r")
hist(dados$i, xlim = c(10,30), ylim = c(0,40000),xlab = "i")
hist(dados$z, xlim = c(10,30), ylim = c(0,40000),xlab = "z")
```

![](EDA_ADASS_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-3-1.png)

Boxplot de cada banda fotométrica e do redshift
-----------------------------------------------

``` r
par(mfrow=c(1, 6))
#pdf(file = "teste.pdf", width = 20, height = 14) 
boxplot(dados$u, main="U",ylim = c(10,30))
boxplot(dados$g, main="G",ylim = c(10,30))
boxplot(dados$r, main="R",ylim = c(10,30))
boxplot(dados$i, main="I",ylim = c(10,30))
boxplot(dados$z, main="Z",ylim = c(10,30))
boxplot(dados$redshift, main="Redshift")
```

![](EDA_ADASS_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-4-1.png)

``` r
#dev.off() 
```

Redshifts e Erros de redshift
-----------------------------

``` r
par(mfrow=c(1,1))
plot(dados$redshift)
```

![](EDA_ADASS_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-5-1.png)

``` r
par(mfrow=c(1,1))
plot(dados$redshift_err)
```

![](EDA_ADASS_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-5-2.png)

``` r
par(mfrow=c(1,1))
plot(dados$redshift_err,ylim = c(-0.01,0.005))
```

![](EDA_ADASS_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-5-3.png)

``` r
par(mfrow=c(1,1))
plot(dados$redshift,dados$redshift_err,ylim = c(-0.001,0.005))
```

![](EDA_ADASS_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-5-4.png)

Correlação entre cada banda fotométrica e o redshift
----------------------------------------------------

``` r
library(gclus)
```

    ## Warning: package 'gclus' was built under R version 3.4.3

    ## Loading required package: cluster

``` r
dados <- read.csv(file="redshift_between0and7.csv", header=TRUE, sep=",", stringsAsFactors=FALSE)
str(dados)
```

    ## 'data.frame':    96768 obs. of  6 variables:
    ##  $ u       : num  21.8 23 18.8 20 20.4 ...
    ##  $ g       : num  20.7 21.2 16.9 18.2 18.6 ...
    ##  $ r       : num  19.3 19.4 16 17.3 17.5 ...
    ##  $ i       : num  18.6 18.7 15.6 16.9 17 ...
    ##  $ z       : num  18.2 18.3 15.2 16.6 16.7 ...
    ##  $ redshift: num  0.4994 0.4268 0.0894 0.088 0.1437 ...

``` r
dados.r <- abs(cor(dados)) # Calcula as correlações
dados.col <- dmat.color(dados.r) # Define as cores
dados.o <- order.single(dados.r) 
cpairs(dados, dados.o, panel.colors=dados.col, gap=.5,
main="Parâmetros coloridos de acordo com a correlação." )
```

![](EDA_ADASS_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-6-1.png)

``` r
corr <- cor(dados$u,dados$redshift)
round(corr,3)
```

    ## [1] 0.769

``` r
corr <- cor(dados$g,dados$redshift)
round(corr,3)
```

    ## [1] 0.883

``` r
corr <- cor(dados$r,dados$redshift)
round(corr,3)
```

    ## [1] 0.881

``` r
corr <- cor(dados$i,dados$redshift)
round(corr,3)
```

    ## [1] 0.856

``` r
corr <- cor(dados$z,dados$redshift)
round(corr,3)
```

    ## [1] 0.835
