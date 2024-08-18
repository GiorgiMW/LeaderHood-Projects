def reverse_alternate(st):
    st = st.split()
    listn = []
    for i in st:
        if st.index(i) % 2 == 1:
            listn.append(st[st.index(i)][::-1])
        else:
            listn.append(st[st.index(i)])
    return " ".join(listn)