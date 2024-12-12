#!/bin/bash

path=$(pwd)/$1
alphabet=$2
size=$3

for count in {0..12}
do
	echo "\nIniciando arquivo $count"
	pdf2john $path/pdf$count.pdf > hashes/hash_$count.txt
	time john --increment=$2 --lenght=$3 hashes/hash_$count.txt
done
