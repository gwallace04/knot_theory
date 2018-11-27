# A Program to check which knots are tricolorable
# Author: Gabriel Wallace <wallace004@live.missouristate.edu>

def main():
    f = open("knot_det.txt", "r")
    contents = f.read().split(',')
    f.close()
    contents = list(map(int, contents))
    tri_list = list(i for i, x in enumerate(contents) if x % 3 == 0)
    for n, i in enumerate(tri_list):
        if i <= 1:
            tri_list[n] = "3_{}".format(str(1))
        elif i <= 7:
            tri_list[n] = "6_{}".format(str(i - 4))
        elif i <= 14:
            tri_list[n] = "7_{}".format(str(i - 7))
        elif i <= 35:
            tri_list[n] = "8_{}".format(str(i - 14))
        elif i <= 84:
            tri_list[n] = "9_{}".format(str(i - 35))
        elif i <= 249:
            tri_list[n] = "10_{}".format(str(i - 84))
        elif i <= 616:
            tri_list[n] = "11a_{}".format(str(i - 249))
        elif i <= 801:
            tri_list[n] = "11n_{}".format(str(i - 616))

    ratio = len(tri_list)/len(contents)
    percent = int(ratio * 100)
    out_file = open("tricolorable_knots.txt", "w")
    intro = "There are a total of {} ".format(len(contents))
    intro += "knots with 11 or fewer crossings.\n"
    intro += "{} are tricolorable, or about {}%\n\n".format(len(tri_list), percent)
    out_file.write(intro)
    for x in tri_list:
        out_file.write(x)
        out_file.write(" ")
    out_file.close()

if __name__ == '__main__':
    main()

