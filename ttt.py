import colorama

def spisok():
    w=[]
    for i in range(1,10):
        w.append(str(i))
    return w
red=colorama.Fore.RED
green=colorama.Fore.GREEN
blue=colorama.Fore.BLUE
mag=colorama.Fore.MAGENTA
reset=colorama.Style.RESET_ALL
def draw_board(sp):
    print(f'{mag}-----|------|-----{reset}')
    for i in range(0,9,3):
        print(f'{mag}    | {reset}'.join(sp[i:i+3]))
        print(f'{mag}-----|------|-----{reset}')

def prov_ind(indx, spiso, player1):
    try:
        if str(indx) in spiso:
            spiso[indx-1]=player1
            return True
    except ValueError:
        print(f'{red}неверный индекс{reset}')
        return False


def chek_win(spis, player1):
    for i in range(0,9,3):
        if spis[i:i+3] == [player1]*3:
            return True
    for i in range(0,3):
        if spis[i]==spis[i+3]==spis[i+6]==player1:
            return True
    if spis[0]==spis[4]==spis[8]==player1:
        return True
    elif spis[2] == spis[4] == spis[6] == player1:
        return True


def nichya(sp3):
    for i in sp3:
        if i!="X" and i!='O':
            return False
    return True



def main():
    sp2=spisok()
    draw_board(sp2)
    players = ['X', 'O']
    play1 = players[0]
    while True:
        ind=int(input(f'{blue}введите число: {reset}'))
        if prov_ind(ind, sp2, play1)== True:
            draw_board(sp2)
            if chek_win(sp2, play1)==True:
                print(f'{green}{play1} победил!{reset}')
                break
            elif nichya(sp2)==True:
                print(f'{blue}Ничья!{reset}')
                break

            if play1==players[0]:
                play1=players[-1]
            else:
                play1=players[0]


main()
