def timekonverter(x): #WIth Inspiration of Concept INput in Sec
    if x // (365.2425*24*3600) < 1: # year
        if x//(24 * 3600)>1: #day
            days = x // (24 * 3600)
            hours = (x % (24 * 3600))/3600
            return [int(days),"days",int(hours),"hours"]
        else:
            if x // 3600 < 1:  # day
                sec=x % 60
                min= x // 60
                return[int(min),"min",int(sec),"seconds"]
            else:
                hours = x // 3600
                min = (x % 3600)/60
                return [int(hours), "hours", int(min), "min"]
    else:
        days= (x % (365.2425*24*3600))/(24*3600)
        years=x // (365.2425*24*3600)
        return [int(years),"years",int(days),"days"]
