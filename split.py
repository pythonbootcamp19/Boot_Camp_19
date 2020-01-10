x = 'Uled by Mrstark\t2850\t1175'
clean_x = x.strip()
clean_x_splitted = clean_x.split("\t")
uploader_name = clean_x_splitted[0].split()[-1]
seeds = clean_x_splitted[1]
peers = clean_x_splitted[2]

print(uploader_name, seeds, peers)

#-----
# x = 'Uled by Mrstark\t2850\t1175'
# a = x.split(' ')
# print(len(a))
# print(a[0])
# print(a[-1])
