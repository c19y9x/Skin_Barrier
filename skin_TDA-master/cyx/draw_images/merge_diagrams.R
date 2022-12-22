rm(list=ls())
library(TDA)
library(ggplot2)
library(ggExtra)
library(MASS)
library(dplyr)
library(tidyr)
library(viridis)
library(akima)
library(ggrepel)

"0"
filename1 <- "skin_TDA-master/cyx/output_txt/3_50_90/3_0_50_90.txt"
X1 <- read.table(filename1, sep=",")

colnames(X1) <- c("x","y")

X1lim <- c(0, 1400);
Y1lim <- c(0, 1200);
by <- 10;

X1_knn.Diag <- gridDiag(X = X1, FUN = knnDE, k = 100,
                            lim = cbind(X1lim, Y1lim),by = by,
                            sublevel = FALSE, library = "Dionysus",
                            printProgress = TRUE, location=TRUE)

D_zero1 <- as.data.frame(X1_knn.Diag$diagram[X1_knn.Diag$diagram[,1]==0,])
D_zero1[, 2] <- log(D_zero1[, 2])
D_zero1[, 3] <- log(D_zero1[, 3])
D_zero1[, 4] <- (D_zero1[, 2] + D_zero1[, 3])/2
D_zero1[, 5] <- D_zero1[, 3] - D_zero1[, 2]
D_zero1[, 6] <- rep("3_0_50_90",nrow(D_zero1))
colnames(D_zero1)<- c("dimension", "Death","Birth", "midlife","lifetime", "ID") 

D_one1 <- as.data.frame(X1_knn.Diag$diagram[X1_knn.Diag$diagram[,1]==1,])
D_one1[, 2] <- log(D_one1[, 2])
D_one1[, 3] <- log(D_one1[, 3])
D_one1[, 4] <- (D_one1[, 2] + D_one1[, 3])/2
D_one1[, 5] <- D_one1[, 3] - D_one1[, 2]
D_one1[, 6] <- rep("3_0_50_90",nrow(D_one1))
colnames(D_one1)<- c("dimension", "Death","Birth", "midlife","lifetime", "ID") 

"2"
filename5 <- "skin_TDA-master/cyx/output_txt/3_50_90/3_2_50_90.txt"
X5 <- read.table(filename5, sep=",")

colnames(X5) <- c("x","y")

X5lim <- c(0, 1400);
Y5lim <- c(0, 1200);
by <- 10;

X5_knn.Diag <- gridDiag(X = X5, FUN = knnDE, k = 100,
                            lim = cbind(X5lim, Y5lim),by = by,
                            sublevel = FALSE, library = "Dionysus",
                            printProgress = TRUE, location=TRUE)

D_zero5 <- as.data.frame(X5_knn.Diag$diagram[X5_knn.Diag$diagram[,1]==0,])
D_zero5[, 2] <- log(D_zero5[, 2])
D_zero5[, 3] <- log(D_zero5[, 3])
D_zero5[, 4] <- (D_zero5[, 2] + D_zero5[, 3])/2
D_zero5[, 5] <- D_zero5[, 3] - D_zero5[, 2]
D_zero5[, 6] <- rep("3_2_50_90",nrow(D_zero5))
colnames(D_zero5)<- c("dimension", "Death","Birth", "midlife","lifetime", "ID") 
          
D_one5 <- as.data.frame(X5_knn.Diag$diagram[X5_knn.Diag$diagram[,1]==1,])
D_one5[, 2] <- log(D_one5[, 2])
D_one5[, 3] <- log(D_one5[, 3])
D_one5[, 4] <- (D_one5[, 2] + D_one5[, 3])/2
D_one5[, 5] <- D_one5[, 3] - D_one5[, 2]
D_one5[, 6] <- rep("3_2_50_90",nrow(D_one5))
colnames(D_one5)<- c("dimension", "Death","Birth", "midlife","lifetime", "ID") 

"4"
filename2 <- "skin_TDA-master/cyx/output_txt/3_50_90/3_4_50_90.txt"
X2 <- read.table(filename2, sep=",")

colnames(X2) <- c("x","y")

X2lim <- c(0, 1400);
Y2lim <- c(0, 1200);
by <- 10;

X2_knn.Diag <- gridDiag(X = X2, FUN = knnDE, k = 100,
                            lim = cbind(X2lim, Y2lim),by = by,
                            sublevel = FALSE, library = "Dionysus",
                            printProgress = TRUE, location=TRUE)

D_zero2 <- as.data.frame(X2_knn.Diag$diagram[X2_knn.Diag$diagram[,1]==0,])
D_zero2[, 2] <- log(D_zero2[, 2])
D_zero2[, 3] <- log(D_zero2[, 3])
D_zero2[, 4] <- (D_zero2[, 2] + D_zero2[, 3])/2
D_zero2[, 5] <- D_zero2[, 3] - D_zero2[, 2]
D_zero2[, 6] <- rep("3_4_50_90",nrow(D_zero2))
colnames(D_zero2)<- c("dimension", "Death","Birth", "midlife","lifetime", "ID") 

D_one2 <- as.data.frame(X2_knn.Diag$diagram[X2_knn.Diag$diagram[,1]==1,])
D_one2[, 2] <- log(D_one2[, 2])
D_one2[, 3] <- log(D_one2[, 3])
D_one2[, 4] <- (D_one2[, 2] + D_one2[, 3])/2
D_one2[, 5] <- D_one2[, 3] - D_one2[, 2]
D_one2[, 6] <- rep("3_4_50_90",nrow(D_one2))
colnames(D_one2)<- c("dimension", "Death","Birth", "midlife","lifetime", "ID") 

