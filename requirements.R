# Set R repository to a fixed backup for repository
options(repos = list(CRAN = 'http://mran.revolutionanalytics.com/snapshot/2021-01-01/'))

# Install packages not present in the Docker image by default
install.packages("sp")
install.packages("ggplot2")
install.packages("extrafont")
install.packages("heatmaply")
install.packages("ggrepel")
install.packages("ggpubr")
install.packages("igraph")
install.packages("dplyr")
install.packages("reticulate")
install.packages("robustbase")
