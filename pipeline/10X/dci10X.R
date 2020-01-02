
# Create a path to a 10x output directory
samplefun <- function(sampleid, rootdir, postdir="outs/filtered_feature_bc_matrix/") {
  file.path(rootdir, sampleid, postdir)
}

# Import 10X data as Seurat object
import10X <- function(datadir, project, genecolumn = 2, uniquefeatures = TRUE, addMT = TRUE, patternMT = "^MT-") {
  my10X <- Read10X(data.dir = datadir, genecolumn , uniquefeatures)
  my10X <- CreateSeuratObject(counts = my10X, project = project, min.cells = 3, min.features = 200)
  if (addMT) {
    my10X[["percent.mt"]] <- PercentageFeatureSet(my10X, pattern = patternMT)
  }
  return(my10X)
}


# Produce quick qc plots for each samples
qcmetricsplots <- function(seuratobjs, rootdir = "/home/owzar001", w1 = 480*3, h1 =480, w2 = 480*2 , h2 = 480){
  foreach(sampleid = names(my10Xobjs)) %do% {
     file1 <- file.path(rootdir, paste0(sampleid, "-qcmetrics", ".png"))
     file2 <- file.path(rootdir, paste0(sampleid, "-featureplot", ".png"))
    png(file1, width = w1, height = h1)
    print(VlnPlot(seuratobjs[[sampleid]], features = c("nFeature_RNA", "nCount_RNA", "percent.mt"), ncol = 3))
    graphics.off()
    png(file2, width = w2, height = h2)
    plot1 <- FeatureScatter(seuratobjs[[sampleid]], feature1 = "nCount_RNA", feature2 = "percent.mt")
    plot2 <- FeatureScatter(seuratobjs[[sampleid]], feature1 = "nCount_RNA", feature2 = "nFeature_RNA")
    print(CombinePlots(plots = list(plot1, plot2)))
    graphics.off()
  }
    
}


library(Seurat)
library(foreach)
library(tidyverse)

rootdir <- "/mnt/data1/Project/HTAN/dci-bioinformatics-pipeline-misc/10X/"
sampleids <- list.files(rootdir,"SS")

# Make named list of 10X output directories
my10files <- sampleids %>% { set_names(map(., ~ samplefun(.x, rootdir)), .) } 

# Import 10X data as Seurat Objects
my10Xobjs <- names(my10files) %>% { set_names(map(., ~ import10X(my10files[[.x]], .x)), .) } 

qcmetricsplots(my10Xobjs)

sessionInfo()
q(save = "no")
