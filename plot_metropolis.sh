#/bin/bash

name=$1
output=$name.dat
png=$name.png
./metropolis.py > $output
gnuplot << EOF
set xrange [-4:4]
set yrange [0:10]
set size ratio -1
set terminal pngcairo enhanced
set output "$png"
p x**2/2+3 t "boundary", "$output" u 1:2 w l t "trajectory"
EOF

