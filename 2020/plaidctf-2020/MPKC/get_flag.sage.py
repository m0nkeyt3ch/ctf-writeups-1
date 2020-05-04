
# This file was *autogenerated* from the file get_flag.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_256 = Integer(256); _sage_const_10 = Integer(10); _sage_const_59 = Integer(59); _sage_const_25 = Integer(25)
q,n,a,s = (_sage_const_3 ,_sage_const_59 ,_sage_const_10 ,_sage_const_25 )

def combine_blocks(blocks):
    x = _sage_const_0 
    for i in blocks[::-_sage_const_1 ]:
        for j in i[::-_sage_const_1 ]:
            x = x*q+Integer(j)
    ss = ""
    while x > _sage_const_0 :
        ss = chr(x % _sage_const_256 ) + ss
        x = x//_sage_const_256 
    return ss


blocks = [
  [_sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_2 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_2 , _sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_2 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_1 , _sage_const_2 , _sage_const_1 , _sage_const_2 , _sage_const_2 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_2 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_2 , _sage_const_1 , _sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_0 ],
  [_sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_2 , _sage_const_1 , _sage_const_1 , _sage_const_2 , _sage_const_1 , _sage_const_2 , _sage_const_2 , _sage_const_1 , _sage_const_2 , _sage_const_2 , _sage_const_2 , _sage_const_2 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_2 , _sage_const_1 , _sage_const_1 , _sage_const_2 , _sage_const_2 , _sage_const_1 , _sage_const_2 , _sage_const_1 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_2 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_2 , _sage_const_2 , _sage_const_0 ],
  [_sage_const_1 , _sage_const_2 , _sage_const_0 , _sage_const_2 , _sage_const_2 , _sage_const_2 , _sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_2 , _sage_const_1 , _sage_const_2 , _sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_2 , _sage_const_2 , _sage_const_1 , _sage_const_2 , _sage_const_1 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_2 , _sage_const_1 , _sage_const_2 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_2 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_2 , _sage_const_1 , _sage_const_2 , _sage_const_0 , _sage_const_2 , _sage_const_2 , _sage_const_1 , _sage_const_0 ],
  [_sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_2 , _sage_const_2 , _sage_const_2 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_2 , _sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_2 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_2 , _sage_const_2 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_0 ],
  [_sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_2 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_2 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_2 , _sage_const_0 , _sage_const_2 , _sage_const_2 , _sage_const_0 , _sage_const_2 , _sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_1 ],
  [_sage_const_1 , _sage_const_2 , _sage_const_2 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_2 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_2 , _sage_const_1 , _sage_const_2 , _sage_const_2 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_2 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 ],
]

print combine_blocks(blocks)

