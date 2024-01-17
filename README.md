conda create -p env python==3.8 -y

conda activate env/

conda info --envs

python setup.py install

## Push to git hub
ssh-keygen -o