import sys

fa = sys.argv[1]
start = sys.argv[2]
option = sys.argv[3]
output = sys.argv[4]

def parseFasta(file):
    with open(file) as f:
        seq = []
        while True:
            line = f.readline().rstrip()
            if not line:
                break
            if line[0] != ">":
                seq.append(line)
    return "".join(seq)

def mutateSeq(fasta, cnt, opt):
    all_aa = "GALMFWKQESPVICYHRNDT"
    mut_list = []
    for i in range(len(fasta)):
        cnt += 1
        for j in range(len(all_aa)):
            if fasta[i] == all_aa[j]:
                continue
            else:
                if opt == "1":
                    mut_list.append(str(fasta[i])+"A"+str(cnt)+str(all_aa[j])+";")
                if opt == "2":
                    mut_list.append(str(fasta[i])+"A"+str(cnt)+str(all_aa[j])+","+
                                    str(fasta[i])+"B"+str(cnt)+str(all_aa[j])+";")
                if opt == "3":
                    mut_list.append(str(fasta[i])+"A"+str(cnt)+str(all_aa[j])+","+
                                    str(fasta[i])+"B"+str(cnt)+str(all_aa[j])+","+
                                    str(fasta[i])+"C"+str(cnt)+str(all_aa[j])+";")
    with open(output, "w") as f:
        for mut in mut_list:
            f.write(str(mut) + "\n")
    return

protein_seq = parseFasta(fa)
mutations = mutateSeq(protein_seq, int(start), option)