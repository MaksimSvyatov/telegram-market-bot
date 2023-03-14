import schedule

def greeting ():
    print('This is notification')

def get_notification():
    schedule.every().day.at('16:00').do(greeting)
    
    while True:
        schedule.run_pending()