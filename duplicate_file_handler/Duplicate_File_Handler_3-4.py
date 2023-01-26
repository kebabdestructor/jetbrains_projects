import sys
import os
import hashlib


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

def print_duplicates(duplicates):
    counter = 1
    size = None
    for key, files in duplicates.items():
        hash = key[1]
        if size == key[0]:
            print(f'Hash: {hash}')
        else:
            size = key[0]   
            print(f"\n{size} bytes\nHash: {hash}") 
        for file in files:
            print(f'{counter}. {file}')
            counter += 1

def check_hash(filtered_flist):
    duplicate_flist = {k: v for (k, v) in filtered_flist.items() if len(v) > 1}
    hash_table = {}

    for size, files in duplicate_flist.items():
        for file in files:
            with open(file, 'rb') as f:
                hash_md5 = hashlib.md5()
                for chunk in iter(lambda: f.read(65536), b""):
                    hash_md5.update(chunk)
                hash = hash_md5.hexdigest()
                if (size, hash) in hash_table:
                    hash_table[(size, hash)].append(file)
                else:
                    hash_table.update({(size, hash): [file]})
    
    duplicate_hash = {k: v for (k, v) in hash_table.items() if len(v) > 1}
    print_duplicates(duplicate_hash)

def check_duplicates():
    answer = input()
    if answer == 'yes':
        return True
    elif answer == 'no':
        return False
    else:
        print("Wrong option")
        return check_duplicates()

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

    print("Check for duplicates?")

    if check_duplicates():
        check_hash(filtered_flist)
    else:
        return

main()