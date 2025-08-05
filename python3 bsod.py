import os
import time
def bsod():
    from ctypes import POINTER, byref, c_int, c_uint, c_ulong, windll
    nullptr = POINTER(c_int)()
    windll.ntdll.RtlAdjustPrivilege(
        c_uint(19),
        c_uint(1),
        c_uint(0),
        byref(c_int())
    )

    windll.ntdll.NtRaiseHardError(
        c_ulong(0xC000007B),
        c_ulong(0),
        nullptr,
        nullptr,
        c_uint(6),
        byref(c_uint())
    )
accept = int(input("Type 0 to generate BSOD. Ctrl+C to cancel"))
while True:
    if accept == 0:
        print("BSOD generated")
        time.sleep(0.1)
        bsod()
        break
