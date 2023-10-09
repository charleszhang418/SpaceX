# Zootopia (Model Zoo)

## Challenge
  - Challenge: Model Zoo
    https://www.spaceappschallenge.org/2023/challenges/building-the-space-biology-model-zoo

# High-level Summary


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

## Data
```
- We used data sample for space project related species projects from [Open Science for Life in Space](https://osdr.nasa.gov/bio/index.html) 
- Data processing steps:
  1. Retrieve sample csv and raw data(.gz) files and move into other/ and /raw/gz folders
  2. Transfer raw data files into csv files, due to the large quantity, we sample them for model
     training with equal portion from all the samples to reduce bias
  3. We will convert DNA sequences to kmer using Seq2Kmer as model pretraining input


```

## Our model
  + Space Mouse
    + [Google Drive Direct Download](https://drive.google.com/file/d/1whPLN43rjUPgN1GDoUAqkWY8IbISKB6Y/view?usp=sharing)
    + [Hugging Face](https://huggingface.co/CheesyChank/SpaceMouse_DNABert)
  + Zebra Fish
    + [Google Drive Direct Download](https://drive.google.com/file/d/1xngF0lLYHUaEE2FQ1crdTHAXO-c--Cry/view?usp=sharing)
    + [Hugging Face](https://huggingface.co/CheesyChank/ZebraFish_DNABert)
  + More models will be coming, due to time limit, we only have time for one trained model



## Code folder structure
```
📂Code
 ┣ 📜data_generation_finetune.ipynb // Data processing
 ┣ 📜data_generation_finetune.ipynb // Data processing
 ┣ 📜dnabert_finetune_test.ipynb // Finetune Testing
 ┣ 📜dnabert_pretrain_ipynb // For dnabert pretrain, details will mention below
 ┣ 📜run_pretrain.py // Will mention below
```

## Reference
# Data Set Reference
- https://genelab.nasa.gov/datasets_and_counting
- https://science.nasa.gov/biological-physical/programs/space-biology

# Other reference
