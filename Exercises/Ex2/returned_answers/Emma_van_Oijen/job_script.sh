#!/bin/bash

for i in {1..10}; do
  ./output "$i" > "output_$i.txt" &
done
wait
