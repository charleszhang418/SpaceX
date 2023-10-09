# Zootopia (Model Zoo)

## Challenge
  - Challenge: Model Zoo
    https://www.spaceappschallenge.org/2023/challenges/building-the-space-biology-model-zoo

# High-level Summary


# Data folder structure
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

# Data

- We used data sample for space project related species projects from [Open Science for Life in Space](https://osdr.nasa.gov/bio/index.html) 
- Data processing steps:
  1. Retrieve sample csv and raw data(.gz) files and move into other/ and /raw/gz folders
  2. Transfer raw data files into csv files, due to the large quantity, we sample them for model
     training with equal portion from all the samples to reduce bias
  3. We will convert DNA sequences to kmer using Seq2Kmer as model pretraining input



# Model
## Introduction
  - Our model is based on DNABERT(Ji Y, Zhou Z, Liu H, Davuluri RV, 2021 DNABERT)[Github Repo](https://github.com/jerryji1993/DNABERT) DNABERT is a specialized Transformer-based model designed to process and understand DNA sequences. It is pre-trained on a large corpus of genomic data and can be fine-tuned for various genomics tasks, offering the potential to advance research and analysis in the field of genomics and bioinformatics.
  - Our model, built on the BERT architecture, has the ability to interpret DNA sequences thanks to its distinctive attention mechanism and sequence processing capabilities. We adapted the DNABERT framework and conducted pre-training using NASA Open Science species data. During pre-training, we processed DNA data by converting DNA sequences into k-mers as inputs, ultimately generating 768-dimensional output representations, which capture the model's understanding of DNA

##
- The significance of this model lies in its utility for researchers in the field of information data analysis who need to analyze DNA sequences. They can utilize this model to obtain outputs for their specific fine-tuning tasks.
  To ensure the accuracy of the pre-trained model, we conducted several downstream fine-tuning tasks.

## Pretrained models
  + Space Mouse
    + [Google Drive Direct Download](https://drive.google.com/file/d/1whPLN43rjUPgN1GDoUAqkWY8IbISKB6Y/view?usp=sharing)
    + [Hugging Face](https://huggingface.co/CheesyChank/SpaceMouse_DNABert)
  + Zebra Fish
    + [Google Drive Direct Download](https://drive.google.com/file/d/1xngF0lLYHUaEE2FQ1crdTHAXO-c--Cry/view?usp=sharing)
    + [Hugging Face](https://huggingface.co/CheesyChank/ZebraFish_DNABert)
  + More models will be coming

## Future Expectation
- We aim to establish a more mature and comprehensive database that also allows users to upload data at any time. Users should also be able to upload and download models. Additionally, We aim to establish cloud servers for model training. Users can utilize data from both local and cloud sources for pre-training models.
- We aim for a more sophisticated user interface (UI) to achieve a better user experience (UX) for researchers and professionals in DNA medicine and biological research, facilitating their studies.


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
- Data Set Reference
  - https://genelab.nasa.gov/datasets_and_counting
  - https://science.nasa.gov/biological-physical/programs/space-biology

- Other reference
  - Ji Y, Zhou Z, Liu H, Davuluri RV. DNABERT: pre-trained Bidirectional Encoder Representations from Transformers model for DNA-language in genome. Bioinformatics. 2021 Aug 9;37(15):2112-2120. doi: 10.1093/bioinformatics/btab083. PMID: 33538820.
