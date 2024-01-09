import customtkinter
import os
# from app import app
# from app.models.BaseConfig import BaseConfig
# import logging
# from dotenv import load_dotenv
# load_dotenv()


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


root = customtkinter.CTk()
root.geometry("1000x900")


# def startServer():
#     print('INICIANDO')    
#     config = {
#         "host":os.environ['HOST'],
#         "dataBase":os.environ['DATABASE'],
#         "user":os.environ['USER'],
#         "pwd":os.getenv('PASSWORD', ''),
#         "port": os.environ['PORT']  
#     }
#     print(config)
#     server_run( 
#             None, None, None, config, None         
#             )


# def server_run(pagesPath, dataPath, dir_pages, config, addMsg=None):
#     print('RODANDO SERVIDOR')
#     bse = BaseConfig.getInstance()
#     bse._host = config['host']
#     bse._database = config['dataBase']
#     bse._user= config['user']
#     bse._passwd= config['pwd']
#     bse._port = config['port']
    
#     app.run(host='0.0.0.0', port=5001)

        
def createEnv():
        print(inputHost.get())
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


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Painel Saúde")
label.pack(pady=12, padx=10)


label2 = customtkinter.CTkLabel(master=frame, text="Configuração do banco de dados:")
label2.pack(pady=12, padx=10)


inputHost = customtkinter.CTkEntry(master=frame, placeholder_text="Host:", width=600,
                               height=25,
                               corner_radius=10)
inputHost.pack(pady=10, padx=10)


inputDatabase = customtkinter.CTkEntry(master=frame, placeholder_text="Base de dados:", width=600,
                               height=25,
                               corner_radius=10)
inputDatabase.pack(pady=10, padx=10)

inputUser = customtkinter.CTkEntry(master=frame, placeholder_text="Usuário:", width=600,
                               height=25,
                               corner_radius=10)
inputUser.pack(pady=10, padx=10)

inputPassword = customtkinter.CTkEntry(master=frame, placeholder_text="Senha:", width=600,
                               height=25,
                               corner_radius=10)
inputPassword.pack(pady=10, padx=10)

inputPort = customtkinter.CTkEntry(master=frame, placeholder_text="Porta:", width=600,
                               height=25,
                               corner_radius=10)
inputPort.pack(pady=10, padx=10)


labelConfigPainel = customtkinter.CTkLabel(master=frame, text="Configuração do painel:")
labelConfigPainel.pack(pady=12, padx=10)

inputCidade = customtkinter.CTkEntry(master=frame, placeholder_text="Cidade:", width=600,
                               height=25,
                               corner_radius=10)
inputCidade.pack(pady=10, padx=10)

inputEstado = customtkinter.CTkEntry(master=frame, placeholder_text="Estado:", width=600,
                               height=25,
                               corner_radius=10)
inputEstado.pack(pady=10, padx=10)

inputUserAdmin = customtkinter.CTkEntry(master=frame, placeholder_text="Usuário:", width=600,
                               height=25,
                               corner_radius=10)
inputUserAdmin.pack(pady=10, padx=10)

inputPasswordAdmin = customtkinter.CTkEntry(master=frame, placeholder_text="Senha:", width=600,
                               height=25,
                               corner_radius=10)
inputPasswordAdmin.pack(pady=10, padx=10)

inpoutPopolacao = customtkinter.CTkEntry(master=frame, placeholder_text="População:", width=600,
                               height=25,
                               corner_radius=10)
inpoutPopolacao.pack(pady=10, padx=10)

button = customtkinter.CTkButton(master=frame, text="Testar conexão", command=createEnv)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Lembrar conexão")
checkbox.pack(pady=12, padx=10)

root.mainloop()
