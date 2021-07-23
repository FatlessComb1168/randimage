from PIL import Image;
import random;
import time;
import os;
import colorama;
from colorama import Fore, Back, Style;
import ctypes;
colorama.init();
ctypes.windll.kernel32.SetConsoleTitleW('Randimage');

colorama.init();

while True:
    os.system('cls');
    print(Fore.YELLOW + 'Добро пожаловать в Randimage!' + Style.RESET_ALL);
    print('Введите 0, чтобы сгенерировать изображение');
    print('Введите 1, чтобы выйти');
    a = input();

    if a == '0':
        os.system('cls');
        while True:
            try:
                p = input('Введите путь к папке, где будет сохранён файл: ');

                if os.path.isdir(p):
                    p = p + '\\';
                else:
                    print(Fore.RED + 'Неверный путь файла. Попробуйте ещё раз.');
                    time.sleep(1.5);
                    break;

                n = input('Введите название файла: ');
                c = p + n + '.png';

                a = int(input('Введите ширину: '));
                b = int(input('Введите длину: '));

                img = Image.new('RGB', (a, b), 'white');

                for i1 in range(a):
                    for i2 in range(b):
                        h1 = random.randrange(0,255);
                        h2 = random.randrange(0,255);
                        h3 = random.randrange(0,255);
                        img.putpixel((i1,i2), (h1,h2,h3));

                img.save(c);
                time.sleep(1.5);

                print(Fore.YELLOW + 'Готово! Нажмите Enter, чтобы вернуться в главное меню.');
                img.show();
                input();
                break;
            except:
                print(Fore.RED + 'Произошла ошибка: было введено нечисловое значение.\nПопробуйте ещё раз.');
                time.sleep(1.5);
                break;

    if a == '1':
        break;
    
    else:
        os.system('cls');