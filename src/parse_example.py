#!/usr/bin/env python

from __future__ import print_function

import gzip
import argparse
import dataset_infocom2019_pb2 as pb
from google.protobuf.internal.decoder import _DecodeVarint32

def open_pb(fname):
    networks = []
    with gzip.open(fname, "rb") as f:
        while True:
            buf = f.read(4)
            if len(buf) == 0:
                break
            size, pos = _DecodeVarint32(buf, 0)
            net = pb.Network()
            net.ParseFromString(buf[pos:] + f.read(size - (4 - pos)))
            networks.append(net)
    return networks


def main(path):
    print("Parsing", path)
    networks = open_pb(path)
    print("Parsed {} networks".format(len(networks)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str)
    args = parser.parse_args()
    main(args.path)
