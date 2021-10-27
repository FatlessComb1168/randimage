'''
Randimage RU.
Copyright (C) 2021 Fedor Egorov <fedoregorov1@yandex.ru>
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
from PIL import Image;
from random import randint, choice;
from os import system;
from tkinter.filedialog import asksaveasfilename;
from tkinter import Tk;
from colorama import Fore, Style, init;
import ctypes;

init();
ctypes.windll.kernel32.SetConsoleTitleW('Randimage');
Tk().withdraw();
colorlist = [0,255];

def random_color():
    global h1, h2, h3, h4, h5, h6;
    h1 = randint(0,255);
    h2 = randint(0,255);
    h3 = randint(0,255);
    h4 = randint(0,255);
    h5 = randint(0,255);
    h6 = randint(0,255);

def error():
    print(e);
    print(Fore.RED + 'An error was occurred:',
    'a non-digit string was input.\nTry again.');
    input();

_exit = True;
while _exit:
    try:
        system('cls');
        print(Fore.YELLOW + 'Welcome to Randimage!' + Style.RESET_ALL);
        user_input = int(input('Enter a number from 1 to 11 to' +
            'generate an image, or 12 to exit: '));

        if user_input in [i for i in range(1, 12)]:
            system('cls');
            try:
                print('Enter a path to a folder where file will be saved: ');
                p = asksaveasfilename(title='Save file',
                    defaultextension='.png');

                a = int(input('Enter width: '));
                b = int(input('Enter height: '));
                
                img = Image.new('RGB', (a, b), 'white');

                if user_input == 0:
                    for i1 in range(a):
                        for i2 in range(b):
                            random_color();
                            img.putpixel((i1,i2), (h1,h2,h3));
                
                if user_input == 1:
                    for i1 in range(a):
                        for i2 in range(b):
                            h1 = randint(0,255);
                            img.putpixel((i1,i2), (h1,h1,h1));
                
                if user_input == 2:
                    for i1 in range(a):
                        for i2 in range(b):
                            h1 = choice(colorlist);
                            img.putpixel((i1,i2), (h1,h1,h1));
                
                if user_input == 3:
                    for i2 in range(a):
                        random_color();
                        for i1 in range(b):
                            img.putpixel((i1,i2), (h1,h2,h3));

                if user_input == 4:
                    for i1 in range(a):
                        random_color();
                        for i2 in range(b):
                            img.putpixel((i1,i2), (h1,h2,h3));

                if user_input == 5:
                    for i1 in range(a):
                        random_color();
                        c = [(h1, h2, h3), (h4, h5, h6)];
                        for i2 in range(b):
                            img.putpixel((i1,i2), a[randint(0,1)]);

                if user_input == 6:
                    for i1 in range(a):
                        random_color();
                        c = [(h1, h2, h3), (h4, h5, h6)];
                        for i2 in range(b):
                            img.putpixel((i2,i1), c[randint(0,1)]);

                if user_input == 7:
                    for i1 in range(a):
                        random_color();
                        for i2 in range(b):
                            img.putpixel((i1,i2), (h1, h1, h1));

                if user_input == 8:
                    for i1 in range(a):
                        random_color();
                        c = [(h1, h2, h3), (h4, h5, h6)];
                        for i2 in range(b):
                            img.putpixel((i2,i1), (h1, h1, h1));

                if user_input == 9:
                    random_color();
                    for i1 in range(a):
                        for i2 in range(b):
                            c = [(h1, h2, h3), (h4, h5, h6)];
                            img.putpixel((i1,i2), c[randint(0,1)]);

                if user_input == 10:
                    random_color();
                    for i1 in range(a):
                        for i2 in range(b):
                            c = [(h1, h2, h3), (0, 0, 0)];
                            img.putpixel((i1,i2), c[randint(0,1)]);

                if user_input == 11:
                    random_color();
                    for i1 in range(a):
                        for i2 in range(b):
                            c = [(h1, h2, h3), (255, 255, 255)];
                            img.putpixel((i1,i2), c[randint(0,1)]);


                img.save(p);
                print(Fore.YELLOW + 'Done! Click "Enter" to continue.');
                img.show();
                input();

            except Exception as e:
                error();

        if user_input == 12:
            _exit = False;
        
        else:
            system('cls');
    
    except Exception as e:
        error();