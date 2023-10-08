Zootopia

- Challenge
  - Challenge: Model Zoo
    https://www.spaceappschallenge.org/2023/challenges/building-the-space-biology-model-zoo

  - Time
    Toronto: 10.8 9am - 10.9 11:59pm
    Chicago: 10.8 8am - 10.9 10:59pm

  - Dataset
    - https://genelab.nasa.gov/datasets_and_counting
    - https://science.nasa.gov/biological-physical/programs/space-biology


  

+ [Google Doc](https://docs.google.com/document/d/1K6lgoii-VoXzJDCYtdKcNZ4D126ZX16gQD661QfDNNE/edit?usp=sharing)

+ Our model for [Space mouse](https://drive.google.com/file/d/1whPLN43rjUPgN1GDoUAqkWY8IbISKB6Y/view?usp=sharing)

## Data folder structure
```
📂Data
 ┣ 📂intermediate // File processed by scripts in this repo, details below
  ┣ 📜dna_data.csv
  ┣ 📜dna_str.txt
 ┣ 📂other
  ┣ 📜OSD-466-samples.csv // Example sample file downloaded from https://osdr.nasa.gov/bio/repo/data/studies/OSD-466
 ┣ 📂raw
   ┣ 📂gz
    ┣ 📜YOUR_RAW_DATA.fastq.gz 
    ┗ ... Anything.fastq.gz
    
```

## Data Process
```
1. use data_generation_finetune, choose the labels, and store all the datasets in /data/raw/gz, dna_data.csv will be generated in Data/intermediate
2. use data_generation_pretrain, it reads Data/intermediate/dna_data.csv and generate dna_str.txt for use.

```
