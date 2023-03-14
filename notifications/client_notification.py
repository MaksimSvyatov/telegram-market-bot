import schedule

def greeting():
    print('This is notification')

def get_notification():
    schedule.every().day.at('16:30').do(greeting)
    
    while True:
        schedule.run_pending()