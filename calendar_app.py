import pandas as pd
from datetime import datetime, timedelta

# Pandas Settings

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None ) 


# Date Stuff

first_day = datetime.today()
last_day = first_day + timedelta(days=30)
dates = pd.date_range(first_day, last_day, freq='D').strftime('%d-%m-%Y').tolist()

try:
    df = pd.read_csv("takvim_uygulamasi.csv")
    df.to_csv("takvim_uygulamasi.csv", index=False)
except FileNotFoundError:
    df = pd.DataFrame(columns=dates)

# UI

def menu():
    global action
    menu = print("*" * 10 + "\n0-Show Calendar\n1-Add Event\n2-Remove Event\n3-Update Event\n4-Go To Date\n5-Quit\n" + "*" * 10)
    action = int(input("What do you want to do? "))

# Show Calendar

def show():
        print("Showing Calendar")

# Add
    
def add():
        print("You pressed add event. Press ^ to quit.")
        while 1>0:
            input_userdate = input("Write the date you wish to add. (DD-MM-YYYY) ")
            if input_userdate == "^":
                break
            try:
                input_date = datetime.strptime(input_userdate, '%d-%m-%Y').date()    
            except ValueError:
                print("Enter valid date.")
                continue
            input_userevent = input("Write event that you wish to add. ")
            if input_userdate in df.columns:
                event_row = df[df[input_userdate].notna()]
                if event_row.empty:
                    df.loc[0,f"{input_userdate}"] = input_userevent
                else:
                    last_row_index = event_row.index[-1] + 1
                    df.loc[last_row_index,f"{input_userdate}"] = input_userevent
            else:
                df[f"{input_userdate}"] = None
                df.loc[0,f"{input_userdate}"] = input_userevent
            df.to_csv("takvim_uygulamasi.csv", index=False)

# Remove

def remove():
        print("You pressed remove event. Press ^ to quit.")
        while 1>0:
            input_userdate_2 = input("Write the date you wish to remove. (DD-MM-YYYY) ")
            if input_userdate_2 == "^":
                break
            try:
                input_date_2 = datetime.strptime(input_userdate_2, '%d-%m-%Y').date()
            except ValueError:
                print("Enter valid date.")
                continue
            print(df[input_userdate_2].to_string(index=False))
            remove_event = input("Write the event that you wish to remove: ")
            df.loc[df[f'{input_userdate_2}'] == remove_event, f'{input_userdate_2}'] = ''
            df.to_csv("takvim_uygulamasi.csv", index=False)

# Update

def update():
        print("You pressed update event. Press ^ to quit.")
        while True:
            input_userdate = input("Write the date you wish to update. (DD-MM-YYYY) ")
            if input_userdate == "^":
                break
            try:
                input_date = datetime.strptime(input_userdate, '%d-%m-%Y').date()
            except ValueError:
                print("Enter valid date.")
                continue
            if input_userdate not in df:
                print("Can't find an event on this date.")
                continue
            print(df[input_userdate].to_string(index=False))
            input_userevent = input("Write the event that you wish to update. ")
            if input_userevent not in df[input_userdate].values:
                print("Can't find an event like that.")
                continue
            new_event = input("Write the new event:  ")
            df.loc[df[input_userdate] == input_userevent, input_userdate] = new_event
            df.to_csv("takvim_uygulamasi.csv", index=False)
        

# Go

def go():
    while 1>0:
        go_date = input("Write the date you wish to go. (DD-MM-YYYY) ")
        print("Going to, ", go_date, )  
        if go_date in df:
            df_date = df[[go_date]]
            if df_date.isnull().all().all():
                print("Couldn't find an event on this date..")
            else:
                print(df_date.dropna())
        else:
            print("Couldn't find an event on this date.")
        cont = input("Press ^ to continue.")
        if cont == "^":
            menu()

# Exit

def exit():
        quit("Quiting.")

# App

menu()
if action == 0:
    show()
    df = (pd.read_csv("takvim_uygulamasi.csv"))
    print(df)
if action == 1:
    add()
    df = (pd.read_csv("takvim_uygulamasi.csv"))
    print(df)
if action == 2:
    remove()
    df = (pd.read_csv("takvim_uygulamasi.csv"))
    print(df)
if action == 3:
    update()
    df = (pd.read_csv("takvim_uygulamasi.csv"))
    print(df)
if action == 4:
    go()
if action == 5:
    quit()
