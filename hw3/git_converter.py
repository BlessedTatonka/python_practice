def prepare_title(line):
    title = ' '.join(line.split('# title')[1:]).strip()
    res = ''
    res += f'+ [{title}]({"-".join(title.lower().split(" "))})\n'
    res += '\n'
    res += f'## {title}\n'
    res += '\n'
    return res

def prepare_desc(line):
    description = ' '.join(line.split('# description')[1:]).strip()
    res = ''
    res += description
    res += '\n'
    res += '\n'
    return res

def append_to_md(path_to_solution, path_to_md):
    with open(path_to_solution, 'r') as fin:
        with open(path_to_md, 'a') as fout:
            fout.write('\n\n<!---next problem-->\n\n')
            line = fin.readline()
            while not line.startswith('# ---end----'):
                if line.startswith('# title'):
                    fout.write(prepare_title(line))

                if line.startswith('# description'):
                    fout.write(prepare_desc(line))

                line = fin.readline()

            fout.write(f'```python\n{"".join(fin.readlines()).strip()}\n```')
        
append_to_md('solution2.py', 'out.md')