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


def check_files(root_folder, fformat):
    flist = {}
    for root, _, files in os.walk(root_folder, topdown=True):
        for name in files:
            if '.{}'.format(fformat) in name:
                fpath = os.path.join(root, name)
                fsize = os.path.getsize(fpath)
                if fsize in flist:
                    flist[fsize].append(fpath)
                else:
                    flist[fsize] = [fpath]
    return flist


def output_duplicates(duplicates):
    counter = 1 # overall duplicate files counter
    size = None
    ordered_duplicates = {} # create a new list to reference a file by sequence number
    for key, files in duplicates.items():
        hash = key[1]
        if size == key[0]: # if hash is different but size is the same just print new hash
            print(f'Hash: {hash}')
        else:
            size = key[0]   
            print(f"\n{size} bytes\nHash: {hash}") 
        for file in files:
            print(f'{counter}. {file}')
            ordered_duplicates.update({str(counter): (file, size)}) 
            counter += 1
    return ordered_duplicates

def calculate_hash(filtered_flist):
    duplicate_flist = {k: v for (k, v) in filtered_flist.items() if len(v) > 1}
    hash_table = {}

    for size, files in duplicate_flist.items():
        for file in files:
            with open(file, 'rb') as f:
                hash_md5 = hashlib.md5()
                for chunk in iter(lambda: f.read(65536), b""): #divide file in chunks for better perfomance of hash function
                    hash_md5.update(chunk)
                hash = hash_md5.hexdigest()
                if (size, hash) in hash_table:
                    hash_table[(size, hash)].append(file) 
                else:
                    hash_table.update({(size, hash): [file]})
    
    duplicate_hash = {k: v for (k, v) in hash_table.items() if len(v) > 1}
    ordered_duplicates = output_duplicates(duplicate_hash)
    return ordered_duplicates 

def delete_duplicates(ordered_duplicates):
    numbers_to_delete = input().split(' ')
    total_freespace = 0
    
    for n in numbers_to_delete:
        if n not in ordered_duplicates.keys():
            print("\nWrong format\n")
            return delete_duplicates(ordered_duplicates)
    
    for n in numbers_to_delete:
        path = ordered_duplicates[n][0]
        size = ordered_duplicates[n][1]
        os.remove(path)
        total_freespace += size

    print(f'Total freed up space: {total_freespace} bytes')

def check_answer():
    answer = input()
    if answer == 'yes':
        return True
    elif answer == 'no':
        return False
    else:
        print("Wrong option")
        return check_answer()


def main(root_folder):
    print("\nEnter file format:")
    fformat = input()
    print('Size sorting options:\n1. Descending\n2. Ascending\n')
    option = int(check_input())
    filtered_flist = check_files(root_folder, fformat)
    if option == 1:
        filtered_flist = dict(sorted(filtered_flist.items(), reverse=True))
    elif option == 2:
        filtered_flist = dict(sorted(filtered_flist.items(), reverse=False))

    for file in filtered_flist:
        print(f"{file} bytes", *filtered_flist[file], sep="\n", end="\n\n")   

    duplicates_list = {}
    print("Check for duplicates?")
    if check_answer() == True:
        duplicates_list = calculate_hash(filtered_flist)
    else:
        return

    print("Delete files?")
    if check_answer() == True:
        delete_duplicates(duplicates_list)
    else:
        return

if __name__ == "__main__":
    try:
        root_folder = sys.argv[1]
    except IndexError:
        print("Directory is not specified")
        sys.exit()
    else:
        main(root_folder)
