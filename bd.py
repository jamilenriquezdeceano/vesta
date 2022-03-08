
from typing import List
from datetime import date

today = date.today()
today_format = today.strftime("%d/%m/%Y")

current_day=[
 {"id":1, "user":1, "symbol":"AAPL", "qty":2, "price":160.50, "total":321.00, "hour":9,"date":today_format},
 {"id":2, "user":1, "symbol":"AAPL", "qty":2, "price":150.50, "total":301.00, "hour":10,"date":today_format},
 {"id":3, "user":1, "symbol":"AAPL", "qty":1, "price":100.00, "total":100.00, "hour":11,"date":today_format},
 {"id":4, "user":1, "symbol":"AAPL", "qty":2, "price":100.00, "total":200.00, "hour":12,"date":today_format},
 {"id":5, "user":1, "symbol":"AAPL", "qty":2, "price":160.50, "total":321.00, "hour":13,"date":today_format},
 {"id":6, "user":1, "symbol":"AAPL", "qty":2, "price":150.50, "total":301.00, "hour":14,"date":today_format},

]

buy_table=[
 {"id":1, "user":1, "symbol":"AAPL", "qty":2, "price":160.50, "total":321.00, "date":"5/03/2022"},
 {"id":2, "user":1, "symbol":"AAPL", "qty":2, "price":150.50, "total":301.00, "date":"5/03/2022"},
 {"id":3, "user":1, "symbol":"AAPL", "qty":1, "price":100.00, "total":100.00, "date":"6/03/2022"},
 {"id":4, "user":1, "symbol":"AAPL", "qty":2, "price":100.00, "total":200.00, "date":"6/03/2022"},
 {"id":5, "user":1, "symbol":"AAPL", "qty":2, "price":160.50, "total":321.00, "date":"7/03/2022"},
 {"id":6, "user":1, "symbol":"AAPL", "qty":2, "price":150.50, "total":301.00, "date":"7/03/2022"},
 {"id":7, "user":1, "symbol":"AAPL", "qty":1, "price":100.00, "total":100.00, "date":"8/03/2022"},
 {"id":8, "user":1, "symbol":"AAPL", "qty":2, "price":100.00, "total":200.00, "date":"8/03/2022"},
 {"id":9, "user":1, "symbol":"GOOG", "qty":2, "price":160.50, "total":321.00, "date":"5/03/2022"},
 {"id":10, "user":1, "symbol":"GOOG", "qty":2, "price":150.50, "total":301.00, "date":"5/03/2022"},
 {"id":11, "user":1, "symbol":"GOOG", "qty":1, "price":100.00, "total":100.00, "date":"6/03/2022"},
 {"id":12, "user":1, "symbol":"GOOG", "qty":2, "price":100.00, "total":200.00, "date":"6/03/2022"},
 {"id":13, "user":1, "symbol":"GOOG", "qty":2, "price":160.50, "total":321.00, "date":"7/03/2022"},
 {"id":14, "user":1, "symbol":"GOOG", "qty":2, "price":150.50, "total":301.00, "date":"7/03/2022"},
 {"id":15, "user":1, "symbol":"GOOG", "qty":1, "price":100.00, "total":100.00, "date":"8/03/2022"},
 {"id":16, "user":1, "symbol":"GOOG", "qty":2, "price":100.00, "total":200.00, "date":"8/03/2022"}
]

def held_shares(data, symbol):
    sum_shares = 0
    for row in data:
        if(row["symbol"] == symbol):
            sum_shares = sum_shares + int(row["qty"])
    return sum_shares

def total_shares(data, symbol):
    total = 0
    for row in data:
        if(row["symbol"] == symbol):
            total = total + float(row["total"])
    return total

def profit_loss_in_percentage(symbol:str, current_price: float):
    percent = 0
    shares = held_shares(buy_table,"AAPL")  
    accumulated_total = total_shares(buy_table, "AAPL")
    current_total = shares * current_price
    percent = ((current_total - accumulated_total) * 100) / current_total
    print(percent)

profit_loss_in_percentage("AAPL", 400)




