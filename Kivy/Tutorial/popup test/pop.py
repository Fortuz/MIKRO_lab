class SettingsWindow(Screen):
pretty_list_people = StringProperty ("")
pretty_list_jobs = StringProperty ("")

def get_Jobs(self):
    return WindowManager.jobs

def get_People(self):
    return WindowManager.people

def Pretty_Print_People(self, ppl_list):
    self.pretty_list_people = ""
    for person in ppl_list:
        self.pretty_list_people += person + "\n"

def Pretty_Print_Jobs(self, job_list):
    self.pretty_list_jobs = ""
    for job in job_list:
        self.pretty_list_jobs += job + "\n"

def show_popup(self):
    show = PopupAddJob()
    popupWindow = Popup(title="Add Job", content=show, size_hint=(None, None), size=(200, 200))
    popupWindow.open()

def dismiss_popup(self):
    self.popupWindow.dismiss()
