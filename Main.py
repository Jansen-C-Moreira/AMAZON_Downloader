
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from _thread import *


class StoreBooks:
    def __init__(self):
        self.caughtbooks = 0
        self.pagspassed = 0

class   AMZBot():
    def __init__(self, username, password, url, code):
        self.username = username
        self.password = password
        self.url = url
        self.code = code
        self.a = 0
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("int1.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enable", False)
        self.driver = webdriver.Firefox(
            firefox_profile=firefoxProfile
        )

    def login(self,):
        try:

            driver = self.driver
            driver.get("https://www.amazon.com.br/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com.br%2Fref%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=brflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
            loginusuario = driver.find_element_by_xpath("//input[@name='email']")
            loginusuario.clear()
            loginusuario.send_keys(self.username)
            buto = driver.find_element_by_id('continue').click()
            passwd = driver.find_element_by_xpath( "//input[@name='password']")
            passwd.clear()
            passwd.send_keys(self.password)
            time.sleep(2)
            buton = driver.find_element_by_id('signInSubmit').click()
            time.sleep(2)
        except:
            time.sleep(60)
        try:
            buton = driver.find_element_by_id('continue').click()
            time.sleep(30)
        except:
            pass

        self.takebooks()

    def takebooks(self):
        driver = self.driver
        driver.get(self.url)
        time.sleep(1)
        store = StoreBooks()
        while True:
            for n in range(1,1000):

                try:
                    clicar = driver.find_element_by_id('a-autoid-'+str(n)+'-announce').send_keys(Keys.SHIFT + Keys.CONTROL + Keys.ENTER)
                    store.caughtbooks += 1
                    print("Livro Pego({})".format(store.caughtbooks))
                    time.sleep(0.5)
                    driver.switch_to_window(driver.window_handles[-1])
                    time.sleep(1)
                    driver.close()
                    driver.switch_to_window(driver.window_handles[0])
                    time.sleep(1)
                except Exception as error:
                    #print("----")
                    pass
            try:

                nextpage = driver.find_element_by_class_name('a-last').click()
                store.pagspassed += 1
                print("Páginas passadas"+ str(store.pagspassed))
            except Exception as error:
                print(error)

            time.sleep(1)


def main():
    root = Tk()
    app = Window1(root)
    root.mainloop()
class Window1():
    def __init__(self, master):
        self.master = master
        self.master.title("BotInstagtram")
        self.master.geometry("700x500")
        self.frame = Frame(self.master)
        self.frame.pack()
        self.user = StringVar()
        self.passwd = StringVar()
        self.url = StringVar()
        self.LabelTitle = Label(self.frame, text="BOT AMAZON FREE BOOKS", font=("verdana", 30), bd=20, justify=LEFT)
        self.LabelTitle.grid(row=0, columnspan=2, pady=20, sticky=W)
        #-----------------------------------------------------------
        #Frames
        self.Loginframe1 = Frame(self.frame, width=500, height=150, bd=20, relief='ridge')
        self.Loginframe1.grid(row=1, column=0, sticky=W)
        self.Loginframe2 = Frame(self.frame, width=500, height=50, bd=10, relief='ridge')
        self.Loginframe2.grid(row=2, column=0, sticky=W)
        self.Loginframe4 = Frame(self.frame, width=500, height=50, bd=10, relief='ridge')
        self.Loginframe4.grid(row=1, column=1, sticky=W)

        ##########################################
        #Bar

        #-----------------------------------------------------------
        #Radio Button
        self.language = Label(self.Loginframe4, text="Book Language", font=('arial', 12, "bold"))
        self.language.grid()
        self.Valor= IntVar()
        self.Italian = Radiobutton(self.Loginframe4, text="Italian", value=1, variable=self.Valor, command=self.ChangingIT)
        self.Italian.grid(sticky=W)
        self.En = Radiobutton(self.Loginframe4, text="English", value=2, variable=self.Valor, command=self.ChangingEN)
        self.En.grid(sticky=W)
        self.Spanish = Radiobutton(self.Loginframe4, text="Spanish", value=3, variable=self.Valor, command=self.ChangingES)
        self.Spanish.grid(sticky=W)
        self.PT = Radiobutton(self.Loginframe4, text="Portuguese", value=4, variable=self.Valor, command=self.ChangingPT)
        self.PT.grid(sticky=W)
        self.Loginframe4.config(self.En.select())
        #-----------------------------------------------------------
        #StringVar

        self.url.set('https://www.amazon.com.br/s?i=digital-text&bbn=5475882011&rh=n%3A5308307011%2Cn%3A5308308011%2Cn%3A5475882011%2Cp_36%3A5560478011%2Cp_n_feature_browse-bin%3A6406077011&dc&language=pt_BR&_encoding=UTF8&fst=as%3Aoff&linkCode=sl2&linkId=c74a3b3b1606b3a2c5d5249ccab38e13&primeCampaignId=prime_assoc_ft&qid=1591627747&rnid=6406076011&tag=ynv-20&ref=sr_nr_p_n_feature_browse-bin_2')

        self.code = StringVar()
        #-----------------------------------------------------------
        #Frame1
        self.LabelUser = Label(self.Loginframe1, text="Name", font=('arial', 15, "bold"))
        self.LabelUser.grid()
        self.LabeltxtUser = Entry(self.Loginframe1, text="Name", font=('arial', 15, "bold"), textvariable=self.user)
        self.LabeltxtUser.grid(row=0, column=1)
        self.LabelPasswd = Label(self.Loginframe1, text="Pass", font=('arial', 15, "bold"))
        self.LabelPasswd.grid(row=1, column=0)
        self.LabeltxtPasswd = Entry(self.Loginframe1, text="Senha", font=('arial', 15, "bold"), show="*", textvariable=self.passwd)
        self.LabeltxtPasswd.grid(row=1, column=1)
        self.Botar = Label(self.Loginframe1, text="URL", font=('arial', 12, 'bold'))
        self.Botar.grid(row=2, column=0)
        self.LabeltxtURL = Entry(self.Loginframe1, text="URL", font=('arial', 15, "bold"), textvariable=self.url)
        self.LabeltxtURL.grid(row=2, column=1)
        #-----------------------------------------------------------
        #Frame2

        self.TestarConta = Button(self.Loginframe2, text="Run", width=10, font=('arial', 12, 'bold'), command=self.start)
        self.TestarConta.grid()
        #-----------------------------------------------------------
        #Frame3
        self.duvida = Button(self.Loginframe2, text="?", width=6, font=('arial', 12, 'bold'), command=self.showInfo)
        self.duvida.grid(row=0, column=1)


    def showInfo(self):
        tkinter.messagebox.showinfo("Info", "This is a bot that take every free book from Amazon, you can choose de language,\n and the URL(Based on the language you want), if you want to take every book after\n some specific page you can do it too, you just need to put the url in fild.\n Do not close the webBrowser before it took all the books or the app you crash.\n\n\nMade By Jansen Moreira")

    def ChangingIT(self):

        self.url.set("https://www.amazon.com.br/s?i=digital-text&bbn=5475882011&rh=n%3A5308307011%2Cn%3A5308308011%2Cn%3A5475882011%2Cp_36%3A5560478011%2Cp_n_feature_browse-bin%3A12636746011&dc&language=pt_BR&fst=as%3Aoff&linkCode=sl2&linkId=02095141d486184646c643456040a5b7&qid=1591752889&rnid=6406076011&ref=sr_nr_p_n_feature_browse-bin_2")

    def ChangingEN(self):
       self.url.set('https://www.amazon.com.br/s?i=digital-text&bbn=5475882011&rh=n%3A5308307011%2Cn%3A5308308011%2Cn%3A5475882011%2Cp_36%3A5560478011%2Cp_n_feature_browse-bin%3A6406077011&dc&language=pt_BR&_encoding=UTF8&fst=as%3Aoff&linkCode=sl2&linkId=c74a3b3b1606b3a2c5d5249ccab38e13&primeCampaignId=prime_assoc_ft&qid=1591627747&rnid=6406076011&tag=ynv-20&ref=sr_nr_p_n_feature_browse-bin_2')

    def ChangingES(self):
        self.url.set("https://www.amazon.com.br/s?i=digital-text&bbn=5475882011&rh=n%3A5308307011%2Cn%3A5308308011%2Cn%3A5475882011%2Cp_36%3A5560478011%2Cp_n_feature_browse-bin%3A12636744011&dc&language=pt_BR&fst=as%3Aoff&linkCode=sl2&linkId=02095141d486184646c643456040a5b7&qid=1591753012&rnid=6406076011&ref=sr_nr_p_n_feature_browse-bin_5")

    def ChangingPT(self):
        self.url.set("https://www.amazon.com.br/s?i=digital-text&bbn=5475882011&rh=n%3A5308307011%2Cn%3A5308308011%2Cn%3A5475882011%2Cp_36%3A5560478011%2Cp_n_feature_browse-bin%3A6406078011&dc&language=pt_BR&fst=as%3Aoff&linkCode=sl2&linkId=02095141d486184646c643456040a5b7&qid=1591753084&rnid=6406076011&ref=sr_nr_p_n_feature_browse-bin_5")

    def start(self):
        start_new_thread(self.Login, (1,))

    def Login(self, nada):
        nada =0
        name = (self.user.get())
        passwd = (self.passwd.get())
        url = (self.url.get())
        code = self.code
        self.jansen = AMZBot(name, passwd, url, code)
        self.jansen.login()



if __name__ == '__main__':
    main()








