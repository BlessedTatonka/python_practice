class TradeConverter:
    def __init__(self, input_file='input.txt', output_file='output.txt'):
        self.input_file = input_file
        self.output_file = output_file

    def fit(self):
        with open('input.txt', 'r') as fin:
            with open('output.txt', 'w') as fout: 
                text = fin.read()
                for transaction in text.split('BANK')[1:]:
                    fout.write(self.parse_transaction('BANK' + transaction))


    def parse_transaction(self, transaction):
        values = {}

        parsed = transaction.split('\n')
        for i in range(len(parsed)):
            if parsed[i].startswith('BANK'):
                values['BANK'] = float(parsed[i].split(' ')[1])
                values['PAIR'] = parsed[i + 2]
                values['CURRENCY'] = values['PAIR'].split('-')[1]
                values['START_PRICE'] = float(parsed[i + 6].split(' ')[1])
                values['TARGETS'] = {}
                for k, target in enumerate(parsed[i + 8].split(' ', 1)[1].split('; ')):
                    values['TARGETS'][f'target {k + 1}'] = {'TARGET': float(target)}

                values['STOP_PRICE'] = float(parsed[i + 10].split(' ')[1])


            break

        self.calculate_targets(values)

        return self.values_to_string(values)

    def calculate_targets(self, values):
        strategy_income = 0

        for i, key in enumerate(values['TARGETS'].keys()):
            values['TARGETS'][key]['Percent'] = values['TARGETS'][key]['TARGET'] / values['START_PRICE']
            values['TARGETS'][key]['Bank'] = values['TARGETS'][key]['Percent'] * values['BANK']
            values['TARGETS'][key]['Target size'] = \
                values['TARGETS'][key]['TARGET'] * values['BANK'] / values['START_PRICE'] / len(values['TARGETS'].keys())
            strategy_income += values['TARGETS'][key]['Target size']

        values['Strategy income'] = [strategy_income, strategy_income / values['BANK'] * 100 - 100]

    def values_to_string(self, values):
        res = ''
        res += f'BANK: {round(values["BANK"], 3)}\n'
        res += f'START_PRICE: {round(values["START_PRICE"], 3)}\n'
        res += f'STOP_PRICE: {round(values["STOP_PRICE"], 3)}\n'
        res += f'PAIR: {values["PAIR"]}\n\n'
        
        for key in values['TARGETS'].keys():
            res += f'{key}: {round(values["TARGETS"][key]["TARGET"], 3)} {values["CURRENCY"]}\n'
            res += f'Percent: {round(values["TARGETS"][key]["Percent"], 3)}\n'
            res += f'Bank: {round(values["TARGETS"][key]["Bank"], 3)} {values["CURRENCY"]}\n'
            res += f'Target size: {round(values["TARGETS"][key]["Target size"], 3)} {values["CURRENCY"]}\n\n'
            
        res += f'Strategy income: {round(values["Strategy income"][0], 3)}; ' + \
                f'percent: {round(values["Strategy income"][1], 3)}\n\n'

        res += '----------------------------------------------\n'

        return res

def main():
    tc = TradeConverter()
    tc.fit()
        

if __name__ == '__main__':
    main()