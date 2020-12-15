#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import mysql.connector
import robin_stocks as rs


targets = ['MSFT', 'SPY', 'BABA', 'AMZN', 'NDAQ', 'AAPL', 'TCEHY', 'AMD', 'GOOGL', 'NET', 'ENPH', 'ICLN', 'NVDA', 'PANW', 'JKS', 'LOW', 'PYPL',
           'SQ', 'RUN', 'FCEL', 'TSLA', 'BE', 'MRNA', 'CCL', 'NCLH', 'AAL', 'ACB', 'TWTR', 'DAL', 'FCAU', 'LUV', 'WORK', 'GPRO', 'PLAN', 'GEVO', 'DKNG']


def main():
    db = mysql.connector.connect(
        host=os.environ.get("MYSQL_HOST"),
        user=os.environ.get("MYSQL_USER"),
        password=os.environ.get("MYSQL_PASSWORD"),
        database=os.environ.get("MYSQL_DATABASE"),
        port=os.environ.get("MYSQL_PORT")
    )
    user = os.environ.get('RH_USER')
    password = os.environ.get('RH_PASS')
    rs.login(username=user,
             password=password,
             expiresIn=86400,
             by_sms=True)
    conn = db.cursor()
    data = []
    for ticker in targets:
        historical = rs.stocks.get_stock_historicals(
            ticker, interval='5minute', span='day')
        for row in historical:
            data.append((ticker, row['begins_at'].replace('T', ' ').replace('Z', ''), row['open_price'],
                         row['close_price'], row['high_price'], row['low_price'], row['volume'],))
    sql = "INSERT INTO `data` (`ticker`, `begins_at`, `open_price`, `close_price`, `high_price`, `low_price`, `volume`) VALUES (%s, %s, %s, %s, %s, %s, %s);"
    conn.executemany(sql, data)
    db.commit()


if __name__ == '__main__':
    main()
