# Prepare the data for DPR
```bash
srun python create_data_dpr.py
srun python create_data_faiss_index.py
srun python inference_format_test.py
```

# Download Multi-Hop Dense Text Retrieval (MDR)

```bash
git clone https://github.com/facebookresearch/multihop_dense_retrieval.git
```

# Setup the conda environment

```bash
conda create --name MDR python=3.6
conda activate MDR
git clone git@github.com:facebookresearch/multihop_dense_retrieval.git
cd multihop_dense_retrieval 
bash setup.sh
```

# Train DPR
```bash
sbatch dpr_tomt.job
```

# Build FAISS index
```bash
sbatch encode_corpus_tomt.job
```


# Inference on test set
```bash
sbatch eval_dpr_tomt.job
```

