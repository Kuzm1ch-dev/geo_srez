import numpy as np
import matplotlib.pyplot as plt
from mtz import rho
from gen import generator



def main():

    print("Введите размерность: ")
    s = int(input())
    print("Введите сопротивление полупространства слоев (формат 300,400,500): ")
    l = str(input()).split(",")
    print("Введите угол разлома : ")
    fi = int(input())
    print("Введите смещение разлома : ")
    offset = int(input())

    g = generator(s,l,fi,offset)
    g.generate_file()

    data_analysed = rho('Data.txt') #Обрабатываем входные данные в отдельном классе

    gs_kw = dict(width_ratios=[15,1])

    #Вывод
    #Визуализация данных
    fig1, (ax, cax) = plt.subplots(1, 2, figsize=(10, 5),  constrained_layout=True, gridspec_kw=gs_kw)

    ax.set_yscale("linear")
    ax.set_xticks(data_analysed.position_y)
    ax.set_yticks(data_analysed.position_z)
    ax.set_xticklabels(data_analysed.list_x)
    ax.set_yticklabels(data_analysed.list_y)
    ax.set_xlabel("Расстояние по горизонтали, км")
    ax.set_ylabel("Расстояние по вертикали, км")
    ax.set_xlim([0, data_analysed.position_y[-1]])
    ax.set_ylim([data_analysed.position_z[-1], 0])
    ax.grid()

    p = ax.imshow(data_analysed.rho, cmap='jet', aspect='auto', interpolation='bilinear', origin="upper")
    fig1.colorbar(p, cax=cax)
    cax.set_ylabel(r"Сопротивление, $\rho$ [$Ом \times м$]", rotation=90)
    fig1.canvas.manager.set_window_title("Визуализация данных")
    fig1.canvas.draw()

    #Визуализировать кривые rho кажущегося
    fig2, (ax, cax) = plt.subplots(1, 2, figsize=(10, 5),  constrained_layout=True, gridspec_kw=gs_kw)

    cax.clear()
    ax.plot([i+1 for i in range(len(data_analysed.row_solutions))], data_analysed.row_solutions)

    ax.set_yscale('log')
    ax.set_xticks([i+1 for i in range(len(data_analysed.row_solutions))])
    ax.set_xticklabels([i+1 for i in range(len(data_analysed.row_solutions))])
    ax.set_xlim([1, len(data_analysed.row_solutions)])
    ax.set_xlabel("Номер пикета")
    ax.set_ylabel(r"Кажущееся сопротивление, $lg(\rho_{T})$")

    legend_marks = [data_analysed.t1 * 2**(i+1) for i in range(len(data_analysed.row_solutions[0]))]
    ax.legend(legend_marks, title=r"Периоды, $T [с]$")

    fig2.canvas.manager.set_window_title("Визуализировать кривые rho кажущегося")
    fig2.canvas.draw()

    #Визуализировать карту rho кажущегося
    fig3, (ax, cax) = plt.subplots(1, 2, figsize=(10, 5),  constrained_layout=True, gridspec_kw=gs_kw)

    ax.set_xticks(data_analysed.position_y)
    ax.set_xticklabels(data_analysed.list_x)
    ax.set_xlim([0, data_analysed.position_y[-1]])
    ax.set_xlabel("Расстояние по горизонтали, км")

    periods = [data_analysed.t1 * 2**(i+1) for i in range(len(data_analysed.row_solutions[0]))]

    ax.set_yticks([i for i in range(len(periods))])
    ax.set_yticklabels(periods)
    ax.set_ylabel(r"Периоды, $T [с]$")

    temp_mas = np.log10(np.array(data_analysed.row_solutions).transpose())
    p2 = ax.imshow(temp_mas, cmap='jet', aspect='auto', interpolation='bilinear', origin="upper")
    fig3.colorbar(p2, cax=cax)
    cax.set_ylabel(r"Кажущееся сопротивление, $lg(\rho_{T})$", rotation=90)
    fig3.canvas.manager.set_window_title("Визуализировать карту rho кажущегося")
    fig3.canvas.draw()



    #Визуализировать кривые phi
    fig4, (ax, cax) = plt.subplots(1, 2, figsize=(10, 5),  constrained_layout=True, gridspec_kw=gs_kw)
    cax.clear()
    ax.plot([i+1 for i in range(len(data_analysed.phi_solutions))], data_analysed.phi_solutions)

    ax.set_xticks([i+1 for i in range(len(data_analysed.phi_solutions))])
    ax.set_xticklabels([i+1 for i in range(len(data_analysed.phi_solutions))])
    ax.set_xlim([1, len(data_analysed.phi_solutions)])
    ax.set_xlabel("Номер пикета")
    ax.set_ylabel(r"Фаза импеданса, $\phi$")

    legend_marks = [data_analysed.t1 * 2**(i+1) for i in range(len(data_analysed.phi_solutions[0]))]
    ax.legend(legend_marks, title=r"Периоды, $T [с]$")
    fig4.canvas.manager.set_window_title("Визуализировать кривые phi")
    fig4.canvas.draw()
    #Визуализировать карту phi

    fig5, (ax, cax) = plt.subplots(1, 2, figsize=(10, 5),  constrained_layout=True, gridspec_kw=gs_kw)

    ax.set_xticks(data_analysed.position_y)
    ax.set_xticklabels(data_analysed.list_x)
    ax.set_xlim([0, data_analysed.position_y[-1]])
    ax.set_xlabel("Расстояние по горизонтали, км")

    periods = [data_analysed.t1 * 2**(i+1) for i in range(len(data_analysed.phi_solutions[0]))]

    ax.set_yticks([i for i in range(len(periods))])
    ax.set_yticklabels(periods)
    ax.set_ylabel(r"Периоды, $T [с]$")

    temp_mas = np.array(data_analysed.phi_solutions).transpose()
    p2 = ax.imshow(temp_mas, cmap='jet', aspect='auto', interpolation='bilinear', origin="upper")
    fig5.colorbar(p2, cax=cax)
    cax.set_ylabel(r"Фаза импеданса, $\phi$", rotation=90)
    fig5.canvas.manager.set_window_title("Визуализировать карту phi")
    fig5.canvas.draw()

    plt.show()


if __name__ == "__main__":
    main()