from collections import namedtuple
from util import whole_file, chunker

File = namedtuple("File", "pos len")
Empty = namedtuple("Empty", "pos len")
Filesystem = namedtuple("Filesystem", "mem files empties")

def parse_fs(path):
    fs = Filesystem([], [], [])
    for file_id, (file_len, empty_len) in enumerate(chunker(whole_file(path), 2)):
        fs.files.append(File(len(fs.mem), int(file_len)))
        fs.mem.extend([file_id] * int(file_len))
        fs.empties.append(Empty(len(fs.mem), int(empty_len)))
        fs.mem.extend(['.'] * int(empty_len))
    return fs

def inplace_checksum(fs):
    rights = (r for r in range(len(fs.mem) - 1, 0, -1) if fs.mem[r] != '.')
    checksum, left, right = 0, 0, next(rights)
    while left <= right:
        if fs.mem[left] == '.':
            checksum += left * fs.mem[right]
            right = next(rights)
        else:
            checksum += left * fs.mem[left]
        left += 1
    return checksum

def defrag(fs):
    for file in reversed(fs.files):
        for empty in fs.empties:
            if empty.pos > file.pos: break
            if file.len <= empty.len:
                empty_slice = slice(empty.pos, empty.pos + file.len)
                file_slice = slice(file.pos, file.pos + file.len)
                fs.mem[empty_slice] = fs.mem[file_slice]
                fs.mem[file_slice] = ["."] * file.len

                empty_index = fs.empties.index((empty.pos, empty.len))
                if file.len < empty.len:
                    fs.empties[empty_index] = Empty(empty.pos + file.len, empty.len - file.len)
                else:
                    fs.empties.pop(empty_index)
                break

filesystem = parse_fs("input.txt")
p1 = inplace_checksum(filesystem)
defrag(filesystem)
p2 = sum(idx * entry for idx, entry in enumerate(filesystem.mem) if entry != ".")

print(f"part1: {p1}, part2: {p2}")
