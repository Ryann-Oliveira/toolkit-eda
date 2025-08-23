import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def readable(plot, title: bool = False):
    '''
    Aplica configurações para facilitar a legibilidade de um gráfico.
    Argumentos:
    plot -> Função que cria o gráfico
    title -> Se a função requisitará input com o título
    '''
    plt.figure(figsize=(16,8))
    plot()
    if title is True:
        title_str = input('Plot Title: ')
        if len(title_str) != 0:
            plt.title(title_str)
        else:
            pass
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

def disp_analysis(column: pd.Series):
    '''
    Calcula os outliers do conjunto via análise de dispersão.
    Argumentos:
    column -> Coluna do dataframe
    '''
    # Valores até o limite do quartil inferior (25%)
    Q1 = column.quantile(.25)
    
    # Valores até o limite do quartil médio-superior (75%)
    Q3 = column.quantile(.75)

    # Cálculo do intervalo interquartil (IQR)
    IQR = Q3 - Q1
    
    # Definição dos limites dentro dos quais os valores são normais. Fora disso são outliers.
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    
    # Cria a series booleana com todos os outliers da coluna
    outliers = (column < limite_inferior) | (column > limite_superior)
    return outliers

def zscores(column: pd.Series, limit: int = 3):
    '''
    Calcula os outliers do conjunto via z-score.
    Argumentos:
    column -> Coluna do dataframe
    limit -> Limite a partir do qual os valores serão considerados outliers
    '''
    zscores = (column - np.mean(column)) / np.std(column)
    outliers_mask = np.abs(zscores) > limit
    return outliers_mask
