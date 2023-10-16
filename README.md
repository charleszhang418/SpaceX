# Zootopia (Model Zoo)
## TODOs
- [ ] Enhance compatibility of CLinet
- [ ] Pop in more data
- [ ] Enhance accuracy

## A holistic, user-friendly online biomedical ecosystem

  - Challenge: Model Zoo
    https://www.spaceappschallenge.org/2023/challenges/building-the-space-biology-model-zoo
    

# High-level Summary
- We introduce "Zootopia," inspired by Disney's movie, providing a holistic, user-friendly online biomedical ecosystem. It offers uninterrupted access to, preview of, and download options for biomedical data in the Data section. Researchers can also upload and share their experimental data. In the Models section, users can preview, download, and upload pre-trained models specializing in DNA inputs, aiding in fine-tuning specific tasks. Our website was built using Python Flask, Next.js, and MongoDB. We pre-trained animal models with the DNABert framework and conducted fine-tuning. Our models achieved an accuracy rate of 51% in classifying the "spaceflight" category using DNA data from the OSD-466 mouse experiment, surpassing a 33% baseline accuracy.
- Zootopia addresses the critical need for a centralized platform for data and models in biomedical research. This resource simplifies access to crucial datasets, promotes collaboration, and enhances the efficiency of research efforts. Additionally, by providing pre-trained models and tools, Zootopia aids researchers in advancing their studies in space biology, contributing to a deeper understanding of the effects of space environments on living organisms.

# DataBase
- Our databases are powered by MongoDB and seamlessly integrated into Zootopia through our Flask-based backend.
- Our database structure comprises two main components: one dedicated to storing datasets and another for managing essential UI-related data.
- Within the Zootopia platform, users enjoy the convenience of downloading data for training and fine-tuning purposes. This data is accessible in CSV format directly from the database via our user-friendly web interface

# Data folder structure
- Following are details about data processing from *.fastq.gz to dna data needed for the model zoo. The reference dataset can be found at the bottom.
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

- We used data samples for space project-related species projects from [Open Science for Life in Space](https://osdr.nasa.gov/bio/index.html) 
- Data processing steps:
  1. Retrieve sample csv and raw data(.gz) files and move them into other/ and /raw/gz folders
  2. Transfer raw data files into csv files, due to the large quantity, we sample them for model
     training with an equal portion from all the samples to reduce bias
  3. We will convert DNA sequences to kmer using Seq2Kmer as model pretraining input



# Model
## Background
- DNA sequences are intricate and challenging to comprehend. We believe that large datasets can enable machines to interpret DNA data, assisting scientists in their research.
- Both DNA and textual data consist of lengthy sequences. We believe that Natural Language Processing (NLP) techniques can be employed to devise methods for analyzing DNA.
- DNA sequences are typically analyzed using techniques like RNNs and CNNs. We are attempting to incorporate the concept of Large Language Modeling (LLM) by utilizing pre-trained models to enhance the interpretation of DNA.
- DNA, like textual data, is structured as a sequence. BERT has demonstrated remarkable performance in the field of NLP. We believe that a DNA-specific version of BERT can also excel in the domain of DNA analysis.

## Introduction
  - Our model is based on DNABERT(Ji Y, Zhou Z, Liu H, Davuluri RV, 2021 DNABERT)[Github Repo](https://github.com/jerryji1993/DNABERT) DNABERT is a specialized Transformer-based model designed to process and understand DNA sequences. It is pre-trained on a large corpus of genomic data and can be fine-tuned for various genomics tasks, offering the potential to advance research and analysis in the field of genomics and bioinformatics.
  - Our model, built on the BERT architecture, has the ability to interpret DNA sequences thanks to its distinctive attention mechanism and sequence processing capabilities. We adapted the DNABERT framework and conducted pre-training using NASA Open Science species data. During pre-training, we processed DNA data by converting DNA sequences into k-mers as inputs, ultimately generating 768-dimensional output representations, which capture the model's understanding of DNA
- The significance of this model lies in its utility for researchers in the field of information data analysis who need to analyze DNA sequences. They can utilize this model to obtain outputs for their specific fine-tuning tasks.
  To ensure the accuracy of the pre-trained model, we conducted several downstream fine-tuning tasks.

## Pretrained models
  + Space Mouse
    + [Google Drive Direct Download](https://drive.google.com/file/d/1whPLN43rjUPgN1GDoUAqkWY8IbISKB6Y/view?usp=sharing)
    + [HuggingFace](https://huggingface.co/CheesyChank/SpaceMouse_DNABert)
  + Zebra Fish
    + [Google Drive Direct Download](https://drive.google.com/file/d/1xngF0lLYHUaEE2FQ1crdTHAXO-c--Cry/view?usp=sharing)
    + [HuggingFace](https://huggingface.co/CheesyChank/ZebraFish_DNABert)
  + More models will be coming

# Frontend
- Frontend is developed with React, Next.js, and aesthetic refined with Tailwind CSS, minimize redundancy and maximize usability
- Home page: Introduce the project
- Dataset page: allows users to browse and download datasets from our database, these datasets are finetuned and ready for use
- Model page: allows users to interact with some of our completed models, play with them, and link to our open-sourced repository

# Backend
- Backend is developed with Python and Flask, which is fast, maintainable and tested
- Empowers users to download/upload datasets and interact with models from the frontend

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

## Limitation
- Currently, we can only access partial experimental data for certain species, making it challenging to obtain a comprehensive dataset. This limitation may introduce bias into our results.
- We lack the capability to deploy large-scale training and iterations with extensive datasets, which can impact the model's accuracy. However, we have completed all pre-training steps and higher accuracy can be reached with additional iterations.
- For downstream fine-tuning tasks, we don't have well-defined classification features. We have considered setting the target variable as whether a species exhibits mutations. However, our model demonstrates exceptional DNA interpretation capabilities and greater potential beyond this choice of target variable.

## Reference
- Dataset references
  - https://genelab.nasa.gov/datasets_and_counting
  - https://science.nasa.gov/biological-physical/programs/space-biology

- Other references
  - Ji Y, Zhou Z, Liu H, Davuluri RV. DNABERT: pre-trained Bidirectional Encoder Representations from Transformers model for DNA-language in genome. Bioinformatics. 2021 Aug 9;37(15):2112-2120. doi: 10.1093/bioinformatics/btab083. PMID: 33538820.
