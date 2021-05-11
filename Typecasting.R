

#Typecasting

retail <- read.csv("C:\\Users\\hp\\Desktop\\DataSets\\OnlineRetail.csv")

str(retail)

retail <- na.omit(retail)

#Character column to int transformation of InvoiceNo and Stock code

attach(retail)

retail$InvoiceNo <- as.integer(retail$InvoiceNo)

retail$StockCode <-as.integer(retail$StockCode)

retail <-na.omit(retail)
str(retail)

#EDA Of retail data
plot(retail)

hist(retail$InvoiceNo)
hist(retail$StockCode)
hist(retail$Quantity)
hist(retail$UnitPrice)

boxplot(retail$Quantity)
boxplot(retail$UnitPrice)








