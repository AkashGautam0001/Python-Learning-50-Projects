from datetime import datetime

with open("daily_journal.txt", "a", encoding="utf-8") as file :
    logger = input("Enter your daily learning journal : ").strip()
    now = datetime.now()
    todayDate = now.strftime("%Y-%m-%d - %I:%M %p")
    rating = int(input("Enter Productivity Rating from 5 : "))
    log = f"""
    Today : 🗓️ {todayDate}
    {logger}
    Productivity Rating : {rating}/5
    """
    file.write(log)
    file.close()
