def my_function(x) :
    t=""
    for i in range(0,len(x),3) :
        if x[i:(i+3)]=="ONE":
            t=t+"1"
        if x[i:(i+3)]=="TWO":
            t=t+"2"
        if x[i:(i+3)]=="THR":
            t=t+"3"
        if x[i:(i+3)]=="FOU":
            t=t+"4"
        if x[i:(i+3)]=="FIV":
            t=t+"5"
        if x[i:(i+3)]=="SIX":
            t=t+"6"
        if x[i:(i+3)]=="SEV":
            t=t+"7"
        if x[i:(i+3)]=="EIG":
            t=t+"8"
        if x[i:(i+3)]=="NIN":
            t=t+"9"
        if x[i:(i+3)]=="ZER":
            t=t+"0"
    return t
def op(r) :
    u=""
    for i in range(len(r)) :
        if r[i]=="1" :
            u=u+"ONE"
        if r[i]=="2" :
            u=u+"TWO"
        if r[i]=="3" :
            u=u+"THR"
        if r[i]=="4" :
            u=u+"FOU"
        if r[i]=="5" :
            u=u+"FIV"
        if r[i]=="6" :
            u=u+"SIX"
        if r[i]=="7" :
            u=u+"SEV"
        if r[i]=="8" :
            u=u+"EIG"
        if r[i]=="9" :
            u=u+"NIN"
        if r[i]=="0" :
            u=u+"ZER"
    print(u)
s=input()
for i in range(len(s)) :
    if s[i]=="+" :
        x=s[(i+1):]
        y=s[:i]
q=int(my_function(x))
w=int(my_function(y))
r=str(q+w)
op(r)
