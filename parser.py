import sys

name = sys.argv[1]
file_type = (name.split ("-"))[0]

raw_file = open ("./"+name, "r")
lines = raw_file.readlines ()

write_file = open ("./"+name+".parsed", "w")

time = 0

if file_type == "mpstat":
    write_file.write ("time[s]\tutil[%]\n")
    for line in lines:
        parsedline = line.split ()
        if not len (parsedline):
                continue
        if parsedline[2] =="all":
            data = "%d\t%s" % (time, parsedline[3])
            print (data)
            write_file.write (data + "\n")
            time = time + 1

elif file_type == "nicstat":
    write_file.write ("time[s]\trKB/s\twKB/s\n")
    for line in lines:
        parsedline = line.split ()
        if not len (parsedline):
            continue
        if parsedline[1] =="eno1":
            data = "%d\t%s\t%s" % (time, parsedline[2], parsedline[3])
            print (data)
            write_file.write (data + "\n")
            time = time + 1

elif file_type == "iostat":
    write_file.write ("time[s]\trKB/s\twKB/s\n")
    for line in lines:
        parsedline = line.split ()
        if not len (parsedline):
            continue
        if parsedline[0] == "sda":
            data = "%d\t%s\t%s" % (time, parsedline[2], parsedline[3])
            print (data)
            write_file.write (data + "\n")
            time = time + 1
            
else:
    print ("not supported file_type.")

raw_file.close ()
write_file.close ()