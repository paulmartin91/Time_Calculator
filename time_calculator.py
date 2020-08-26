def add_time(start, duration, day=False):

    days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
 
#account for case in day
    if day is not False: day = day.capitalize()

#Seperate everything out
    start_hours = start.split(":")[0]
    start_minutes = start.split(":")[1].split(" ")[0]
    start_am_or_pm = start.split(":")[1].split(" ")[1]
    duration_hours = duration.split(":")[0]
    duration_minutes = duration.split(":")[1]

#Add hours to give new hours total
    new_time_hours = int(duration_hours) + int(start_hours)

#Convert start to military time
    if start_am_or_pm == "PM": new_time_hours = new_time_hours + 12

#Add minutes to give new minutes total
    new_time_minutes = int(start_minutes) + int(duration_minutes)

#Check if minutes total more than an hour, if so add 1 hour and keep the remainder as minutes
    if new_time_minutes >= 60:
       new_time_hours = new_time_hours + 1
       new_time_minutes = new_time_minutes - 60

#Divide start hours by 24 to give number of extra days
    extra_days = int(new_time_hours / 24)

#remaineder of days / 24 gives correct hours
    new_time_hours = new_time_hours % 24

    print("new_time_hours =", new_time_hours)
    print("start_am_or_pm", start_am_or_pm)

#Account for 12:00 PM not changing to 00:00 PM
    if (new_time_hours == 12 and start_am_or_pm == "AM"): new_am_or_pm = "PM"
    else:
    #start hours + Duration hours % 24 will give correct hours for returned time
        if (new_time_hours >= 12): 
            new_time_hours = new_time_hours - 12
            new_am_or_pm = "PM"
        else: new_am_or_pm = "AM"

#Add extra days to day
    if (day in days_of_the_week):
        new_day = days_of_the_week[(days_of_the_week.index(day) + extra_days) % 7]
    if extra_days == 1: days_later = " (next day)"
    if extra_days > 1: days_later = " ("+str(extra_days) + " days later)"
    
#add extra 0 to minutes if needed
    new_time_minutes = str(new_time_minutes)
    if len(new_time_minutes) == 1: new_time_minutes = "0"+new_time_minutes

#Turn 12:00 AM to 00:00 AM
    if new_time_hours == 0 and new_am_or_pm == "AM": new_time_hours = "12"

#Create new_time string
    new_time = str(new_time_hours) + ":" + new_time_minutes + " " + new_am_or_pm

#Add day of the week if day peramiter passed
    if day is not False:
        new_time = new_time + ", " + new_day

#Add days later if needed
    if extra_days >= 1: new_time = new_time + days_later

    print(new_time)
    return new_time


add_time("11:40 AM", "0:25")