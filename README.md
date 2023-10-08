# Zootopia (Model Zoo)

## Challenge
  - Challenge: Model Zoo
    https://www.spaceappschallenge.org/2023/challenges/building-the-space-biology-model-zoo

## Our model
  + [Space mouse](https://drive.google.com/file/d/1whPLN43rjUPgN1GDoUAqkWY8IbISKB6Y/view?usp=sharing)
  + More models will be coming, due to time limit, we only have time for one trained model


## Data folder structure
- Following is details about data processing from *.fastq.gz to dna data needed for the model zoo. Reference dataset can be found at the bottom.
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

1. use data_generation_finetune, choose the labels, and store all the datasets in /data/raw/gz,
  dna_data.csv will be generated in Data/intermediate
2. use data_generation_pretrain, it reads Data/intermediate/dna_data.csv and generate dna_str.txt for use.

```


  - Dataset Reference
    - https://genelab.nasa.gov/datasets_and_counting
    - https://science.nasa.gov/biological-physical/programs/space-biology
