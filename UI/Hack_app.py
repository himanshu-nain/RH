import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4



class Main_Window(Gtk.Window):



    def __init__(self):
        #WINDOW DESCRIPTION

        Gtk.Window.__init__(self, title = "Medical App")
        self.set_border_width(10)
        self.set_default_size(1000, 800)


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
        file_save = Gtk.MenuItem("Save")
        file_exit = Gtk.MenuItem("Exit")

        file_exit.connect("activate", Gtk.main_quit)
        file_save.connect("activate", self.save_file)
        file_new.connect("activate", self.new_file)

        file_menu_dropdown.set_submenu(file_menu)

        file_menu.append(file_new)
        file_menu.append(file_save)
        file_menu.append(Gtk.SeparatorMenuItem())
        file_menu.append(file_exit)

        main_menu_bar.append(file_menu_dropdown)


        #ADDING MENU BAR IN THE BOX

        self.hbox.pack_start(main_menu_bar, True, True, 0)


        #ADDING LABEL TITLE OF WINDOW




        #ADDING VERTICAL BOX INSIDE THE HORIZONTAL BOX

        self.hbox.pack_start(self.vbox1, True, True, 0)
        boxseparator = Gtk.Separator(orientation = Gtk.Orientation. VERTICAL)
        self.hbox.pack_start(boxseparator, True, True, 0)
        self.hbox.pack_start(self.vbox2, True, True, 0)




        #PATIENT'S DETAILS FILL

        self.label_name = Gtk.Label("Patient's Name : ")
        self.vbox1.pack_start(self.label_name, False, True, 0)
        self.name = Gtk.Entry()
        self.vbox1.pack_start(self.name, False, True, 5)

        self.label_age = Gtk.Label("Patient's Age : ")
        self.vbox1.pack_start(self.label_age, False, True, 0)
        self.age = Gtk.Entry()
        self.vbox1.pack_start(self.age, False, True, 5)

        label_time = Gtk.Label("Since When the problems started :")
        self.vbox1.pack_start(label_time, False, True, 0)
        time = Gtk.Entry()
        self.vbox1.pack_start(time, False, True, 5)



        #SYMPTOMS DETAILS
        self.symptom1 = Gtk.Entry()
        self.symptom2 = Gtk.Entry()
        self.symptom3 = Gtk.Entry()
        self.symptom4 = Gtk.Entry()
        self.symptom5 = Gtk.Entry()

        self.vbox2.pack_start(self.symptom1, False, True, 5)
        self.vbox2.pack_start(self.symptom2, False, True, 5)
        self.vbox2.pack_start(self.symptom3, False, True, 5)
        self.vbox2.pack_start(self.symptom4, False, True, 5)
        self.vbox2.pack_start(self.symptom5, False, True, 5)


        #SET COMPLETION MODE IN THE SYMPTOMS

        completion1 = Gtk.EntryCompletion()
        completion2 = Gtk.EntryCompletion()
        completion3 = Gtk.EntryCompletion()
        completion4 = Gtk.EntryCompletion()
        completion5 = Gtk.EntryCompletion()
        self.liststore = Gtk.ListStore(str)
        problems = ['Head Ache', 'Loose Motion', 'Breathing Problems', 'Sore Throat', 'Red Eyes', 'Body Pain', 'Ulcer']
        for i in problems:
            self.liststore.append([i])


        self.treeview = Gtk.TreeView(self.liststore)


        completion1.set_model(self.liststore)
        completion2.set_model(self.liststore)
        completion3.set_model(self.liststore)
        completion4.set_model(self.liststore)
        completion5.set_model(self.liststore)
        completion1.set_text_column(0)
        completion2.set_text_column(0)
        completion3.set_text_column(0)
        completion4.set_text_column(0)
        completion5.set_text_column(0)
        self.symptom1.set_completion(completion1)
        selection1 = self.treeview.get_selection()
        result = selection1.get_selected()
        # if result:
        #     self.liststore, iter = result
        #     self.liststore.remove(iter)

        # for row in self.liststore:
        #     if self.liststore[row] == symptom1.get_text():
        #         self.liststore.remove(row.iter)
        #         break
        #  #symptom1.connect('activate', self.activate_cb)

        self.symptom2.set_completion(completion2)
        #symptom2.connect('activate', self.activate_cb)
        self.symptom3.set_completion(completion3)
        #symptom3.connect('activate', self.activate_cb)
        self.symptom4.set_completion(completion4)
        #symptom4.connect('activate', self.activate_cb)
        self.symptom5.set_completion(completion5)
        #symptom5.connect('activate', self.activate_cb)


        #ADD MORE BUTTON

        self.add_more = Gtk.Button("ADD MORE SYMPTOMS")
        self.add_more.connect("clicked", self.button_clicked)
        self.vbox2.pack_start(self.add_more, False, True, 5)



        #ADD HORIZONTAL BOX TO THE WINDOW WHICH CONTAINS ALL THE BOXES

        self.add(self.hbox)


        #FUNCTION TO CALL WHEN ADD_MORE BUTTON IS CLICKED!


    def button_clicked(self, widget):

        #self.vbox2.remove(self.add_more)
        symptom = Gtk.Entry()
        self.vbox2.pack_end(symptom, False, True, 0)



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


    def save_file(self, widget):
        c = canvas.Canvas(self.name.get_text(), pagesize=A4)

        c.setFont('Helvetica', 20, leading=None)
        c.drawString(240, 810, "Patient's Details")
        c.setFont('Helvetica', 16, leading = None)
        c.drawString(5, 750, "Name : ")
        c.setFont('Helvetica', 16, leading = None)
        c.drawString(70, 750, self.name.get_text())
        c.setFont('Helvetica', 16, leading=None)
        c.drawString(5, 710, "Age : ")
        c.setFont('Helvetica', 16, leading=None)
        c.drawString(70,710, self.age.get_text())
        c.setFont('Helvetica', 20, leading=None)
        c.drawString(270, 650, "Symptoms")
        c.setFont('Helvetica', 16, leading=None)
        c.drawString(5, 590, "1. ")
        c.setFont('Helvetica', 16, leading=None)
        c.drawString(20, 590, self.symptom1.get_text())
        c.setFont('Helvetica', 16, leading=None)
        c.drawString(5, 550, "2. ")
        c.setFont('Helvetica', 16, leading=None)
        c.drawString(20, 550, self.symptom2.get_text())
        c.setFont('Helvetica', 16, leading=None)
        c.drawString(5, 510, "3. ")
        c.setFont('Helvetica', 16, leading=None)
        c.drawString(20, 510, self.symptom3.get_text())
        c.setFont('Helvetica', 16, leading=None)
        c.drawString(5, 470, "4. ")
        c.setFont('Helvetica', 16, leading=None)
        c.drawString(20, 470, self.symptom4.get_text())
        c.setFont('Helvetica', 16, leading=None)
        c.drawString(5,430, "5. ")
        c.setFont('Helvetica', 16, leading=None)
        c.drawString(20, 430, self.symptom5.get_text())
        c.showPage()
        c.save()































window = Main_Window()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()