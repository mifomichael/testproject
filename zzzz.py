import tkinter as tk
import tkinter.ttk as ttk


root = tk.Tk()
style = ttk.Style(root)

#    try also the 'clam' theme
style.theme_use('alt')

common_bg = '#1d2e33'  # RGB in dec
#    alternatively use the "more red" version of the common_bg as the indicatorcolor
#    sel_bg = '#' + ''.join([hex(x)[2:].zfill(2) for x in (221, 26, 18)])
common_fg = 'yellow'  # pure white

rad_button = ttk.Radiobutton(root, text='abc', value=0)
rad_button.pack(expand=True, fill='both')
rad_button2 = ttk.Radiobutton(root, text='abc',value=1)
rad_button2.pack(expand=True, fill='both')

style_name = rad_button.winfo_class()
style.configure(style_name, foreground=common_fg, background=common_bg, indicatorcolor=common_bg)

style.map(style_name,
          foreground = [('disabled', common_fg),
                      ('pressed', common_fg),
                      ('active', common_fg)],
          background = [('disabled', common_bg),
                      ('pressed', '!focus', common_bg),
                      ('active', common_bg)],
          indicatorcolor=[('selected', common_bg),
                          ('pressed', common_bg)]

          )
root.mainloop()