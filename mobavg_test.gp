fn = 'mobavg_test.dat'
set yrange [0:1.1]
set xlabel '$t$(s)'

plot \
     fn using 1:2 with lines title 'MAF',\
     fn using 1:3 with lines title 'LPF ($\tau = T$)', \
     fn using 1:4 with lines title 'LPF ($2\, \tau = T$)', \
     fn using 1:5 with lines title 'LPF ($3\, \tau = T$)', \
     fn using 1:6 with lines title 'LPF ($5\, \tau = T$)'

# gp-size: 12cm,8cm
