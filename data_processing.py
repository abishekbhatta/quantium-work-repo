import csv

# Process each record in the provided CSV file and write specific data to a new file

def processing(csv_file):
    # Open the input file for reading and the output file for appending
    with open(csv_file, mode= 'r') as read_file, open('processed-data.csv', mode='a') as write_file:

        csv_reader = csv.reader(read_file, delimiter=',')  
        csv_writer = csv.writer(write_file, delimiter=',') 

        next(csv_reader) #skip the header row

        # Iterate over each row in the input file
        for row in csv_reader:
            food = row[0]
            if food == 'pink morsel': # Filter rows where the food item is 'pink morsel'

                #calculate sales and extract date and region
                sales = float(row[1].strip('$')) * int(row[2])
                date = row[3]
                region = row[4] 
                # Write the processed data to the output file
                csv_writer.writerow([sales, date, region])





