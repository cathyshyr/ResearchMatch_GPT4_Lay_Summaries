## **Leveraging Artificial Intelligence to Summarize Abstracts in Lay Language for Increasing Research Accessibility and Transparency**


This repository contains the following files:

1. Pull abstracts.R is the R script used to retrieve abstracts using the National Center for Biotechnology Information’s Entrez Programming Utilities API.
2. Summarize_abstracts.py is the Python script used to generate lay summaries using OpenAI's GPT-4.
3. /data/ResearchMatch publications PubMed IDs.csv is a spreadsheet containing a list of PMIDs associated with the published studies that benefited from ResearchMatch's recruitment mechanism. This is an input file to the for loop defined in Pull abstracts.R.
4. /data/abstract_text.csv is a spreadsheet containing a list of randomly-sampled PMIDs from ResearchMatch's "Study Findings" page and their associated abstracts. This file can be reproduced by running Pull abstracts.R

