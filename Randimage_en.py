from PIL import Image;
import random;
import os;
import colorama;
from tkinter.filedialog import asksaveasfilename;
from tkinter import Tk;
from colorama import Fore, Style;
import ctypes;
colorama.init();
ctypes.windll.kernel32.SetConsoleTitleW('Randimage');

Tk().withdraw();
colorama.init();
colorlist = [0,255];

while True:
    os.system('cls');
    print(Fore.YELLOW + 'Welcome to Randimage!' + Style.RESET_ALL);
    print('Enter "0" to generate a new image');
    print('Enter "1" to generate a new image using only shades of grey');
    print('Enter "2" to generate a new image using only black and white colors');
    print('Enter "3" to generate a new horizontal lines image');
    print('Enter "4" to generate a new vertical lines image');
    print('Enter "5" to exit');
    user_input = input();

    if user_input == '0' or '1' or '2' or '3' or '4':
        os.system('cls');
        while True:
            try:
                print('Enter a path to a folder where file will be saved: ');
                p = asksaveasfilename(title='Save file',defaultextension='.png');

                a = int(input('Enter width: '));
                b = int(input('Enter height: '));
                
                img = Image.new('RGB', (a, b), 'white');

                if user_input == '0':
                    for i1 in range(a):
                        for i2 in range(b):
                            h1 = random.randrange(0,255);
                            h2 = random.randrange(0,255);
                            h3 = random.randrange(0,255);
                            img.putpixel((i1,i2), (h1,h2,h3));
                
                if user_input == '1':
                    for i1 in range(a):
                        for i2 in range(b):
                            h1 = random.randrange(0,255);
                            img.putpixel((i1,i2), (h1,h1,h1));
                
                if user_input == '2':
                    for i1 in range(a):
                        for i2 in range(b):
                            h1 = random.choice(colorlist);
                            img.putpixel((i1,i2), (h1,h1,h1));
                
                if user_input == '3':
                    for i2 in range(a):
                        h1 = random.randrange(0,255);
                        h2 = random.randrange(0,255);
                        h3 = random.randrange(0,255);
                        for i1 in range(b):
                            img.putpixel((i1,i2), (h1,h2,h3));

                if user_input == '4':
                    for i1 in range(a):
                        h1 = random.randrange(0,255);
                        h2 = random.randrange(0,255);
                        h3 = random.randrange(0,255);
                        for i2 in range(b):
                            img.putpixel((i1,i2), (h1,h2,h3));

                img.save(p);
                print(Fore.YELLOW + 'Done! Click "Enter" to continue.');
                img.show();
                input();
                break;

            except Exception as e:
                print(e);
                print(Fore.RED + 'An error was occurred: a non-digit string was input.\nTry again.');
                input();
                break;

    if user_input == '5':
        break;
    
    else:
        os.system('cls');