#!/bin/bash
py=`pwd`/home.py
cat<<EOF >> ~/.lldbinit
command script import $py
EOF