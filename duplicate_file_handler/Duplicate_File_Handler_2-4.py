import sys
import os


def check_input():
    print("\nEnter a sorting option:")
    option = int(input())
    if option in [1, 2]:
        return option
    else:
        print("\nWrong option")
        return check_input()


def check_files(args, fformat):
    flist = {}
    for root, _, files in os.walk(args[1], topdown=True):
        for name in files:
            if '.{}'.format(fformat) in name:
                fpath = os.path.join(root, name)
                fsize = os.path.getsize(fpath)
                if fsize in flist:
                    flist[fsize].append(fpath)
                else:
                    flist[fsize] = [fpath]
    return flist


def main():
    args = sys.argv
    if len(args) < 2:
        return print("Directory is not specified")
    print("\nEnter file format:")
    fformat = input()
    print('Size sorting options:\n1. Descending\n2. Ascending\n')
    option = int(check_input())
    filtered_flist = check_files(args, fformat)
    if option == 1:
        filtered_flist = dict(sorted(filtered_flist.items(), reverse=True))
    elif option == 2:
        filtered_flist = dict(sorted(filtered_flist.items(), reverse=False))

    for file in filtered_flist:
        print(f"{file} bytes", *filtered_flist[file], sep="\n", end="\n\n")   

main()