"6"
filename3 <- "skin_TDA-master/cyx/output_txt/3_50_90/3_6_50_90.txt"
X3 <- read.table(filename3, sep=",")

colnames(X3) <- c("x","y")

X3lim <- c(0, 1400);
Y3lim <- c(0, 1200);
by <- 10;

X3_knn.Diag <- gridDiag(X = X3, FUN = knnDE, k = 100,
                            lim = cbind(X3lim, Y3lim),by = by,
                            sublevel = FALSE, library = "Dionysus",
                            printProgress = TRUE, location=TRUE)

D_zero3 <- as.data.frame(X3_knn.Diag$diagram[X3_knn.Diag$diagram[,1]==0,])
D_zero3[, 2] <- log(D_zero3[, 2])
D_zero3[, 3] <- log(D_zero3[, 3])
D_zero3[, 4] <- (D_zero3[, 2] + D_zero3[, 3])/2
D_zero3[, 5] <- D_zero3[, 3] - D_zero3[, 2]
D_zero3[, 6] <- rep("3_6_50_90",nrow(D_zero3))
colnames(D_zero3)<- c("dimension", "Death","Birth", "midlife","lifetime", "ID") 
          
D_one3 <- as.data.frame(X3_knn.Diag$diagram[X3_knn.Diag$diagram[,1]==1,])
D_one3[, 2] <- log(D_one3[, 2])
D_one3[, 3] <- log(D_one3[, 3])
D_one3[, 4] <- (D_one3[, 2] + D_one3[, 3])/2
D_one3[, 5] <- D_one3[, 3] - D_one3[, 2]
D_one3[, 6] <- rep("3_6_50_90",nrow(D_one3))
colnames(D_one3)<- c("dimension", "Death","Birth", "midlife","lifetime", "ID") 

#D_one2$density <- get_density(D_one2$midlife, D_one2$lifetime)

"8"
filename4 <- "skin_TDA-master/cyx/output_txt/3_50_90/3_8_50_90.txt"
X4 <- read.table(filename4, sep=",")

colnames(X4) <- c("x","y")

X4lim <- c(0, 1400);
Y4lim <- c(0, 1200);
by <- 10;

X4_knn.Diag <- gridDiag(X = X4, FUN = knnDE, k = 100,
                            lim = cbind(X4lim, Y4lim),by = by,
                            sublevel = FALSE, library = "Dionysus",
                            printProgress = TRUE, location=TRUE)

D_zero4 <- as.data.frame(X4_knn.Diag$diagram[X4_knn.Diag$diagram[,1]==0,])
D_zero4[, 2] <- log(D_zero4[, 2])
D_zero4[, 3] <- log(D_zero4[, 3])
D_zero4[, 4] <- (D_zero4[, 2] + D_zero4[, 3])/2
D_zero4[, 5] <- D_zero4[, 3] - D_zero4[, 2]
D_zero4[, 6] <- rep("3_8_50_90",nrow(D_zero4))
colnames(D_zero4)<- c("dimension", "Death","Birth", "midlife","lifetime", "ID") 
          
D_one4 <- as.data.frame(X4_knn.Diag$diagram[X4_knn.Diag$diagram[,1]==1,])
D_one4[, 2] <- log(D_one4[, 2])
D_one4[, 3] <- log(D_one4[, 3])
D_one4[, 4] <- (D_one4[, 2] + D_one4[, 3])/2
D_one4[, 5] <- D_one4[, 3] - D_one4[, 2]
D_one4[, 6] <- rep("3_8_50_90",nrow(D_one4))
colnames(D_one4)<- c("dimension", "Death","Birth", "midlife","lifetime", "ID") 

"merge"
D_one_All <- rbind(D_one5,D_one4,D_one3,D_one2,D_one1)
g <- ggplot() + geom_point(data=D_one_All , aes(x=midlife, y=lifetime, color = ID), size=1) + 
#  xlim(-17.5, -12) + ylim(0,3) +
  labs(x="Mid-life", y="Life-time") +
  theme(panel.border = element_rect(fill = NA, size=1), 
    panel.background = element_rect(fill = NA,color = NA), 
    text=element_text(size=16, family="Arial"),
    legend.position = c(0.9,0.85))

g2 <- ggMarginal(
  g,
  type = "density",
  margins = "both",
  size = 5,
  groupColour = TRUE,
  groupFill = TRUE
)

# quartz(type="pdf", file="data/merged_diagrams_1dim.pdf")
png(filename = "Result_Images/TDA/3_50_90/merged_diagrams_1dim.png",width = 4096,height = 2160,res = 300)
g2
dev.off()


D_zero_All <- rbind(D_zero5,D_zero4,D_zero3,D_zero2,D_zero1)
g <- ggplot() + geom_point(data=D_zero_All , aes(x=midlife, y=lifetime, color = ID), size=1) + 
#  xlim(-17.5, -12) + ylim(0,3) +
  labs(x="Mid-life", y="Life-time") +
  theme(panel.border = element_rect(fill = NA, size=1), 
    panel.background = element_rect(fill = NA,color = NA), 
    text=element_text(size=16, family="Arial"),
    legend.position = c(0.9,0.85))

g2 <- ggMarginal(
  g,
  type = "density",
  margins = "both",
  size = 5,
  groupColour = TRUE,
  groupFill = TRUE
)

# quartz(type="pdf", file="data/merged_diagrams_0dim.pdf")
png(filename = "Result_Images/TDA/3_50_90/merged_diagrams_0dim.png",width = 4096,height = 2160,res = 300)
g2
dev.off()