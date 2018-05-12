sudo apt-get update
sudo apt-get upgrade

# NECESSARY FOR DJANGO
sudo apt-get install -y python3-dev python3-pip
sudo pip3 install Django

# NECESSARY FOR PYTORCH
sudo apt-get install -y build-essential cmake gfortran pkg-config
sudo apt-get install -y software-properties-common wget vim
sudo apt-get autoremove
sudo apt-get update
sudo apt-get install -y libprotobuf-dev libleveldb-dev libsnappy-dev libhdf5-serial-dev protobuf-compiler libopencv-dev
sudo apt-get install -y --no-install-recommends libboost-all-dev doxygen
sudo apt-get install -y libgflags-dev libgoogle-glog-dev liblmdb-dev libblas-dev
sudo apt-get install -y libatlas-base-dev libopenblas-dev libgphoto2-dev libeigen3-dev libhdf5-dev
sudo pip3 install http://download.pytorch.org/whl/cpu/torch-0.3.1-cp35-cp35m-linux_x86_64.whl
sudo pip3 install torchvision

# OTHER
sudo apt-get install -y git python3-nose python3-numpy python3-scipy
