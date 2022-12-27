import re

with open(r'22_07.txt', 'r') as f:
    raw_lines = f.read().strip()

re_base   = re.compile('\$ cd \/')
re_cd     = re.compile('\$ cd (\w+)')
re_ls     = re.compile('\$ ls')
re_file   = re.compile('(\d+) (\w+\.?\w?)')
re_folder = re.compile('dir (\w+)')
re_dir_up = re.compile('\$ cd \.\.')

class Folder:
    def __init__(self, name, parent):
        self.name    = name
        self.parent  = parent
        self.files   = {}
        self.folders = []
        self.size    = None

    def create_folder(self, name):
        new_folder = Folder(name, self)
        self.folders.append(new_folder)
        return new_folder

    def create_file(self, name, size):
        self.files[name] = size

    def find_folder(self, name):
        folder = [folder for folder in self.folders if folder.name == name][0]
        return folder

    def __repr__(self):
        return self.name

    def print_folders(self, indentation=0, print_files=True):
        indent = '\t' * indentation
        print(indent, self)
        if print_files:
            for name, size in self.files.items():
                print(indent, f'{name}\t{size}')
        for folder in self.folders:
            folder.print_folders(indentation+1, print_files)

    def size_of_folder(self):
        if self.size:
            return self.size

        sum_ = sum(value for value in self.files.values())
        for folder in self.folders:
            sum_ += folder.size_of_folder()

        self.size = sum_

        return sum_

    def traverse_folders(self):
        yield self
        for folder in self.folders:
            yield from folder.traverse_folders()
        return

base_folder    = None
current_folder = None
reading_folder = False

for line in raw_lines.split('\n'):
    match reading_folder, line:
        case False, str if re_base.match(line):
            base_folder = Folder('/', None)
            current_folder = base_folder

        case False, str if re_ls.match(line):
            reading_folder = True

        case True, str  if re_folder.match(line):
            current_folder.create_folder(line.split(' ')[1])

        case True, str  if re_file.match(line):
            size, file_name = line.split(' ')
            current_folder.create_file(file_name, int(size))

        case _, str     if re_dir_up.match(line):
            reading_folder = False
            current_folder = current_folder.parent 
        
        case _, str     if re_cd.match(line):
            folder_name    = line.split(' ')[2]
            reading_folder = False
            current_folder = current_folder.find_folder(folder_name)

        case _, _:
            print(f'unhandled line {count}: {reading_folder}, {line}')
            break

# Calculate all sizes of folders
folder_generator = base_folder.traverse_folders()
folder_sizes = [folder.size_of_folder() for folder in folder_generator]

# Get list of all sizes of folders smaller than cap and sum them 
capped_folder_sizes = [folder_size for folder_size in folder_sizes if folder_size <= 100000]
print('Part 1 Sum: ', sum(capped_folder_sizes))

disk_size   = 70000000
update_size = 30000000

size_to_free = base_folder.size_of_folder() - (disk_size-update_size)

capped_folder_sizes = [folder_size for folder_size in folder_sizes if folder_size >= size_to_free]
capped_folder_sizes.sort()

print('Part 2 Smallest folder to delete:', capped_folder_sizes[0])
