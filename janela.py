# -*- coding: utf-8 -*-

import cv2
import time
import face_recognition
import sys
import os

from reconhecimento import *
from tkinter import *

def main():
	class Application:
		def __init__(self, master=None):

			self.Titulo = ("Arial", "20")
			self.fontetexto = ("Arial", "12")
			self.fontebotoes = ("Arial", "12")
			self.titulo = Frame(master)
			#self.titulo["pady"] = 10
			#self.titulo["padx"] = 20
			self.titulo.pack(side=TOP)
			self.titulo.pack()

			#entidade primeiro conteiner

			self.primeiroContainer = Frame(master)
			#self.primeiroContainer["pady"] = 10
			#self.primeiroContainer["padx"] = 20
			self.primeiroContainer.pack(side=TOP)
			self.primeiroContainer.pack()

			#botão Iniciar Reconhecimento

			self.reconhecimento = Button(self.primeiroContainer, font=self.fontebotoes)
			self.reconhecimento["text"] = "Iniciar Reconhecimento"
			#self.reconhecimento["font"] = ("Arial", "10")
			#self.reconhecimento["width"] = 30
			self.reconhecimento["command"] = self.rotina1
			self.reconhecimento.pack()

			#botão cadastrar
			'''
			self.cadastrar = Button(self.primeiroContainer)
			self.cadastrar["text"] = "Cadastrar novo usuário"
			self.cadastrar["font"] = ("Arial", "10")
			#self.cadastrar["width"] = 30
			self.cadastrar["command"] = self.rotina2
			self.cadastrar.pack()

			#botão sair

			self.sair = Button(self.primeiroContainer)
			#self.sair["pady"] = 5
			self.sair["text"] = "sair"
			self.sair["font"] = ("Arial", "10")
			#self.sair["width"] = 7
			self.sair["command"] = self.primeiroContainer.quit
			#self.sair.pack(side=RIGTH)
			self.sair.pack ()
			'''

			self.mensagem = Frame(master)
			self.mensagem.pack()
			self.mensagem["pady"] = 10
			self.mensagem["padx"] = 10
			self.msg = Label(self.titulo, text="Controle de Acesso com Reconhecimento Facial ", font=self.Titulo)
			#self.msg["font"] = ("Arial", "20")
			self.mensagem.pack(side=TOP)
			self.msg.pack ()

			self.mensagem = Frame(master)
			self.mensagem.pack()
			self.mensagem["pady"] = 10
			self.mensagem["padx"] = 10
			self.msg = Label(self.mensagem, text="Aperte <Q> para fechar a janela de reconhecimento ", font=self.fontetexto)
			#self.msg["font"] = ("Arial", "10")
			self.msg.pack ()

			self.mensagem0 = Frame(master)
			self.mensagem0.pack()
			self.mensagem0["pady"] = 10
			self.mensagem0["padx"] = 10
			self.msg = Label(self.mensagem0, text="Para cadastrar um novo usuário, escreva o nome e nível de acesso ", font=self.fontetexto)
			#self.msg["font"] = ("Arial", "10")
			self.msg.pack ()
			
			#primeiro conteiner

			self.Container = Frame(master)
			self.Container["padx"] = 20
			self.Container.pack()

			self.nomeLabel = Label(self.Container,text="Nome", font=self.fontetexto)
			self.nomeLabel.pack(side=LEFT)

			self.nome = Entry(self.Container)
			self.nome["width"] = 29
			self.nome["font"] = self.fontetexto
			self.nome.pack(side=LEFT)

			#caixa do cadastro

			self.caixacadastro = Frame(master)
			self.caixacadastro.pack()

			#segundo conteiner
			
			self.Container2 = Frame(master)
			self.Container2["padx"] = 20
			self.Container2.pack()

			self.acessoLabel = Label(self.Container2,text="Nível de acesso", font=self.fontetexto)
			self.acessoLabel.pack(side=LEFT)
			
			global var0
			self.var0 = StringVar()
			a = Checkbutton(master, text="Porta 'a'", variable=self.var0, onvalue="a", offvalue="", command=self.cb, font=self.fontetexto)
			a.pack()

			global var1
			self.var1 = StringVar()
			b = Checkbutton(master, text="Porta 'b'", variable=self.var1, onvalue="b", offvalue="", command=self.cb, font=self.fontetexto)
			b.pack()

			global var2
			self.var2 = StringVar()
			c = Checkbutton(master, text="Porta 'c'", variable=self.var2, onvalue="c", offvalue="", command=self.cb, font=self.fontetexto)
			c.pack()

			global per
			per = ""

			#Mensagem de quando apertar o botão

			self.mensagem1 = Frame(master)
			self.mensagem1.pack()
			self.mensagem1["padx"] = 10
			self.mensagem1["pady"] = 10
			self.msg = Label(self.mensagem1, text="Após digitar os dados, click no botão 'Abrir Camera' para tirar a foto", font=self.fontetexto)
			#self.msg["font"] = ("Arial", "10")
			self.msg.pack ()

			#entidade para atrelar os botões

			self.botoes = Frame(master)
			self.botoes.pack()

			#botao Abrir Camera
			
			#self.quartoContainer = Frame(master)
			#self.quartoContainer["pady"] = 22
			#self.quartoContainer.pack()
			self.abrircamera = Button(self.botoes, font=self.fontebotoes)
			self.abrircamera["text"] = "Abrir Camera"
			#self.abrircamera["font"] = ("Arial", "10")
			#self.abrircamera["width"] = 20
			self.abrircamera["command"] = self.tirafoto
			self.abrircamera.pack(side=LEFT)

			#botao alterar cadastro

			self.alterar = Button(self.botoes, font=self.fontebotoes)
			self.alterar["text"] = "Alterar Cadastro"
			self.alterar["command"] = self.rotina2
			self.alterar.pack(side=LEFT)
			#self.alterar.pack()

			#botao Cancelar

			#self.conteinersair = Frame(master)
			self.Cancelar = Button(self.botoes, font=self.fontebotoes,fg="red", bg="grey")
			#self.Cancelar["pady"] = 5
			self.Cancelar["text"] = "Fechar Aplicação"
			#self.Cancelar["font"] = ("Arial", "10")
			#self.Cancelar["width"] = 10
			self.Cancelar["command"] = self.mensagem0.quit
			#self.Cancelar.pack(side=RIGHT)
			self.Cancelar.pack ()
			
			#mensagem para tirar a foto

			self.widget = Frame(master)
			self.widget.pack()
			self.msg = Label(self.widget, text="Aperte <ESC> para sair do modo camera ou <s> para Salvar a foto e finalizar o cadastro", font=self.fontetexto)
			#self.msg["font"] = ("Arial", "10")
			self.msg.pack ()

		def cb(self):
			global per
			#per = self.var0.get()
			per = "{}{}{}".format(self.var0.get(), self.var1.get(), self.var2.get())
			#print ("per:", per)
			return per

		def rotina1(self):
			#print ('reconhecimento')
			reconhecimento()
			#cv2.destroyAllWindows()

		def rotina2(self):
			print ('alterar cadastro')

			self.novoLabel = Label(self.caixacadastro,text="Novo nome", font=self.fontetexto)
			self.novoLabel.pack(side=LEFT)

			self.novo = Entry(self.caixacadastro)
			self.novo["width"] = 21
			self.novo["font"] = self.fontetexto
			#self.novo.pack(side=LEFT)
			self.novo.pack()

			self.alterar = Button(self.caixacadastro, font=self.fontebotoes)
			self.alterar["text"] = "confirmar alteração"
			self.alterar["command"] = self.confirma
			#self.alterar["command"] = self.valida
			self.alterar.pack(side=LEFT)

		def valida(self):

			self.novo.destroy()
			self.novoLabel.destroy()
			self.alterar.destroy()
			self.volta.destroy()


		def confirma(self):
			nome_antigo = self.nome.get()
			novo_nome = self.novo.get()
			acesso = "{}{}{}".format(self.var0.get(), self.var1.get(), self.var2.get())

			self.alterar["command"] = self.valida

			for fotos in os.listdir('./'):
				if fotos.endswith('.jpg'):
					dados = fotos.split('.')[0].split('_')
					#print('{} {}'.format(dados[0], dados[1]))
					#nome = str(raw_input("nome a alterar:"))
					#nome = 'Mansur'
					#acesso = str(raw_input("Novo nivel de acesso:"))
					#acesso = 'abc'
					if str(dados[0]) == nome_antigo:
						#nome_arquivo = str(dados[0]) + "_" + acesso + '.jpg'
						nome_arquivo = novo_nome + "_" + acesso + '.jpg'
						os.rename(fotos, nome_arquivo)
						print('{} {} alterado para: {} {}'.format(dados[0], dados[1], novo_nome, acesso))
						self.volta = Button(self.caixacadastro, font=self.fontebotoes)
						self.volta["text"] = "Cancelar alteração"
						self.volta["command"] = self.valida
						self.alterar["command"] = self.valida
						self.volta.pack(side=RIGHT)


		def tirafoto(self):
			aba = self.nome.get()
			#per = self.acesso.get()

			print ("nome do arquivo: {}_{}.jpg".format(aba, per))
			
			#aba = str(input("Insira um nome:"))
			#per = str(input("Nivel e acesso:"))

			camera_port = 0

			nFrames = 30

			camera = cv2.VideoCapture(camera_port)
			
			file = "/home/mansur/Downloads/TCC/{}_{}.jpg".format(aba, per) 
			#file = "/home/pi/Downloads/Programa_final/{}_{}.jpg".format(aba, per)
			#file = "/home/mansur/Downloads/TCC/{}.jpg".format(aba)

			print ("Digite <ESC> para sair / <s> para Salvar")

			emLoop= True

			while(emLoop):

				retval, img = camera.read()
				cv2.imshow('Foto',img)

				k = cv2.waitKey(100)

				if k == 27:
					emLoop= False


				elif k == ord('s'):
					cv2.imwrite(file,img)
					#self.Cancelar["command"] = self.cancelar.quit
					cv2.destroyAllWindows()
					emLoop= False

			cv2.destroyAllWindows()
			camera.release()


		if __name__ == '__main__':
			import sys
			sys.exit((sys.argv))


	root = Tk()
	Application(root)
	root.mainloop()
