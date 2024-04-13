import csv

s = 'eval/img/'
with open('dataset.imgs','w') as f:

    for i in range(1,498):

        name =  str(i) + ',' + s + "{:04}".format(i-1) + '1.png\n'
        # print(name)
        f.writelines(name)