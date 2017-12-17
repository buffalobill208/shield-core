li = ["do", "re", "mi", "fa", "sol"]

i = 0
for i in range(len(li)):
    if i < len(li)-1:
       # until end is reached
       #print("this", li[i]
       print("this {}".format(i))
       print("next {}".format(i+1))
    else:
       # end
       #print "this", li[i]
       print("this {}".format(i))
