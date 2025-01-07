# 9.4 Write a program to read through the mbox-short.txt
# and figure out who has sent the greatest
# number of mail messages. The program looks
# for 'From ' lines and takes the second word of those
# lines as the person who sent the mail. The program creates
# a Python dictionary that maps the sender's mail address to a
# count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the
# dictionary using a maximum loop to find the most prolific committer.

if __name__ == '__main__':
    fname = input("Enter file name: ")
    fhand = open(fname)
    counts = dict()
    for line in fhand:
        # if line.startswith('From '):
        #     print(line)
        if not line.startswith('From '):
            continue
        line_lst = line.split()
        mail_lst = line_lst[1].split('@')
        sender_name = mail_lst[0]
        counts[sender_name] = counts.get(sender_name, 0) + 1
    names_lst = list(counts.keys())
    counts_lst = list(counts.values())
    counts_max = max(counts_lst)
    print(counts_max)
    print(counts)
    max_names = [key for key, value in counts.items() if value == counts_max]
    print(max_names)
    print(f'{", ".join(max_names)} is/are the prolific sender/s with a total of {counts_max} mails')
    # counts_max= sorted(counts_lst, reverse=True)[0]
    # print(counts_max)
    # for name, count in counts.items():
    #     if count == counts_max:
    #         print(f'{name} is the prolific sender with a total of {count} mails')
