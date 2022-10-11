with open('solution.py', 'r') as fin:
    with open('out.txt', 'w') as fout:
        line = fin.readline()
        while not line.startswith('# ---end----'):
            if line.startswith('# title'):
                title = ' '.join(line.split('# title')[1:]).strip()
                fout.write(f'+ [{title}]({"-".join(title.lower().split(" "))})\n')
                fout.write('\n')
                fout.write(f'## {title}\n')
                fout.write('\n')

            if line.startswith('# description'):
                description = ' '.join(line.split('# description')[1:]).strip()
                fout.write(description + '\n')
                fout.write('\n')

            line = fin.readline()

        fout.write(f'```python\n{"".join(fin.readlines()).strip()}\n```')