from pathlib import Path
# file operations in python 

# opening files in python 
file = open('stock.txt', 'r') # opening the file for reading
file = open('stock.txt', 'w') # open file for writing - i.e overwriting over the already written content 
file = open('stock.txt', 'a') #open the file for appending

# other common Modes of file operations :

# 'r+' : Read and write
# 'b' : Binary mode (add to other modes like 'rb' or 'wb')



#---------------reading files 
#read entire file 
with open('stock.txt', 'r') as file:
  readContent = file.read()




#-------------------------------------- writing file content
with open('stock.txt', 'w') as file:
  file.write('stock lists showing')

#writing multiple lines 
with open('stock.txt', 'w') as file:
  file.writelines(['this is line first ', 'this is the second line ', 'stock list goes brrr '])



#creating a file with data 
 
stock_data = '''Date,Symbol,Open,High,Low,Close,Volume
2024-01-01,AAPL,185.34,187.22,184.21,186.95,25678900
2024-01-02,AAPL,186.54,188.45,185.78,187.82,28945600
2024-01-03,AAPL,187.82,189.56,186.90,188.23,30123400
2024-01-01,GOOGL,138.45,140.32,137.89,139.78,15678300
2024-01-02,GOOGL,139.78,141.23,139.12,140.56,17834500
2024-01-03,GOOGL,140.56,142.67,140.12,142.34,19234600
2024-01-01,MSFT,372.65,375.23,371.45,374.67,12567800
2024-01-02,MSFT,374.67,377.89,373.56,376.45,14523900
2024-01-03,MSFT,376.45,378.90,375.67,377.89,16234500
'''

with open('stock.txt', 'w') as file:
  file.write(stock_data)
  #now the stock data will filled in the stock.txt file when this file is runned


#now readin this file line by line and only printing AAPL stocks 
with open('stock.txt', 'r') as file:
  for line in file:
    if 'AAPL' in line:
      print(line.strip())


# appending new data in stock file 

new_stock = '2024-01-04,AAPL,188.23,190.45,187.89,189.67,29876500\n'

with open('stock.txt', 'a') as file:
  file.write(new_stock)

#finding highest volume day
with open('stock.txt', 'r') as file:
    next(file)  # Skip header
    max_volume = 0
    max_volume_line = ''
    
    for line in file:
        data = line.strip().split(',')
        volume = int(data[6])
        if volume > max_volume:
            max_volume = volume
            max_volume_line = line
            
    print(f"Highest volume day: {max_volume_line}")

#----------------------------------------------------------------------------------------------------------
#using with statement - using 'with' automatically closes the file after use 
with open('stock.txt', 'r') as file:
  content = file.read()


# error handling in file operations 

try: 
  with open('stock.txt', 'r') as file:
    readIt = file.read()
    # print(readIt)
except FileNotFoundError:
  print('The file doesn not exist')
except IOError:
  print('Error readin the file')




