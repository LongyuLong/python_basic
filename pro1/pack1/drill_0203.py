print("\n\nFunction Q1. 키보드를 통해 직원 자료를 입력받아 가공 후 출력하기") ## 복습

def inputfunc():
    datas = [
    [1, "강나루", 1500000, 2010],
    [2, "이바다", 2200000, 2018],
    [3, "박하늘", 3200000, 2005],
    ]
    return datas

def processfunc(datas):
    for data in datas:
        number = data[0]
        name = data[1]
        salary = data[2]
        year = 2026-data[3]
        
        # print(data)
        if year < 4:
            sudang = 150000
        elif year >= 4 and year < 9:
            sudang = 450000
        elif year >= 9:
            sudang = 1000000

        monthly = salary + sudang
        if monthly >= 3000000:
            tax = 0.5 * monthly
            getmoney = monthly - tax
        elif monthly >= 2000000:
            tax = 0.3 * monthly
            getmoney = monthly - tax
        elif monthly < 2000000:
            tax = 0.15 * monthly
            getmoney = monthly - tax            
        final = [number, name, salary, year, sudang, tax, getmoney]

        print(final)
    return

processfunc(inputfunc())

print("\n연습문제2) 리스트를 통해 상품 자료를 입력받아 가공 후 출력하기")

print()

