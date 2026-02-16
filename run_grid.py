import os

m1list = [0.02, 0.05, 0.1, 0.2, 0.5, 1., 2., 5., 10., 20., 30., 40., 50., 75., 100., 200.]
dmlist = [0.1, 0.2, 0.4]

#m1list = [0.5, 1., 2., 5., 10., 20., 30., 40., 50., 75., 100., 200.]
#dmlist = [0.01, 0.05]

#m1list = [0.05, 0.1, 0.2]
#dmlist = [0.05]

for m1 in m1list:
    for dm in dmlist:

        os.system(f'python3 makeGridpack_run3.py {m1} {dm} 1jet')
            
