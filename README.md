# TensorFlow-Model-Manager
My code for creating/interacting with tensorflow v2+ models on an M1 Mac

### Requirements
- Miniforge (For Arm based compatible python interpreting. This is instead of anaconda): https://github.com/conda-forge/miniforge
    - `bash Miniforge3-MacOSX-arm64.sh` on the installation path to install
- [environment.yml](https://raw.githubusercontent.com/mwidjaja1/DSOnMacARM/main/environment.yml) - included in this repo
    - `conda env create --file=environment.yml --name tf_m1` on the yml path
- You need a new python environment
    - `conda activate tf_m1` to create
- [Tensorflow](https://github.com/apple/tensorflow_macos/releases), such as [v0.1alpha3](https://github.com/apple/tensorflow_macos/releases/tag/v0.1alpha3)
    - `pip install --upgrade --force --no-dependencies https://github.com/apple/tensorflow_macos/releases/download/v0.1alpha3/tensorflow_addons_macos-0.1a3-cp38-cp38-macosx_11_0_arm64.whl https://github.com/apple/tensorflow_macos/releases/download/v0.1alpha3/tensorflow_macos-0.1a3-cp38-cp38-macosx_11_0_arm64.whl` this command takes care of the install
- Run `python` and run the command `import tensorflow as tf` and then `print(tf.__version__)` to verifiy install
- You're done with the required installs!

### Commands to remember
- `conda activate tf_m1` to create your python environment
- `conda deactive` to get out of the environment