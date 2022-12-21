with open('input.txt', 'r') as inp, open('output.txt', 'w') as outp:
    nums = inp.read().splitlines()
    form = list(map(int, nums))
    print(form)
    C = form[0]//2
    H = form[1]//6
    O = form[2]//1
    if C < O and C<H:
        outp.write(str(C))
    if H < O and H<C:
        outp.write(str(H))
    if O < C and O<H:
        outp.write(str(O))
    if O==C and C==H and H==C:
        outp.write(str(O))
    outp.close()
    inp.close()