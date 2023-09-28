fn = 'mobavg_test.dat'
set yrange [0:1.1]
set xlabel '$t$(s)'

plot \
     fn using 1:2 with lines title 'MAF',\
     fn using 1:3 with lines title 'LPF: $\tau = 1/\omega$', \
     fn using 1:4 with lines title 'LPF: $\tau = 1/(2\omega$)', \
     fn using 1:5 with lines title 'LPF: $\tau = 1/(3\omega$)', \
     fn using 1:6 with lines title 'LPF: $\tau = 1/(5\omega$)'

# gp-size: 12cm,8cm
