stocks = {
    "info": [600, 630, 620],
    "mtl": [1430, 1490, 1567],
    "ril": [234, 180, 160]
}

opt = int(input("Enter your option (1 for average, 2 for insert/update): "))

if opt == 1:
    for k, v in stocks.items():
        avg = sum(v) / len(v)
        print(k, "==>", v, "==> avg:", avg)

elif opt == 2:
    stock_name = input("Enter stock sticker (e.g. info, mtl, newone): ").lower()
    stock_price = int(input("Enter stock price: "))

    if stock_name in stocks:
        stocks[stock_name].append(stock_price)
    else:
        stocks[stock_name] = [stock_price]

    print("Updated stock data:")
    print(stock_name, "==>", stocks[stock_name])

else:
    print("Invalid option.")