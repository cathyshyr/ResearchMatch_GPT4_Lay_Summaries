library(XML)
library(rentrez)
library(readr)
setwd("./data/")
PubMED_ids <- read.csv("ResearchMatch publications PubMed IDs.csv", header = TRUE)

# Randomly select 100 IDs
set.seed(9)
selected_IDs_100 <- sample(PubMED_ids$IDs, 100, replace = FALSE)
write.csv(selected_IDs_100, file = "selected_IDs_100.csv")

selected_IDs <- read.csv("selected_IDs_100.csv")
selected_IDs <- selected_IDs$x

abstract_text <- vector("list", length = length(selected_IDs))
for(i in 1:length(selected_IDs)){
  print(i)
  record <- entrez_fetch(db = "pubmed", id = selected_IDs[i], rettype = "xml", parsed = TRUE)
  
  abstract_nodes <- xpathSApply(record, "//Abstract", xmlValue)
  
  if (length(abstract_nodes) > 0) {
    abstract_text[[i]] <- abstract_nodes[[1]]
  } else {
    abstract_text[[i]] <- ""
  }
}

abstract_text <- data.frame(ID = selected_IDs, abstract = do.call("rbind", abstract_text))

readr::write_excel_csv(abstract_text, file = "abstract_text.csv")
