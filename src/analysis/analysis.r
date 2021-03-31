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
hamiltonHSA <- houseSizeApportionments[ which(houseSizeApportionments$method == "Hamilton"), ]
jeffersonHSA <- houseSizeApportionments[ which(houseSizeApportionments$method == "Jefferson"), ]
lowndesHSA <- houseSizeApportionments[ which(houseSizeApportionments$method == "Lowndes"), ]
adamsHSA <- houseSizeApportionments[ which(houseSizeApportionments$method == "Adams"), ]
websterHSA <- houseSizeApportionments[ which(houseSizeApportionments$method == "Webster"), ]
deanHSA <- houseSizeApportionments[ which(houseSizeApportionments$method == "Dean"), ]
huntingtonHillHSA <- houseSizeApportionments[ which(houseSizeApportionments$method == "Huntington-Hill"), ]

# Filter data for variable census years dataset
hamiltonCYA <- censusYearApportionments[ which(censusYearApportionments$method == "Hamilton"), ]
jeffersonCYA <- censusYearApportionments[ which(censusYearApportionments$method == "Jefferson"), ]
lowndesCYA <- censusYearApportionments[ which(censusYearApportionments$method == "Lowndes"), ]
adamsCYA <- censusYearApportionments[ which(censusYearApportionments$method == "Adams"), ]
websterCYA <- censusYearApportionments[ which(censusYearApportionments$method == "Webster"), ]
deanCYA <- censusYearApportionments[ which(censusYearApportionments$method == "Dean"), ]
huntingtonHillCYA <- censusYearApportionments[ which(censusYearApportionments$method == "Huntington-Hill"), ]

# Plot house size lines together

png(file = "houseSizeGraph.png")
ggplot() + xlab("House Size") + ylab("District Population") + 
  labs(color = "Method") + scale_y_continuous(labels = scales::label_comma()) +
  geom_line(data = hamiltonHSA, aes(x = house_size, y = ave_constituency, color = method)) + 
  geom_line(data = jeffersonHSA, aes(x = house_size, y = ave_constituency, color = method)) + 
  geom_line(data = lowndesHSA, aes(x = house_size, y = ave_constituency, color = method)) + 
  geom_line(data = adamsHSA, aes(x = house_size, y = ave_constituency, color = method)) + 
  geom_line(data = websterHSA, aes(x = house_size, y = ave_constituency, color = method)) + 
  geom_line(data = deanHSA, aes(x = house_size, y = ave_constituency, color = method)) + 
  geom_line(data = huntingtonHillHSA, aes(x = house_size, y = ave_constituency, color = method))
dev.off()

# Plot census year lines together

png(file = "censusYearGraph.png")
ggplot() + xlab("Year") + ylab("District Population") + 
  labs(color = "Method") + scale_y_continuous(labels = scales::label_comma()) +
  geom_line(data = hamiltonCYA, aes(x = year, y = ave_constituency, color = method)) + 
  geom_line(data = jeffersonCYA, aes(x = year, y = ave_constituency, color = method)) + 
  geom_line(data = lowndesCYA, aes(x = year, y = ave_constituency, color = method)) + 
  geom_line(data = adamsCYA, aes(x = year, y = ave_constituency, color = method)) + 
  geom_line(data = websterCYA, aes(x = year, y = ave_constituency, color = method)) + 
  geom_line(data = deanCYA, aes(x = year, y = ave_constituency, color = method)) + 
  geom_line(data = huntingtonHillCYA, aes(x = year, y = ave_constituency, color = method))
dev.off()
