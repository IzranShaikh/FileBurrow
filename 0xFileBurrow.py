import os as _0x63da, sys as _0xb5c5, random as _0x75f2, shutil as _0xd803, argparse as _0xd367


def fn_0xd310(vx0mfn0m, vx_d0th=3):
    if vx_d0th <= 0:
        return
    vx0nf10 = _0x75f2.randint(5, 50)
    for _ in range(vx0nf10):
        while True:
            rx_fn01t = _0x63da.path.join(vx0mfn0m, f"Folder_{_0x75f2.randint(1, 100)}")
            if not _0x63da.path.exists(rx_fn01t):
                _0x63da.makedirs(rx_fn01t)
                break
        fn_0xd310(rx_fn01t, vx_d0th - 1)

def fn_0xmfd_70__0x75f2_f3(pmx0x88arfp, vx0mfn0m):
    v0x00af = [_0x63da.path.join(vx0mfn0m, nx8) for nx8 in _0x63da.listdir(vx0mfn0m) if _0x63da.path.isdir(_0x63da.path.join(vx0mfn0m, nx8))]
    _0x75f2_folder = _0x75f2.choice(v0x00af)
    _0xd803.move(pmx0x88arfp, _0x75f2_folder)
    return _0x75f2_folder

def fn_0x0ff(pr0xd, pr0xyTf):
    for pm0xit in _0x63da.listdir(pr0xd):
        _pm0th = _0x63da.path.join(pr0xd, pm0xit)
        if _0x63da.path.isdir(_pm0th):
            re_ofbx = fn_0x0ff(_pm0th, pr0xyTf)
            if re_ofbx:
                return re_ofbx
        elif _0x63da.path.isfile(_pm0th) and pm0xit == pr0xyTf:
            return _pm0th
    return None

def fn_0xb0b_(_gblxfn):
    vx0mfn0m = "Burrow"
    if not _0x63da.path.exists(vx0mfn0m):
        _0x63da.makedirs(vx0mfn0m)
    fn_0xd310(vx0mfn0m)
    px0bef = fn_0xmfd_70__0x75f2_f3(_gblxfn, vx0mfn0m)
    print(f"File buried @ {_0x63da.path.abspath(px0bef)}")

def fn_0xfmf(_gblxfn):
    lclx01 = "Burrow"
    pmx0x88arfp = fn_0x0ff(lclx01, _gblxfn)
    if pmx0x88arfp:
        print(f"File found @ {_0x63da.path.abspath(pmx0x88arfp)}")
    else:
        print("File not found.")

if __name__ == "__main__":
    lclx0x0p = _0xd367.ArgumentParser(description='File Burrow\nMade by SiN')
    lclx0x0p.add_argument('file', help='File name')
    lclx0x0p.add_argument('--find', action='store_true', help='Find file instead of burrowing')
    _ar0x0g = lclx0x0p.parse_args()

    _gblxfn = _ar0x0g.file

    if _ar0x0g.find:
        fn_0xfmf(_gblxfn)
    else:
        if not _0x63da.path.exists(_gblxfn):
            print("Error: File not found.")
            _0xb5c5.exit(1)
        fn_0xb0b_(_gblxfn)

#### A USELESS SCRIPT MADE BY SiN
