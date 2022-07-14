import tkinter

main_window = tkinter.Tk()

label1 = tkinter.Label(main_window, text = "Apakah Anda Sudah Menikah ? ")
tombol1 = tkinter.Button(main_window, text = "Sudah")
tombol2 = tkinter.Button(main_window, text = "Belum")

label2 = tkinter.Label(main_window, text = "Ingin Melanjutkan Program ? ")
tombol3 = tkinter.Button(main_window, text = "Ya")
tombol4 = tkinter.Button(main_window, text = "Tidak")


# method positioning
label1.pack()
tombol1.pack()
tombol2.pack()
label2.pack()
tombol3.pack()
tombol4.pack()


# method menampilkan GUI
main_window.mainloop() 