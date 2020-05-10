
last_line=''
with open('data.txt') as f:
    for line in f:
        pass
    last_line = line
array_dim = int(last_line.split('\t')[0])

line_count = file_len('data.txt') - 3
mat = [x[:] for x in [[0] * array_dim] * array_dim]

f = open('data1.txt','r')
for line in f:
    print("Processing line : {}".format(line))
    if line.startswith('#'):
        print('skipping line as it is a comment')
        continue
    node1 = int(line.split('\t')[0])
    node2 = int(line.rstrip('\n').split('\t')[1])
    mat[node1][node2] = 1
