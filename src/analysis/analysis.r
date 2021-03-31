# Install packages used below
# install.packages("dplyr")
# install.packages("ggplot2")
# install.packages("gam")
# install.packages("tidyverse")
# install.packages("plotly")

library(dplyr)
library(ggplot2)
library(gam)
library(tidyverse)
library(plotly)

# Load in data
houseSizeApportionments <- read.csv(file.choose(), header = TRUE, sep = ",")
censusYearApportionments <- read.csv(file.choose(), header = TRUE, sep = ",")

# Filter data for variable house sizes dataset
hamiltonHSA <- houseSizeApportionments[ which(houseSizeApportionments$method == "hamilton"), ]
jeffersonHSA <- houseSizeApportionments[ which(houseSizeApportionments$method == "jefferson"), ]
lowndesHSA <- houseSizeApportionments[ which(houseSizeApportionments$method == "lowndes"), ]
adamsHSA <- houseSizeApportionments[ which(houseSizeApportionments$method == "adams"), ]
websterHSA <- houseSizeApportionments[ which(houseSizeApportionments$method == "webster"), ]
deanHSA <- houseSizeApportionments[ which(houseSizeApportionments$method == "dean"), ]
huntingtonHillHSA <- houseSizeApportionments[ which(houseSizeApportionments$method == "huntington-hill"), ]

# Filter data for variable census years dataset
hamiltonCYA <- censusYearApportionments[ which(censusYearApportionments$method == "hamilton"), ]
jeffersonCYA <- censusYearApportionments[ which(censusYearApportionments$method == "jefferson"), ]
lowndesCYA <- censusYearApportionments[ which(censusYearApportionments$method == "lowndes"), ]
adamsCYA <- censusYearApportionments[ which(censusYearApportionments$method == "adams"), ]
websterCYA <- censusYearApportionments[ which(censusYearApportionments$method == "webster"), ]
deanCYA <- censusYearApportionments[ which(censusYearApportionments$method == "dean"), ]
huntingtonHillCYA <- censusYearApportionments[ which(censusYearApportionments$method == "huntington-hill"), ]

# Plot house size lines together

png(file = "tempHS.png")
ggplot() + xlab("House Size") + ylab("District Population") + labs(color = "Method") +
  geom_line(data = hamiltonHSA, aes(x = house_size, y = ave_constituency, color = method)) + 
  geom_line(data = jeffersonHSA, aes(x = house_size, y = ave_constituency, color = method)) + 
  geom_line(data = lowndesHSA, aes(x = house_size, y = ave_constituency, color = method)) + 
  geom_line(data = adamsHSA, aes(x = house_size, y = ave_constituency, color = method)) + 
  geom_line(data = websterHSA, aes(x = house_size, y = ave_constituency, color = method)) + 
  geom_line(data = deanHSA, aes(x = house_size, y = ave_constituency, color = method)) + 
  geom_line(data = huntingtonHillHSA, aes(x = house_size, y = ave_constituency, color = method))
dev.off()

# Plot census year lines together

png(file = "tempCY.png")
ggplot() + xlab("Year") + ylab("District Population") + labs(color = "Method") +
  geom_line(data = hamiltonCYA, aes(x = year, y = ave_constituency, color = method)) + 
  geom_line(data = jeffersonCYA, aes(x = year, y = ave_constituency, color = method)) + 
  geom_line(data = lowndesCYA, aes(x = year, y = ave_constituency, color = method)) + 
  geom_line(data = adamsCYA, aes(x = year, y = ave_constituency, color = method)) + 
  geom_line(data = websterCYA, aes(x = year, y = ave_constituency, color = method)) + 
  geom_line(data = deanCYA, aes(x = year, y = ave_constituency, color = method)) + 
  geom_line(data = huntingtonHillCYA, aes(x = year, y = ave_constituency, color = method))
dev.off()
