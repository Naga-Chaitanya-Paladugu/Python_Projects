# 10.2 Write a program to read through the mbox-short.txt and
# figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then
# splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 "09":14:16 2008
# Once you have accumulated the counts for each hour, print out the counts,
# sorted by hour as shown below.

if __name__=='__main__':
    fname= input("Enter file name: ")
    fh = open(fname)
    hourly_count = dict()
    for line in fh:
        if not line.startswith('From '):
            continue
        # print(line)
        line_lst= line.split()
        hour= line_lst[5].split(':')[0]
        # print(hour)
        hourly_count[hour]= hourly_count.get(hour, 0)+ 1
