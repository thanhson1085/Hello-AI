#!/bin/bash

for i in `seq 10 20`; do
    python run.py dataset/test_set/dogs/dog.40$i.jpg
    python run.py dataset/test_set/cats/cat.40$i.jpg
done
