import csv

#process each record of daily_sales_file into sales, date, region

def processing(csv_file):

    with open(csv_file, mode= 'r') as read_file, open('processed-data.csv', mode='a') as write_file:
        csv_reader = csv.reader(read_file, delimiter=',')  
        csv_writer = csv.writer(write_file, delimiter=',') 
        next(csv_reader)

        for row in csv_reader:
            food = row[0]
            if food == 'pink morsel':
                sales = float(row[1].strip('$')) * int(row[2])
                date = row[3]
                region = row[4]
                csv_writer.writerow([sales, date, region])


processing('data/daily_sales_data_0.csv')
processing('data/daily_sales_data_1.csv')
processing('data/daily_sales_data_2.csv')



