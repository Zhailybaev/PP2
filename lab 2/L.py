s=input()
st=[]
t=""
for i in range(len(s)) :
    if s[i]=="(" or s[i]=="[" or s[i]=="{" :
        st.append(s[i])
    elif s[i]==")" :
        if len(st)==0:
            t="No"
            break
        elif st[len(st)-1]=="(" :
            t="Yes"
            st.pop(len(st)-1)
        else :
            t="No"
    elif s[i]=="}" :
        if len(st)==0:
            t="No"
            break
        elif st[len(st)-1]=="{" :
            t="Yes"
            st.pop(len(st)-1)
        else :
            t="No"
    elif s[i]=="]" :
        if len(st)==0:
            t="No"
            break
        elif st[len(st)-1]=="[" :
            t="Yes"
            st.pop(len(st)-1)
        else :
            t="No"
if len(st)!=0 :
    print("No")
else :
    print(t)