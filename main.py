import matplotlib.pyplot as plt

effort = []
runs = []

def foo(file):
    lines = file.readlines()
    whole = []
    del effort[:]
    del runs[:]


    for x in lines:
        whole.append(x.split(','))

    for y in range(1, 201):
        whole[y][-1] = whole[y][-1].rstrip()

        for z in range(1, 34):
            whole[y][z] = float(whole[y][z])

        effort.append(whole[y][1])
        runs.append(sum(whole[y][2:]) / len(whole[y][2:]))

def main():
    evolrs1 = open('rsel.csv', 'r')
    foo(evolrs1)
    evolrs1.close()
    plt.plot(effort, runs, 'b', label='1-Evol-RS')

    coevrs1 = open('cel-rs.csv', 'r')
    foo(coevrs1)
    coevrs1.close()
    plt.plot(effort, runs, 'g', label='1-Coev-RS')

    coevrs2 = open('2cel-rs.csv', 'r')
    foo(coevrs2)
    coevrs2.close()
    plt.plot(effort, runs, 'r', label='2-Coev-RS')

    coev1 = open('cel.csv', 'r')
    foo(coev1)
    coev1.close()
    plt.plot(effort, runs, 'k', label='1-Coev')

    coev2 = open('2cel.csv', 'r')
    foo(coev2)
    coev2.close()
    plt.plot(effort, runs, 'm', label='2-Coev')

    plt.legend()
    plt.xlim(0,500000)
    plt.ylim(0.6, 1)
    plt.xlabel('Rozegranych gier')
    plt.ylabel('Odsetek wygranych gier')
    plt.savefig('Wykres_generated.pdf')
    plt.close()

if __name__ =='__main__':
    main()
