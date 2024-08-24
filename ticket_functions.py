"""CSC108: Fall 2023 -- Assignment 1: Airline Tickets

This code is provided solely for the personal and private use of students taking
CSC108 at the University of Toronto. Copying for purposes other than this use is
expressly prohibited. All forms of distribution of this code, whether as given 
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2023 Sadia Sharmin, Jacqueline Smith, and Sophia Huynh.
"""

# Constants
YEAR = 0
MONTH = 4
DAY = 6
FROM = 8
TO = 11
SEAT = 14
FLYER = 17

WINDOW = 'window'
AISLE = 'aisle'
MIDDLE = 'middle'



def get_flyer_info(ticket: str) -> str:
    """Return the flyer number of the flyer for this ticket, if present. 
    Otherwise, return the empty string.
    
    >>> get_flyer_info('20230915YYZYEG12F')
    ''
    >>> get_flyer_info('20230915YYZYEG12F1236')
    '1236'
    """
    if len(ticket) > 16:
        return ticket[16:]
    else:
        return ''


def visits_airport(ticket: str, airport: str) -> bool:
    """Return True if and only if the given airport is either
    the From or To airport on this ticket, else False.
    
    >>> visits_airport('20230915YYZYEG12F', 'YYZ')
    True
    >>> visits_airport('20230915YYZYEG12F1236','NLD')
    False
    """
    if ticket[8:11] == airport:
        return True
    elif ticket[11:14] == airport:
        return True
    else:
        return False


def get_seat_type(ticket: str) -> str:
    """Return the seat type of the seat for this ticket.
    if the seat type is invalid return the empty string

    >>> get_seat_type('20230915YYZYEG12F')
    'window'
    >>> get_seat_type('20230915YYZYEG12C')
    'aisle'
    >>> get_seat_type('20230915YYZYEG12B')
    'middle'
    >>> get_seat_type('20230915YYZYEG12U')
    ''
    """
    
    seat_letter = ticket[16]

    if seat_letter == 'A' or seat_letter == 'F':
        return 'window'
    elif seat_letter == 'B' or seat_letter == 'E':
        return 'middle'
    elif seat_letter == 'C' or seat_letter == 'D':
        return 'aisle'
    else:
        return ''


def is_valid_seat(ticket: str) -> bool:
    """Return True if and only if the row of the seat
    on the ticket and the seat letter on the ticket is valid.
    Otherwise return False.

    >>> is_valid_seat('20230915YYZYEG12F1236')
    True
    >>> is_valid_seat('20230915YYZYEG32F1236')
    False
    >>> is_valid_seat('20230915YYZYEG12U1236')
    False
    """
    if 0 < int(ticket[14:16]) < 31 \
       and ticket[16] in ('A', 'B', 'C', 'D', 'E', 'F'):
        return True
    else:
        return False    


def is_valid_flyer(ticket: str) -> bool:
    """Return True if and only if the flyer number on the flyer of
    the ticket is valid. Otherwise return False.
    >>> is_valid_flyer('20231221YYZYEG25F4442')
    True
    >>> is_valid_flyer('20231221YYZYEG25F4441')
    False
    >>> is_valid_flyer('20231221YYZYEG25F432')
    False
    >>> is_valid_flyer('20231221YYZYEG25F')
    True
    """

    if len(ticket) == 20:
        flyer_number = ticket[17:20]
        if flyer_number.isdigit() and int(flyer_number) % 10 == int(ticket[20]):
            return True
    elif len(ticket) == 17:
        return True

    return False


def is_valid_ticket(ticket: str) -> bool:
    """Return True if and only if the ticket has a valid seat, a valid flyer
    number, and has different From and To airports.
    >>> is_valid_ticket('20231221YYZYEG25F4442')
    True
    >>> is_valid_ticket('20231221YYZYEG25U4442')
    False
    >>> is_valid_ticket('20231221YYZYYZ25F4442')
    False
    """
   
    if is_valid_flyer(ticket) and is_valid_seat(ticket):
        if ticket[0:7].isdigit() \
           and ticket[8:13].isalpha() and ticket[16].isalpha():
            if 0 < int(ticket[14:16]) < 31:
                if ticket[8:10] != ticket[11:13]:
                    return True
    else:
        return False


def days_until(ticket: str, date: str) -> int:
    """Return the number of days from the second date until the ticket date.
    
     >>> days_until('20230908YULYYZ07C2349', '20230901')
     7
    
    >>> days_until('20230901YULYYZ07C2349', '20230908')
    -7
    """
    flight_month = int(ticket[4:6])
    flight_day = int(ticket[6:8])

    year = int(date[0:4])
    month = int(date[4:6])
    day = int(date[6:8])
    this_year = 2023  

    if month > flight_month:
        if this_year - year > 1:
            count = 365 * (this_year - year - 1) + \
                30 * (12 - (month - flight_month))
        else:
            count = 30 * (12 - (month - flight_month))
        if flight_day - day >= 0:
            num_days = count + (flight_day - day)
        else:
            num_days = count - (day - flight_day)
    else:
        count = 30 * (flight_month - month) + 365 * (this_year - year)
        if flight_day - day >= 0:
            num_days = count + (flight_day - day)
        else:
            num_days = count - (day - flight_day)

    return num_days
