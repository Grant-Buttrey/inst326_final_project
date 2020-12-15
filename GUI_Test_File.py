import tkinter
import fantasy_draft_rank as ranks

def bottom_fill(bot_frame):
    #8 Different People Rosters
    widget_dict = dict()
    #Fix this after
    POSITIONS = ['QB','RB','RB','WR','WR','TE','FLEX','FLEX']  
    
    for i in range(8):
        #One frame for each drafter        
        widget_dict[f'frame{i}'] = tkinter.Frame(bot_frame,\
            borderwidth=1)            
                
        #12 Players for each drafter(label, textbox, button)
        for j in range(8):
            if(i == 0 and j == 0):  
                #Label put in
                widget_dict[f'lbl_player_dict{j}'] = tkinter.Label(\
                    widget_dict[f'frame{i}'], \
                    text = 'Draft Player', borderwidth=1)
                widget_dict[f'lbl_player_dict{j}'].pack()
                #Textbox put in
                widget_dict[f'txt_player_dict{j}'] = tkinter.Entry(\
                    widget_dict[f'frame{i}'],\
                    borderwidth=1)
                widget_dict[f'txt_player_dict{j}'].pack()
                #Button put in
                widget_dict[f'btn_confirm'] = tkinter.Button(\
                    widget_dict[f'frame{i}'],\
                    borderwidth=1, text = 'Confirm')
                widget_dict[f'btn_confirm'].pack()
            if(i>0 and j == 0):
                #Labels put in
                widget_dict[f'lbl_drafter_dict{j}'] = tkinter.Label(\
                    widget_dict[f'frame{i}'], \
                    text = f'Opponent {i}', borderwidth=1)
                widget_dict[f'lbl_drafter_dict{j}'].pack()
                #Filler put in
                widget_dict[f'lbl_fill_dict{j}'] = tkinter.Label(\
                    widget_dict[f'frame{i}'], \
                    borderwidth=1)
                widget_dict[f'lbl_fill_dict{j}'].pack()
            
            #Labels put in
            widget_dict[f'lbl_dict{j}'] = tkinter.Label(\
                widget_dict[f'frame{i}'], \
                text = POSITIONS[j], borderwidth=1)
            widget_dict[f'lbl_dict{j}'].pack()
            
            #Textboxes put in
            widget_dict[f'txt_dict{j}'] = tkinter.Entry(\
                widget_dict[f'frame{i}'],\
                borderwidth=1, state = "disabled")
            widget_dict[f'txt_dict{j}'].pack()

        #Packs after everything is put in
        widget_dict[f'frame{i}'].pack(side = 'left')
    


def top_fill(root, player_names):
    top_scroll = tkinter.Scrollbar(root)
    top_scroll.pack(side = 'right', fill = "y")
    player_text = tkinter.Text(root, width = 125, yscrollcommand = top_scroll.set)
    player_text.insert('1.0', player_names)
    player_text.pack(side = 'top', fill = 'both')
    top_scroll.config(command = player_text.yview)


def main(player_names):
    #Creates overall window
    top = tkinter.Tk()
    top.title("Mock Draft")

    #Creates top half of window and calls method to fill in
    top_frame = tkinter.Frame(top, borderwidth=1)
    top_fill(top_frame,player_names)
    top_frame.pack(side = "top", fill = 'x')

    #Creates bottom half of window frame
    bot_frame = tkinter.Frame(top, borderwidth=1)
    bot_frame.pack(side = "bottom", fill = 'x')
    
    #Bottom half is filled with widgets and then container frame is packed
    bottom_fill(bot_frame)

    top.mainloop()

if __name__ == "__main__":
    main([1,2,3])