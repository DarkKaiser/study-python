import os.path
import pandas as pd

def crawling():
    for idx in range(1, 50):
        # 데이터 추출
        df = pd.read_html(f'https://finance.naver.com/sise/sise_market_sum.naver?&page={idx}', encoding='euc-kr')[1]
        df.dropna(axis='index', how='all', inplace=True)
        df.dropna(axis='columns', how='all', inplace=True)
        if len(df) == 0:
            break

        # 파일 저장
        f_name = 'sise.csv'
        if os.path.exists(f_name):
            df.to_csv(f_name, encoding='utf-8-sig', index=False, mode='a', header=False)
        else:
            df.to_csv(f_name, encoding='utf-8-sig', index=True)

        print(f'{idx} 페이지 완료')


if __name__ == '__main__':
    crawling()
