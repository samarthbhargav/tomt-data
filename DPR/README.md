# Prepare the data for DPR
```bash 
# create a sym link so code can be accessed
ln -s ../tomt ./tomt
mkdir -p dataset/
unzip ../data_release/Books.zip -d dataset
unzip ../data_release/Movies.zip -d dataset
srun python create_data_dpr.py --root dataset/ --dataset Movies --file_path dataset/Movies/DPR/
srun python create_data_dpr.py --root dataset/ --dataset Books --file_path dataset/Books/DPR/

srun python create_data_faiss_index.py --root dataset/ --dataset Movies --file_path dataset/Movies/DPR/
srun python create_data_faiss_index.py --root dataset/ --dataset Books --file_path dataset/Books/DPR/

srun python inference_format_test.py --root dataset/ --dataset Movies --file_path dataset/Movies/DPR/
srun python inference_format_test.py --root dataset/ --dataset Books --file_path dataset/Books/DPR/
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

