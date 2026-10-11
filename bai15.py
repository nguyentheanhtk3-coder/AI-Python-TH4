a = input()
b = input()
sv_nop_bai = set(a.split())
danh_sach_lop = set(b.split())
def bai_tap(x, y):
    sv_da_nop = []
    sv_chua_nop = []
    for i in y:
        if i in x:
            sv_da_nop.append(i)
        else:
            sv_chua_nop.append(i)
    yes = tuple(sv_da_nop)
    no = tuple(sv_chua_nop)
    print(yes)
    print(no)

bai_tap(sv_nop_bai, danh_sach_lop)