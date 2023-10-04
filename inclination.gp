$Mydata << EOD
#tf freq_max freq_grid
2.0 145 159
2.5 156 165
3.0 168 175
3.5 185 189
4.0 206 209
4.5 237 239
4.75 260.89 262.11
5.0 294.65 295.43
5.25 353.57 353.88
5.5 551.123 551.098
6 3248.19 3248.69
7 3248 3248
8 3248 3248
10 3248 3248
EOD
set xlabel 'kHz/s'
set ylabel '$f(\unit\hertz)$'
stats $Mydata using 1:2
plot $Mydata using (5.0/$1):2 with lines notitle

# gp-size 12cm,7cm