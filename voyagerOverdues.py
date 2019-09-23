# This script extracts information about overdue, etc., items from ExLibris' Voyager integrated library system's crcnotes report. The best way to get this information is to use the Reporter module, but one of our libraries does not want notices sent without staff first checking the shelves. This gives them that information and then they can contact the patron manually.
# Note: When pulling the crcnotes file from the Voyager server, rename the copy left on the server (example: crcnotes.B-Circ.inp.old). If this isn't done, Voyager will keep appending information to it rather than creating a new file.

handle = open("crcnotes.B-Circ.inp") # use the name of the desired .inp file
fout = open("overdues.txt", "w")
nowname = "None"

for line in handle :
    words = line.split("|")
    newname = words[4] + ", " + words[6] + " " + words[5] + " - " + words[2]
    finetype = "Description: " + words[34]
    duedate = "Due date: " + words[33]
    finedate = "Fine date: " + words[33]
    noticenum = "Notice number: " + words[34]
    barcode = "Barcode: " + words[30]
    totalfee = "Total fee: $" + words[38]
    book = words[28]
    bookpart = book.split("/")
    title = bookpart[0]
    callno = "Call number: " +  words[31]
    info = "\n\t" + title + "\n\t\t" + barcode + "\t" + callno + "\n\t\t" + finetype + "\n\t\t" + duedate + "\n\t\t" + totalfee
    if newname != nowname :
        fout.write("\n")
        print("\n" + newname)
        print(info)
        fout.write(newname + "\n")
        fout.write(info + "\n")
        fout.write("\n")
    else :
        print(info)
        fout.write(info + "\n")
        fout.write("\n")
    nowname = newname
