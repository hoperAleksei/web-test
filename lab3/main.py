from time import sleep

from jinja2 import Template, Environment, FileSystemLoader
import webbrowser
import matplotlib.pyplot as plt


def create_pict(x, y, name="pict.jpg"):
    plt.cla()
    line = plt.plot(x, y)
    plt.setp(line, color="blue", linewidth=2)
    plt.gca().spines["left"].set_position("zero")
    plt.gca().spines["bottom"].set_position("zero")
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)

    plt.savefig("tmp/{}".format(name))

    return "tmp/{}".format(name)


def f(x, n_var=0):
    if n_var == 0:
        return x ** 3 - 6 * x ** 2 + x + 5
    elif n_var == 1:
        return x ** 2 - 5 * x + 1
    elif n_var == 2:
        return 1 / (x ** 2 + 1)


def task1():
    a = -2
    b = 6
    n = 30

    h = (b - a) / n

    x_list = [a + i * h for i in range(n + 1)]
    f1_list = [f(x) for x in x_list]

    with open('templates/function_template.jinja2', 'r', encoding='utf-8-sig') as f_template:
        html = f_template.read()

    template = Template(html)
    template.globals["len"] = len(x_list)

    with open('function.html', 'w', encoding='utf-8-sig') as f_html:
        f_html.write(
            template.render(x=list(map(lambda x: round(x, 3), x_list)),
                            y=list(map(lambda x: round(x, 3), f1_list)),
                            pict=create_pict(x_list, f1_list)))
    webbrowser.open('function.html')


def task2():
    n_var = 1
    list_name_f = ["f(x)", "y(x)", "z(x)"]
    a = -2
    b = 6
    n = 30

    h = (b - a) / n

    x_list = [a + i * h for i in range(n + 1)]
    f1_list = [f(x, n_var) for x in x_list]

    with open('templates/function_template2.jinja2', 'r', encoding='utf-8-sig') as f_template:
        html = f_template.read()

    template = Template(html)
    template.globals["len"] = len(x_list)

    with open('function1.html', 'w', encoding='utf-8-sig') as f_html:
        f_html.write(
            template.render(
                count_f=3,
                a=a,
                b=b,
                n=n,
                n_var=n_var,
                list_f=list_name_f,
                x=list(map(lambda x: round(x, 3), x_list)),
                y=list(map(lambda x: round(x, 3), f1_list)),
                pict=create_pict(x_list, f1_list, name="pict1.jpg")))
    webbrowser.open('function1.html')


if __name__ == '__main__':
    task1()
    task2()
