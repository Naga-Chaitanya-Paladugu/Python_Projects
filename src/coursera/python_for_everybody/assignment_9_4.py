# 9.4 Write a program to read through the mbox-short.txt
# and figure out who has sent the greatest
# number of mail messages. The program looks
# for 'From ' lines and takes the second word of those
# lines as the person who sent the mail. The program creates
# a Python dictionary that maps the sender's mail address to a
# count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the
# dictionary using a maximum loop to find the most prolific committer.

if __name__== '__main__':
    fname= input("Enter file name: ")
    fhand = open(fname)
    counts = dict()
    for line in fhand:
        # if line.startswith('From '):
        #     print(line)
        if not line.startswith('From '):
            continue
        line_lst= line.split()
        mail_lst= line_lst[1].split('@')
        sender_name= mail_lst[0]
        counts[sender_name]= counts.get(sender_name,0) + 1
    names_lst= list(counts.keys())
    counts_lst= list(counts.values())
    counts_max= sorted(counts_lst, reverse=True)[0]
    for name, count in counts.items():
        if count == counts_max:
            print(f'{name} is the prolific sender with a total of {count} mails')
