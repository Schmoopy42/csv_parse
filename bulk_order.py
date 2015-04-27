#!/usr/bin/python

import csv

def bulk_orders(account_name):
    # same account
    # same symbol
    # if time between child orders are <= 60 seconds
    print "test"

def main():
    with open('TestOrderData.csv', 'rb') as f:
        reader = csv.reader(f)

        rownum = 0
        # Iterate through rows
        for row in reader:
            if( rownum != 0 ):
                this_acct = row[2]
                if( this_acct == prev_acct ):
                    # stuff

                else:




            elif( rownum == 0 ):
                header = row

            rownum +=1

        f.close()

main()
