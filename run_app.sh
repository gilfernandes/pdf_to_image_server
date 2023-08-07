CONDA_ENV=pdf_to_image_server
source /home/ubuntu/miniconda3/etc/profile.d/conda.sh
conda activate $CONDA_ENV
cd /home/ubuntu/projects/pdf_to_image_server
python ./pdf_to_image_server/server.py
