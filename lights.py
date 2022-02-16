import os
import time

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

while True:
    print('''
Happy Holidays!

       ^
      < >
      / \\
     /   \\
    /     \\
    /     \\
   /       \\
  /         \\
  /         \\
 /           \\
/_____________\\
 __+_ | |  _+_
_|__|_|_|__|_|_\n''')
    time.sleep(1)
    clear()
    print('''
Happy Holidays!

       ^
      <*>
      / \\
     /  *\\
    /* *  \\
    / *   \\
   /   * * \\
  /  *    * \\
  /*  * *  *\\
 /*  *   *   \\
/_____________\\
 __+_ | |  _+_
_|__|_|_|__|_|_
    ''')
    time.sleep(1)
    clear()