from collections import deque
stack=deque()
st=deque()
n=int(input())
for i in range(n) :
    x=input()
    if "1" in x :
        stack.append(x[2:])
    if x=="2" :
        st.append(stack.popleft())        
for j in st :
    print(j, end=" ")