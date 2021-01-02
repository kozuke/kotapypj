import pandas as pd


def main():
    df_tran = pd.read_csv('/Users/kota-ishizuka/localdev/kotapypj/src/kozuke/etfcalc/PaymentRecords.csv',
                          encoding='shift-jis')
    df_tran['約定単価'] = df_tran['約定単価'].str.replace('USD', '').astype(float)
    df_tran['受渡金額'] = df_tran['受渡金額'].str.replace('[円|,]', '').astype(int)
    df_tran['国内約定月'] = pd.to_datetime(df_tran['国内約定日']).dt.strftime('%Y/%m')
    df_grouped_tran = df_tran.groupby(['国内約定月', '銘柄コード']).agg('sum').reset_index()
    df_grouped_tran = df_grouped_tran.sort_values(['国内約定月', '銘柄コード'])
    df_grouped_tran.to_csv('output.csv', encoding='shift-jis', index=False)


if __name__ == '__main__':
    main()
