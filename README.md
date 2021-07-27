# DeepTMA: Predicting Effective Contention Models for Network Calculus using Graph Neural Networks

This repository contains the dataset used for the paper [_"DeepTMA: Predicting Effective Contention Models for Network Calculus using Graph Neural Networks"_](https://dx.doi.org/10.1109/INFOCOM.2019.8737496) publish at the [38th IEEE International Conference on Computer Communications (INFOCOM 2019)](http://infocom2019.ieee-infocom.org/). We refer to the paper for a full explanation of the methodology used for generating the dataset.


## Getting the dataset

The dataset is stored in the git repository using [git lfs](https://git-lfs.github.com/). Install git lfs on your system first and then clone the repository using:

```
$ git lfs clone https://github.com/fabgeyer/dataset-infocom2019.git
```

## Reading the dataset

Each file is encoded using [Protocol Buffers](https://developers.google.com/protocol-buffers/). The data structure is defined in `dataset_infocom2019.proto` and can be compiled to various target languages (e.g. Java, Python, Objective-C, and C++) using the `protoc` command line utility.

### Example code in python

The script `src/parse_example.py` contains an example of how to parse the protobuf files using python.
We first compile the `.proto` file to python:

```
$ sudo apt install python3-protobuf
$ git clone https://github.com/fabgeyer/dataset-infocom2019
$ cd dataset-infocom2019
$ protoc --python_out=src dataset.proto
$ python src/parse_example.py dataset/dataset.part0.pb.gz
```

## Citation

If you use this dataset for your research, please include the following reference in any resulting publication:

```bibtex
@inproceedings{GeyerBondorf_INFOCOM2019,
	author    = {Geyer, Fabien and Bondorf, Steffen},
	title     = {{DeepTMA}: Predicting Effective Contention Models for Network Calculus using Graph Neural Networks},
	booktitle = {Proceedings of the 38th IEEE International Conference on Computer Communications (INFOCOM)},
	year      = {2019},
	month     = apr,
	address   = {Paris, France},
	doi       = {10.1109/INFOCOM.2019.8737496},
}
```

## License

The data in this repository is licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/).
