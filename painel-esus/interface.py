import customtkinter as ctk
import os.path
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


root = ctk.CTk()
root.geometry("800x600")



def existsEnv(root):
        frame = ctk.CTkFrame(master=root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)

        label = ctk.CTkLabel(master=frame, text="Painel Esus", font=("arial bold", 50))
        label.pack(pady=12, padx=10)
        
        image_path = os.getcwd()
        image_path = os.path.join(image_path, 'env.png')
        print(image_path)
        my_image = ctk.CTkImage(light_image=Image.open(image_path), dark_image=Image.open(image_path),
                                size=(100, 100))
        image_label = ctk.CTkLabel(master=frame, text="", font=("arial bold", 20), image=my_image)
        image_label.pack(pady=10)

        exist_file_label = ctk.CTkLabel(master=frame, text="Arquivo de configuração já existente!",
                                font=("arial bold", 15), 
                                width=600,
                                height=25,
                                corner_radius=5,
                                anchor="center",
                                wraplength=600)
        exist_file_label.pack(pady=10, padx=10)

        choose_option = ctk.CTkLabel(master=frame, text="Você pode testar novamente a conexão com o banco de dados ou criar uma nova configuração do Painel-Esus. Escolha a opção abaixo:", 
                                font=("arial bold", 15),
                                width=600,
                                height=25,
                                corner_radius=5,
                                anchor="center",
                                wraplength=600)
        choose_option.pack(pady=10, padx=10)

        test_connection_button = ctk.CTkButton(master=frame, text="Testar conexão")
        test_connection_button.pack(pady=12, padx=10)

        create_new_env_button = ctk.CTkButton(master=frame, text="Configurar novamente")
        create_new_env_button.pack(pady=12, padx=10)
        
        # progressBar = ctk.CTkProgressBar(frame, width=200, height=10, corner_radius=30)
        # progressBar.pack(pady=20)
        # progressBar.start()


def createEnv(inputHost, inputDatabase, inputUser,inputPassword, inputPort, inputCidade, inputEstado, inputUserAdmin, inputPasswordAdmin, inpoutPopolacao):
        print("Entrou aqui: ")
        print("Host: ", inputHost.get())
        with open(".env", "w",encoding='utf-8') as f:
                lines = [
                        "HOST="+inputHost.get()+"\n", 
                        "DATABASE="+inputDatabase.get()+"\n", 
                        "USER="+inputUser.get()+"\n", 
                        "PASSWORD="+inputPassword.get()+"\n", 
                        "PORT="+inputPort.get()+"\n", 
                        "CIDADE="+inputCidade.get()+"\n", 
                        "ESTADO="+inputEstado.get()+"\n",
                        "ADMIN_USR="+inputUserAdmin.get()+"\n", 
                        "ADMIN_PASS="+inputPasswordAdmin.get()+"\n", 
                        "POPULATION="+inpoutPopolacao.get() ]
                f.writelines(lines)
                f.close()


def createNewEnv():
        frame = ctk.CTkFrame(master=root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)
        inputHost = ctk.CTkEntry(master=frame, placeholder_text="Host:", width=600,
                                height=25,
                                corner_radius=10)
        inputHost.pack(pady=10, padx=10)

        inputDatabase = ctk.CTkEntry(master=frame, placeholder_text="Base de dados:", width=600,
                                height=25,
                                corner_radius=10)
        inputDatabase.pack(pady=10, padx=10)

        inputUser = ctk.CTkEntry(master=frame, placeholder_text="Usuário:", width=600,
                                height=25,
                                corner_radius=10)
        inputUser.pack(pady=10, padx=10)

        inputPassword = ctk.CTkEntry(master=frame, placeholder_text="Senha:", width=600,
                                height=25,
                                corner_radius=10)
        inputPassword.pack(pady=10, padx=10)

        inputPort = ctk.CTkEntry(master=frame, placeholder_text="Porta:", width=600,
                                height=25,
                                corner_radius=10)
        inputPort.pack(pady=10, padx=10)


        labelConfigPainel = ctk.CTkLabel(master=frame, text="Configuração do painel:")
        labelConfigPainel.pack(pady=12, padx=10)

        inputCidade = ctk.CTkEntry(master=frame, placeholder_text="Cidade:", width=600,
                                height=25,
                                corner_radius=10)
        inputCidade.pack(pady=10, padx=10)

        inputEstado = ctk.CTkEntry(master=frame, placeholder_text="Estado:", width=600,
                                height=25,
                                corner_radius=10)
        inputEstado.pack(pady=10, padx=10)

        inputUserAdmin = ctk.CTkEntry(master=frame, placeholder_text="Usuário:", width=600,
                                height=25,
                                corner_radius=10)
        inputUserAdmin.pack(pady=10, padx=10)

        inputPasswordAdmin = ctk.CTkEntry(master=frame, placeholder_text="Senha:", width=600,
                                height=25,
                                corner_radius=10)
        inputPasswordAdmin.pack(pady=10, padx=10)

        inpoutPopolacao = ctk.CTkEntry(master=frame, placeholder_text="População:", width=600,
                                height=25,
                                corner_radius=10)
        inpoutPopolacao.pack(pady=10, padx=10)

        button = ctk.CTkButton(master=frame, text="Testar conexão", command=lambda: createEnv(inputHost, inputDatabase, inputUser,inputPassword, inputPort, inputCidade, inputEstado, inputUserAdmin, inputPasswordAdmin, inpoutPopolacao))
        button.pack(pady=12, padx=10)

        checkbox = ctk.CTkCheckBox(master=frame, text="Lembrar conexão")
        checkbox.pack(pady=12, padx=10)

if os.path.exists('.env'):
        existsEnv(root)
else:
        createNewEnv()

root.mainloop()
