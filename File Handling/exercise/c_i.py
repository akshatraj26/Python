# f = open('master_c_i.txt', 'w+')
# master = ['A101 Sanjay', 'A102 Ajay', 'A103 Anuja', 'A104 Akhil', 'A105 Bhushan', 'A106 Ankit', 'A107 Vivek',
#           'A108 Ankita', 'A109 Aditi', 'A110 Harsha']
# for student in master:
#     f.write(student + '\n')
# f.close()
#
# f = open('tran_c_i.txt', 'w')
# tran = ['A101 D', 'A105 D', 'A112 Dheeraj A', 'A105 Dilip A']
# for tra in tran:
#     assert f.write(tra + '\n')
#
# f.close()
#
# f = open('tran_c_i.txt', 'r')
# data = f.read()
# print(data)



fm = open('master_c_i.txt', 'r')
mdata = fm.readlines()
ft = open('tran_c_i.txt', 'r')
while True:
    trec = ft.readline()
    if trec == '':
        break
    tfields = trec.split()
    if len(tfields) == 2:
        count =0
        for record in mdata:
            mfields = record.split()
            if tfields[0] == mfields[0]:
                break

            count += 1
            del(mdata[count])
        if len(tfields) == 3:
            mdata.append(tfields[0] + '' + tfields[1] + '\n')
        print("mdata:- ", mdata)
        sdata = sorted(mdata)

        fp = open('processed.txt', 'w')
        for item in sdata:
            print(item)
            item = item.split()
            rec = item[0] + '' + item[1] + '\n'
            fp.write(rec)

fm.close()
ft.close()
fp.close()

