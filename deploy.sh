#!/bin/bash

echo "Stopping donut-detector daemon..."
sudo stop donut-detector

echo "Cleaning directory..."
python setup.py clean
sudo rm -rf src/*.egg-info/

echo "Running python setup.py sdist"
python setup.py sdist

echo "Installing Donut Detector"
sudo python setup.py install

echo "Starting donut-detector daemon..."
sudo start donut-detector
