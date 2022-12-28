
class StrategyDeal:
    def __init__(self, bank, entry, targets, close):
        self.__bank = bank
        self.__entry = entry
        self.__targets = targets
        self.__close = close
        
    def get_targets(self):
        return self.__targets

    def get_target_percents(self):
        percents = []
        for target in self.__targets:
            percents.append(round(target / self.__entry * 100 - 100, 3))

        return percents


    def get_target_banks(self):	
        target_banks = []
        percents = self.get_target_percents()

        for percent in percents:
            target_banks.append(round(self.__bank * (100 + percent) / 100, 3))
        
        return target_banks

    def __str__(self):
        res = ''
        res += f'BANK: {self.__bank}\n'
        res += f'START_PRICE: {self.__entry}\n'
        res += f'STOP_PRICE: {self.__close}\n'
        res += f'STOP_PERCENT: {round((self.__entry / self.__close - 1) * 100, 3)}%\n'
        res += f'STOP_BANK: {round(self.__bank * (1 - (self.__entry / self.__close - 1)), 3)}\n'

        res += '\n'

        percents = self.get_target_percents()
        target_banks = self.get_target_banks()

        for index, target in enumerate(self.get_targets()):
            res += f'{index + 1} target: {target}\n'
            res += f'Percent: {percents[index]}%\n'
            res += f'Bank: {target_banks[index]}\n'
            res += '\n'


        return res

def read_data(file_name):
    with open(file_name, 'r') as fin:
        data = fin.read()
        return data


def write_data(file_name, data):
    with open(file_name, 'w') as fout:
        fout.write(data)
    
    
def get_number(string):
    res = ''
    for item in string:
        if item.isdigit() or item == '.':
            res += item

    return float(res)

def parse_data(data):
    res = ''
    for deal in data.split('-----')[:-1]:
        bank, entry, close = None, None, None
        targets = []
        for line in deal.split('\n'):
            if 'Bank' in line:
                bank = get_number(line)
            elif 'Entry' in line:
                entry = get_number(line)
            elif 'Close' in line:
                close = get_number(line)
            elif 'Target' in line:
                for item in line.split()[1:]:
                    targets.append(get_number(item))

        sdeal = StrategyDeal(bank, entry, targets, close)
        res += str(sdeal)

        res += '-----\n\n'

    return res



def main():
    content = read_data('deals.txt')
    result = parse_data(content)
    write_data('out.txt', result)


if __name__ == '__main__':    
    main() 