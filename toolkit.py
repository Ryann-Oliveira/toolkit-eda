import pandas as pd
import matplotlib.pyplot as plt

def readable(plot):
    '''
    Aplica configurações para facilitar a legibilidade de um gráfico.
    '''
    plt.figure(figsize=(16,8))
    plot()
    plt.title(input("Title: "))
    plt.show()

def col_values(df: pd.DataFrame, max_unique: int = 20):
    '''
    Exibe os valores únicos de cada coluna.
    '''
    for col in df.columns:
        print(f'Coluna {col}')
        quant_unicos = len(df[col].unique())
        if quant_unicos <= max_unique:
            print(f'Únicos:\n{df[col].unique()}')
        else:
            print(f'Quantidade excede max_unique ({max_unique})\nÚnicos: {quant_unicos} valores.')
        print(f'Total de valores:\n{df[col].value_counts()}')
        print('- ' * 20)
