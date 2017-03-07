#!/bin/bash
python retrain.py --bottleneck_dir=tmp/bottlenecks --how_many_training_steps 500 --model_dir=tmp/inception --output_graph=output/retrained_graph.pb --output_labels=output/retrained_labels.txt --image_dir=dataset/training_set/
