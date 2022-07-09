import tkinter

main_window = tkinter.Tk()

label1 = tkinter.Label(main_window, text = "Apakah Jupri Kembur ? ")
tombol1 = tkinter.Button(main_window, text = "Ya")
tombol2 = tkinter.Button(main_window, text = "Tidak = Ya")

label2 = tkinter.Label(main_window, text = "Apakah Deadine Terlalu Cepat ? ")
tombol3 = tkinter.Button(main_window, text = "Ya")
tombol4 = tkinter.Button(main_window, text = "Tidak = Ya")


# method positioning
label1.pack()
tombol1.pack()
tombol2.pack()
label2.pack()
tombol3.pack()
tombol4.pack()


# method menampilkan GUI
main_window.mainloop() 

