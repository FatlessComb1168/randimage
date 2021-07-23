from PIL import Image;
import random;
import time;
import os;
import colorama;
from colorama import Fore, Back, Style;
import ctypes;
colorama.init();
ctypes.windll.kernel32.SetConsoleTitleW('Randimage');

while True:
    os.system('cls');
    print(Fore.YELLOW + 'Welcome to Randimage!' + Style.RESET_ALL);
    print('Enter "0" to generate a new image');
    print('Enter "1" to exit');
    a = input();

    if a == '0':
        os.system('cls');
        while True:
            try:
                p = input('Enter a path to a folder where file will be saved: ');

                if os.path.isdir(p):
                    p = p + '\\';
                else:
                    print(Fore.RED + 'Incorrect path. Try again.');
                    time.sleep(1.5);
                    break;

                n = input('Enter the name of file: ');
                c = p + n + '.png';

                a = int(input('Enter width: '));
                b = int(input('Enter length: '));

                img = Image.new('RGB', (a, b), 'white');

                for i1 in range(a):
                    for i2 in range(b):
                        h1 = random.randrange(0,255);
                        h2 = random.randrange(0,255);
                        h3 = random.randrange(0,255);
                        img.putpixel((i1,i2), (h1,h2,h3));

                img.save(c);
                time.sleep(1.5);

                print(Fore.YELLOW + 'Done! Click "Enter" to continue.');
                img.show();
                input();
                break;
            except:
                print(Fore.RED + 'An error was occurred: a non-digit string was input.\nTry again.');
                time.sleep(1.5);
                break;

    if a == '1':
        break;
    
    else:
        os.system('cls');