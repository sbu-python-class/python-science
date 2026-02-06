#!/bin/sh

KERAS_BACKEND="torch" jupyter-book build content

cd content/_build/html
for i in $(grep -lR "# alt-text" | grep html)
do
  echo $i
  ../../../parse_alt.py $i
done
