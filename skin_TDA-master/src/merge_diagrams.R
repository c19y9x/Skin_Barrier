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
# 获取文件夹下所有文件名
get_all_files <- function(path){
#  dir.create(path)
  files <- list.files(path = path, full.names = TRUE)
  return(files)
}

my_TDA <- function(filename, k, by){
  # 分割字符串
  ID <- tail(strsplit(filename, split = "/")[[1]],1)
  # 截取文件名
  ID <- sub(".txt$", "", ID)
  X <- read.table(filename, sep=",")
  colnames(X) <- c("x","y")
  Xlim <- c(0, 1400);
  Ylim <- c(0, 1200);
  X_knn.Diag <- gridDiag(X = X, FUN = knnDE, k = k,
                          lim = cbind(Xlim, Ylim),by = by,
                          sublevel = FALSE, library = "Dionysus",
                          printProgress = TRUE, location=TRUE)
  D_zero <- as.data.frame(X_knn.Diag$diagram[X_knn.Diag$diagram[,1]==0,])
  D_zero[, 2] <- log(D_zero[, 2])
  D_zero[, 3] <- log(D_zero[, 3])
  D_zero[, 4] <- (D_zero[, 2] + D_zero[, 3])/2 #mid-life
  D_zero[, 5] <- abs(D_zero[, 3] - D_zero[, 2]) #life-time
  D_zero[, 6] <- rep(ID,nrow(D_zero))
  colnames(D_zero)<- c("dimension", "Death","Birth", "midlife","lifetime", "ID")

  D_one <- as.data.frame(X_knn.Diag$diagram[X_knn.Diag$diagram[,1]==1,])
  D_one[, 2] <- log(D_one[, 2])
  D_one[, 3] <- log(D_one[, 3])
  D_one[, 4] <- (D_one[, 2] + D_one[, 3])/2
  D_one[, 5] <- D_one[, 3] - D_one[, 2]
  D_one[, 6] <- rep(ID,nrow(D_one))
  colnames(D_one)<- c("dimension", "Death","Birth", "midlife","lifetime", "ID")
  return(list(zero=D_zero, one=D_one))
}

#load the coodinate data
args <- commandArgs(trailingOnly = T)
outputs_path <- args[1]

# output <- get_all_files('实验中途数据/3_20_0')
output <- get_all_files(outputs_path)

D <- my_TDA(output[1], 100, 10)
D_zero=D$zero
D_one=D$one

for(i in seq(1, 5)){
  D <- my_TDA(output[i], 100, 10)
  D_zero <- rbind(D_zero, D$zero)
  D_one <- rbind(D_one, D$one)
}


# 分割字符串
image_name <- tail(strsplit(outputs_path, split = "/")[[1]],1)

"merge"
D_one_All <- D_one
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
png(filename = paste0(paste0("Result_Images/TDA/1-dim-",image_name),".png"),width = 4096,height = 2160,res = 300)
g2
dev.off()


D_zero_All <- D_zero
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
png(filename = paste0(paste0("Result_Images/TDA/0-dim-",image_name),".png"),width = 4096,height = 2160,res = 300)
g2
dev.off()