import mysql.connector as myc
con = myc.connect(host='localhost',user='root',passwd='anshupal')

cursor = con.cursor()
cursor.execute("CREATE database IF NOT EXISTS cinema")
cursor.execute("USE cinema")

class SellTicket:
    def createSeat():
        cursor.execute("CREATE TABLE IF NOT EXISTS seats (row_seat decimal NOT NULL PRIMARY KEY, vacant_seat VARCHAR(130) NOT NULL)")
        cursor.execute("CREATE TABLE IF NOT EXISTS cust_info (name VARCHAR(20) NOT NULL, age INT(5) NOT NULL, gender VARCHAR(10), phone_no INT(20) NOT NULL, ticket_p INT(12), seat_num VARCHAR(3) NOT NULL)")
        cursor.execute("DELETE FROM seats")
        cursor.execute("DELETE FROM cust_info")
        print("Enter the number of rows: ")
        row = int(input())
        print("Enter the number of seats in a row: ")
        column = int(input())
        s = []
        for i in range(column):
            s.append(0)
        for i in range(row):
            sql = "INSERT INTO seats(row_seat, vacant_seat) values({},'{}')".format(i+1,s)
            cursor.execute(sql)
        
        con.commit()
        print("Rows And Columns Created!!!!")

    def showseats():
        sql = "SELECT * FROM seats"
        cursor.execute(sql)
        data = cursor.fetchall()
        d = eval(data[0][1])

        a = '  '
        for i in range(len(d)):
            a += ' '+ str(i + 1)
        print(a)

        for i in data:
            s = ''
            for j in eval(i[1]):
                if j==1:
                    s += ' B'
                elif j==0:
                    s += ' S'
            print((data.index(i)+1),s)

    def statistics():
        sql = "SELECT vacant_seat from seats"
        cursor.execute(sql)
        rec = cursor.fetchall()
        row_len = len(rec)
        col_len = len(eval(rec[0][0]))
        total_seat = row_len * col_len
        total_cost = 0
        if total_seat > 60:
            firsthalf = (total_seat//2)
            secondhalf = total_seat - firsthalf
            total_cost = (firsthalf*8)+(secondhalf*10)
        elif total_seat <= 60:
            total_cost = 60*10
        count = 0
        c_inc = 0

        sql_1 = "SELECT ticket_p from cust_info"
        cursor.execute(sql_1)
        rec1 = cursor.fetchall()
        for i in rec1:
            count += 1
            c_inc += int(i[0])
        percentage = (count/total_seat)*100
        print("Number of tickets sold: ", count)
        print("Percent of tickets sold: ", percentage)
        print("Current Cost: ", c_inc)
        print("Total Cost: ", total_cost)

    def user_info():
        sql = "SELECT * from cust_info"
        cursor.execute(sql)
        rec = cursor.fetchall()

        for i in rec:
            print("===========================")
            print("Name: ", i[0])
            print("Age: ", i[1])
            print("Gender: ", i[2])
            print("Phone: ", i[3])
            print("Ticket Cost: ", i[4])
            print("Seat Number: ", i[5])

    def user_specific_info(phone_num):
        sql = "SELECT * from cust_info WHERE phone_no = '%d'" % (phone_num)
        cursor.execute(sql)
        rec = cursor.fetchall()

        if rec:

            for i in rec:
                print("===========================")
                print("Name: ", i[0])
                print("Age: ", i[1])
                print("Gender: ", i[2])
                print("Phone: ", i[3])
                print("Ticket Cost: ", i[4])
                print("Seat Number: ", i[5])

        else:
            print("No Ticket with this phone number")

    


class TicketBooking:

    def bookTicket():
        print("Type Your Name: ")
        c_name = str(input("name = "))

        print("Type Your Age: ")
        c_age = int(input("age = "))

        print("Type Your Gender: ")
        c_gender = str(input("male or female = "))

        print("Type Your Phone Number: ")
        c_phone = str(input("Phone number = "))

        sql = "SELECT * from seats"
        cursor.execute(sql)
        rec = cursor.fetchall()

        print("select row")
        row = int(input())

        row_list = eval(rec[row-1][1])
        ticket_cost = 10
        row_len = len(rec)
        y = eval(rec[1][1])
        col_len = len(y)
        seat_count = row_len*col_len

        if seat_count > 60 and row <= (len(rec)/2):
            ticket_cost = 8

        while True:
            if 0 not in row_list:
                print("No Empty Seats")
                row = int(input())

            elif 0 in row_list:
                print("select seat number")
                s=''
                for i in row_list:
                    if i == 1:
                        s += ' B'
                    elif i == 0:
                        s += ' S'

                print(s)
                break

        col = int(input())
        while True:
            if row_list[col - 1] == 1:
                print("This seat is not Empty")
                col = int(input())
            elif row_list[col-1] == 0:
                new = row_list
                new[col-1] = 1
                break

        seat_number = chr(96+row)+str(col)
        sql_1 = "UPDATE seats SET vacant_seat = '{}' WHERE row_seat = {}".format(str(new), row)
        cursor.execute(sql_1)

        rec_query = "INSERT INTO cust_info(name, age, gender, phone_no, ticket_p, seat_num) values('{}',{},'{}',{},{},'{}')".format(c_name,c_age,c_gender,c_phone,ticket_cost,seat_number)
        cursor.execute(rec_query)
        con.commit()
        print("Booking Confirmed, your ticket price is ", ticket_cost, " and your seat number is ",seat_number)



        




