import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Main_Window(Gtk.Window):



    def __init__(self):
        #WINDOW DESCRIPTION

        Gtk.Window.__init__(self, title = "Medical App")
        self.set_border_width(10)
        self.set_default_size(1000, 800)
        check = False


        #MAKING BOXES

        self.hbox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 10)
        self.vbox1 = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 5)
        self.vbox2 = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 5)

        # TODO : MAKE THE MENU BAR FILE CREATED

        main_menu_bar = Gtk.MenuBar()

        #FILE MENU

        file_menu = Gtk.Menu()
        file_menu_dropdown = Gtk.MenuItem("File")

        file_new = Gtk.MenuItem("New")
        file_open = Gtk.MenuItem("Open")
        file_exit = Gtk.MenuItem("Exit")

        file_exit.connect("activate", Gtk.main_quit)
        file_open.connect("activate", self.open_file)
        file_new.connect("activate", self.new_file)

        file_menu_dropdown.set_submenu(file_menu)

        file_menu.append(file_new)
        file_menu.append(file_open)
        file_menu.append(Gtk.SeparatorMenuItem())
        file_menu.append(file_exit)

        main_menu_bar.append(file_menu_dropdown)


        #EDIT MENU

        edit_menu = Gtk.Menu()
        edit_menu_dropdown = Gtk.MenuItem("Edit")

        edit_cut = Gtk.MenuItem("cut")
        edit_copy = Gtk.MenuItem("copy")
        edit_paste = Gtk.MenuItem("paste")
        edit_delete = Gtk.MenuItem("delete")

        edit_cut.connect("activate", self.cut_edit)
        edit_copy.connect("activate", self.copy_edit)
        edit_paste.connect("activate", self.paste_edit)
        edit_delete.connect("activate", self.delete_edit)

        edit_menu_dropdown.set_submenu(edit_menu)

        edit_menu.append(edit_cut)
        edit_menu.append(edit_copy)
        edit_menu.append(edit_paste)
        edit_menu.append(Gtk.SeparatorMenuItem())
        edit_menu.append(edit_delete)

        main_menu_bar.append(edit_menu_dropdown)

        #HELP MENU

        help_menu = Gtk.Menu()
        help_menu_dropdown = Gtk.MenuItem("Help")

        help_about = Gtk.MenuItem("about")

        help_about.connect("activate", self.about_help)

        help_menu_dropdown.set_submenu(help_menu)

        help_menu.append(help_about)

        main_menu_bar.append(help_menu_dropdown)

        #ADDING MENU BAR IN THE BOX

        self.hbox.pack_start(main_menu_bar, True, True, 0)


        #ADDING VERTICAL BOX INSIDE THE HORIZONTAL BOX

        self.hbox.pack_start(self.vbox1, True, True, 0)
        boxseparator = Gtk.Separator(orientation = Gtk.Orientation. VERTICAL)
        self.hbox.pack_start(boxseparator, True, True, 0)
        self.hbox.pack_start(self.vbox2, True, True, 0)




        #PATIENT'S DETAILS FILL

        label_name = Gtk.Label("Patient's Name : ")
        self.vbox1.pack_start(label_name, True, True, 0)
        name = Gtk.Entry()
        self.vbox1.pack_start(name, True, True, 5)

        label_age = Gtk.Label("Patient's Age : ")
        self.vbox1.pack_start(label_age, True, True, 0)
        age = Gtk.Entry()
        self.vbox1.pack_start(age, True, True, 5)

        label_time = Gtk.Label("Since When the problems started :")
        self.vbox1.pack_start(label_time, True, True, 0)
        time = Gtk.Entry()
        self.vbox1.pack_start(time, True, True, 5)



        #SYMPTOMS DETAILS
        symptom1 = Gtk.Entry()
        symptom2 = Gtk.Entry()
        symptom3 = Gtk.Entry()
        symptom4 = Gtk.Entry()
        symptom5 = Gtk.Entry()

        self.vbox2.pack_start(symptom1, False, True, 5)
        self.vbox2.pack_start(symptom2, False, True, 5)
        self.vbox2.pack_start(symptom3, False, True, 5)
        self.vbox2.pack_start(symptom4, False, True, 5)
        self.vbox2.pack_start(symptom5, False, True, 5)


        #SET COMPLETION MODE IN THE SYMPTOMS

        completion1 = Gtk.EntryCompletion()
        completion2 = Gtk.EntryCompletion()
        completion3 = Gtk.EntryCompletion()
        completion4 = Gtk.EntryCompletion()
        completion5 = Gtk.EntryCompletion()
        self.liststore1 = Gtk.ListStore(str)
        self.liststore2 = Gtk.ListStore(str)
        self.liststore3 = Gtk.ListStore(str)
        self.liststore4 = Gtk.ListStore(str)
        self.liststore5 = Gtk.ListStore(str)
        for i in ['Head Ache', 'Loose Motion', 'Breathing Problems', 'Sore Throat', 'Red Eyes', 'Body Pain', 'Ulcer']:
            self.liststore1.append([i])
            self.liststore2.append([i])
            self.liststore3.append([i])
            self.liststore4.append([i])
            self.liststore5.append([i])

        completion1.set_model(self.liststore1)
        completion2.set_model(self.liststore2)
        completion3.set_model(self.liststore3)
        completion4.set_model(self.liststore4)
        completion5.set_model(self.liststore5)
        completion1.set_text_column(0)
        completion2.set_text_column(0)
        completion3.set_text_column(0)
        completion4.set_text_column(0)
        completion5.set_text_column(0)
        symptom1.set_completion(completion1)
       #symptom1.connect('activate', self.activate_cb)
        symptom2.set_completion(completion2)
        #symptom2.connect('activate', self.activate_cb)
        symptom3.set_completion(completion3)
        #symptom3.connect('activate', self.activate_cb)
        symptom4.set_completion(completion4)
        #symptom4.connect('activate', self.activate_cb)
        symptom5.set_completion(completion5)
        #symptom5.connect('activate', self.activate_cb)


        #ADD MORE BUTTON

        self.add_more = Gtk.Button("ADD MORE SYMPTOMS")
        self.add_more.connect("clicked", self.button_clicked)
        self.vbox2.pack_start(self.add_more, False, True, 5)

        if check == True:
            symptom = Gtk.Entry()
            self.vbox2.pack_start(symptom, False, True, 5)
            check = False



        #ADD HORIZONTAL BOX TO THE WINDOW WHICH CONTAINS ALL THE BOXES

        self.add(self.hbox)


        #FUNCTION TO CALL WHEN ADD_MORE BUTTON IS CLICKED!


    def button_clicked(self, widget):

        self.vbox2.remove(self.add_more)


    def activate_cb(self, entry):
        text = entry.get_text()
        if text:
            if text not in [row[0] for row in self.liststore]:
                self.liststore.append([text])
                entry.set_text(text)
        return




    def open_file(self, widget):

        dialog = Gtk.FileChooserDialog("Select Your File", self, Gtk.FileChooserAction.OPEN, ("Cancel", Gtk.ResponseType.CANCEL, "Ok", Gtk.ResponseType.OK))
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            #TODO OPENING OF THE FILE
            print("HOLA")

        elif response == Gtk.ResponseType.CANCEL:
            dialog.destroy()

        dialog.destroy()




    def new_file(self, widget):
        #TODO IMPROVEMENT

        open("Hack_app.py")



    def cut_edit(self, widget):
        print("")
        #TODO COMPLETE THIS FUNCTION


    def copy_edit(self, widget):
        print("")
        #TODO COMPLETE THIS FUNCTION


    def paste_edit(self, widget):
        print("")
        #TODO COMPLETE THIS FUNCTION


    def delete_edit(self, widget):
        print("")
        #TODO COMPLETE THIS FUNCTION



    def about_help(self, widget):
        print("")
        #TODO COMPLETE THIS FUNCTION




























window = Main_Window()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()