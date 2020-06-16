#!/bin/bash

#SBATCH --job-name=MyArrayJob
#SBATCH -J graph_1k
#SBATCH -o graph_1k.%A_%a.res
#SBATCH -e graph_1k.%A_%a.err

#SBATCH --mail-user laura.iacovissi@gmail.com
#SBATCH --mail-type=ALL

#SBATCH --array=0-9
#SBATCH --cpus-per-task=24
#SBATCH --mem=50G
#SBATCH --partition=short

# Run the python script
python3 numpy_generation.py --r $SLURM_ARRAY_TASK_ID --n 1000 --k 50
