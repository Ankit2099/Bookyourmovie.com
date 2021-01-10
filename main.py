import os,sys
from movie import SellTicket, TicketBooking

def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))       
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return userInput 
            break

while True:
    print('||==============Book My Show===================||')
    print('||     1. SetUp the seat                       ||')
    print('||     2. Go to Menu                           ||')
    print('||=============================================||')

    choice = inputNumber("Enter the choice: ")

    if choice == 1:
        SellTicket.createSeat()

    if choice == 2:
        while True:
            print('||==============Book My Show===================||')
            print('||     1. Show the tickets                     ||')
            print('||     2. Buy a ticket                         ||')
            print('||     3. Statistics                           ||')
            print('||     4. Show all tickets                     ||')
            print('||     5. Show my tickets                      ||')
            print('||     0. Exit                                 ||')
            print('||=============================================||')

            inp = int(input())
            if inp == 1:
                SellTicket.showseats()

            if inp == 2:
                TicketBooking.bookTicket()

            if inp == 3:
                SellTicket.statistics()

            if inp == 4:
                SellTicket.user_info()

            if inp == 5:
                print("Enter phone number used during booking of ticket: ")
                phone_num = int(input())
                SellTicket.user_specific_info(phone_num)

            if inp == 0:
                sys.exit()

                
