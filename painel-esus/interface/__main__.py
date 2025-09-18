# pylint: disable=R0913, R0915, C0121, W1514, W0622, C0103, W0212, W0612, W0404
import json
import logging
import os.path
import threading
import time

import customtkinter as ctk
import pandas as pd
from customtkinter import CTkProgressBar, IntVar
from PIL import Image

# from src.errors.logging import logging
from src.infra.db.settings.connection import DBConnectionHandler

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


def center_window_to_display(
    Screen: ctk, width: int, height: int, scale_factor: float = 1.0
):
    """Centers the window to the main display/monitor"""
    screen_width = Screen.winfo_screenwidth()
    screen_height = Screen.winfo_screenheight()
    x = int(((screen_width / 2) - (width / 2)) * scale_factor)
    y = int(((screen_height / 2) - (height / 1.5)) * scale_factor)
    return f"{width}x{height}+{x}+{y}"


root = ctk.CTk()
if os.name != "posix":
    root.iconbitmap("interface/icon/Icon_Painel_Purple_ICO.ico")
root.title("Configurar")
root.geometry(center_window_to_display(root, 790, 700, root._get_window_scaling()))


def connect_db(new_window):
    with DBConnectionHandler() as db_con:
        engine = db_con.get_engine()
        res = pd.read_sql_query("select * from information_schema.tables", con=engine)

        image_path = os.getcwd()
        image_path = os.path.join(image_path, "interface/icon/success.png")

        my_image = ctk.CTkImage(
            light_image=Image.open(image_path),
            dark_image=Image.open(image_path),
            size=(30, 30),
        )
        image_label = ctk.CTkLabel(
            master=new_window, text="", font=("arial bold", 20), image=my_image
        )
        image_label.pack(pady=10)

        label = ctk.CTkLabel(
            master=new_window,
            text="Conexão realizada com sucesso!",
            font=("arial bold", 20),
        )
        label.pack(pady=12, padx=10)


def connect_db_with_params(
    new_window, db_user, db_password, db_host, db_port, db_database
):
    with DBConnectionHandler(
        db_user, db_password, db_host, db_port, db_database
    ) as db_con:
        engine = db_con.get_engine()
        res = pd.read_sql_query("select * from information_schema.tables", con=engine)
        # print("CONECTOU", res.shape)

        image_path = os.getcwd()
        image_path = os.path.join(image_path, "interface/icon/success.png")

        my_image = ctk.CTkImage(
            light_image=Image.open(image_path),
            dark_image=Image.open(image_path),
            size=(30, 30),
        )
        image_label = ctk.CTkLabel(
            master=new_window, text="", font=("arial bold", 20), image=my_image
        )
        image_label.pack(pady=10)

        label = ctk.CTkLabel(
            master=new_window,
            text="Conexão realizada com sucesso!",
            font=("arial bold", 20),
        )
        label.pack(pady=12, padx=10)


def connection_error_db(new_window):
    # print("ERRO DE CONEXÃO")
    image_path = os.getcwd()
    image_path = os.path.join(image_path, "interface/icon/error.png")

    my_image = ctk.CTkImage(
        light_image=Image.open(image_path),
        dark_image=Image.open(image_path),
        size=(30, 30),
    )
    image_label = ctk.CTkLabel(
        master=new_window, text="", font=("arial bold", 20), image=my_image
    )
    image_label.pack(pady=10)

    error_label = ctk.CTkLabel(
        master=new_window,
        text="Erro ao conectar ao banco de dados. Por favor, realize o procedimento de configuração novamente ou entre em contato com o suporte!",
        font=("arial bold", 15),
        width=350,
        height=25,
        corner_radius=5,
        anchor="center",
        wraplength=350,
    )
    error_label.pack(pady=10, padx=10)


def topLevelViewConeectionFunction(
    frame,
    db_user,
    db_password,
    db_host,
    db_port,
    db_database,
):
    new_window = ctk.CTkToplevel(frame)
    new_window.title("Testando conexão")
    new_window.geometry(
        center_window_to_display(new_window, 400, 200, new_window._get_window_scaling())
    )
    # new_window.geometry("400x200")
    new_window.wait_visibility()
    new_window.grab_set()

    def close():
        new_window.destroy()
        new_window.update()

    try:
        if db_user and db_password and db_host and db_port and db_database:
            # print(
            # db_user, " ", db_password, " ", db_host, " ", db_port, " ", db_database
            # )
            new_window.after(
                1,
                connect_db_with_params(
                    new_window, db_user, db_password, db_host, db_port, db_database
                ),
            )
        else:
            new_window.after(1, connect_db(new_window))
    except Exception as error:
        logging.exception(error)
        new_window.after(1, connection_error_db(new_window))

    close_button = ctk.CTkButton(master=new_window, text="Fechar", command=close)
    close_button.pack(pady=12, padx=10)


def startTopLevelViewConnection(
    frame, db_user, db_password, db_host, db_port, db_database
):
    frame.after(
        1000,
        topLevelViewConeectionFunction(
            frame, db_user, db_password, db_host, db_port, db_database
        ),
    )


def exists_env(root):
    frame = ctk.CTkFrame(master=root, height=800, width=600)
    frame.pack(fill="both", expand=True)

    label = ctk.CTkLabel(master=frame, text="Painel Esus", font=("arial bold", 50))
    label.pack(pady=12, padx=10)

    image_path = os.getcwd()
    image_path = os.path.join(image_path, "interface/icon/env.png")

    my_image = ctk.CTkImage(
        light_image=Image.open(image_path),
        dark_image=Image.open(image_path),
        size=(100, 100),
    )
    image_label = ctk.CTkLabel(
        master=frame, text="", font=("arial bold", 20), image=my_image
    )
    image_label.pack(pady=10)

    exist_file_label = ctk.CTkLabel(
        master=frame,
        text="Arquivo de configuração já existente!",
        font=("arial bold", 15),
        width=600,
        height=25,
        corner_radius=5,
        anchor="center",
        wraplength=600,
    )
    exist_file_label.pack(pady=10, padx=10)

    choose_option = ctk.CTkLabel(
        master=frame,
        text="Você pode testar novamente a conexão com o banco de dados ou criar uma nova configuração do Painel-Esus. Escolha a opção abaixo:",
        font=("arial bold", 15),
        width=600,
        height=25,
        corner_radius=5,
        anchor="center",
        wraplength=600,
    )
    choose_option.pack(pady=10, padx=10)

    loading_label = ctk.CTkLabel(master=frame, text="", font=("Arial", 14))
    loading_label.pack()

    test_connection_button = ctk.CTkButton(
        master=frame,
        text="Testar conexão",
        command=lambda: testar_conexao_com_loading(
            frame,
            None, None, None, None, None,
            test_connection_button,
            loading_label,
        ),
    )
    # test_connection_button = ctk.CTkButton(
    #     master=frame,
    #     text="Testar conexão2",
    #     command=lambda: startTopLevelViewConnection(
    #         frame, None, None, None, None, None
    #     ),
    # )
    test_connection_button.pack(pady=12, padx=10)

    def close():
        frame.destroy()
        frame.update()
        tabs()

    create_new_env_button = ctk.CTkButton(
        master=frame, text="Configurar novamente", command=close
    )
    create_new_env_button.pack(pady=12, padx=10)


def build_env_str(env):
    if env != None:
        str_value = str(env)
        new_str = str_value.replace("\n", "")
        # new_str = str_value.replace("'","")
        return new_str
    return env


def create_env(
    input_host,
    input_database,
    input_user,
    input_password,
    input_port,
    input_cidade,
    input_user_admin,
    input_password_admin,
    input_bridge_login_url,
):
    with open(".env", "w", encoding="utf-8") as f:
        lines = [
            "DB_HOST='" + build_env_str(input_host.get()) + "'\n",
            "DB_DATABASE='" + build_env_str(input_database.get()) + "'\n",
            "DB_USER='" + build_env_str(input_user.get()) + "'\n",
            "DB_PASSWORD='" + build_env_str(input_password.get()) + "'\n",
            "DB_PORT='" + build_env_str(input_port.get()) + "'\n",
            "CIDADE_IBGE='" + build_env_str(input_cidade.get()) + "'\n",
            "ADMIN_USERNAME='" + build_env_str(input_user_admin.get()) + "'\n",
            "ADMIN_PASSWORD='" + build_env_str(input_password_admin.get()) + "'\n",
            "PASSWORD_SALT='" + "painel" + "'\n",
            "BRIDGE_LOGIN_URL='" + build_env_str(input_bridge_login_url.get()) + "'\n",
            "RELOAD_BASE_SCHEDULE='4:00'" + "\n",
            "ARTEFACT=" + "web" + "\n",
            "ENV=" + "instalador" + "\n",
            "SECRET_TOKEN=" + "111111111111111111111" + "\n",
            "GENERATE_BASE=True\n",
            "CHUNK_SIZE=50000\n",
            "POLARS_SKIP_CPU_CHECK=True\n",
            "LOG_API=https://painel-logs.painelsaude.info\n",
            "APPLICATION_VERSION=0.9.3",
            "LAZY_ON=0",
        ]
        f.writelines(lines)
        f.close()


class Field:
    def __init__(self, field):
        self.field = field
        self.index = 0
        self.value = ""

    def get_field_index(self):
        choices = {
            "DB_HOST": 0,
            "DB_DATABASE": 1,
            "DB_USER": 2,
            "DB_PASSWORD": 3,
            "DB_PORT": 4,
            "CIDADE_IBGE": 5,
            "ADMIN_USERNAME": 6,
            "ADMIN_PASSWORD": 7,
            "BRIDGE_LOGIN_URL": 8,
        }
        split = self.field.split("=")
        if len(split) > 1:
            self.index = choices.get(split[0])
            self.value = split[1]
        else:
            self.index = None
            self.value = None


def fill_input_fields(inputFieldsArray: [any]):
    if os.path.exists(".env"):
        file_content = any
        with open(".env", "r") as file:
            file_content = file.readlines()
        for input in file_content:
            field = Field(input)
            field.get_field_index()
            if field.index != None:
                env_field = field.value.replace("'", "").strip()
                if len(env_field) > 0:
                    inputFieldsArray[field.index].insert(
                        0, field.value.replace("'", "").strip()
                    )

        file.close()
    else:
        return


def success_frame():
    frame = ctk.CTkFrame(master=root, height=300, width=600)
    frame.pack(fill="both", expand=True)

    blank_label = ctk.CTkLabel(
        master=frame,
        text="",
        width=600,
        height=25,
        corner_radius=5,
        anchor="center",
        wraplength=600,
    )
    blank_label.pack(pady=10, padx=10)

    label = ctk.CTkLabel(
        master=frame,
        text="Configuração realizada com sucesso!",
        font=("arial bold", 25),
    )
    label.pack(pady=12, padx=10)

    image_path = os.getcwd()
    image_path = os.path.join(image_path, "interface/icon/success.png")

    my_image = ctk.CTkImage(
        light_image=Image.open(image_path),
        dark_image=Image.open(image_path),
        size=(100, 100),
    )
    image_label = ctk.CTkLabel(
        master=frame, text="", font=("arial bold", 20), image=my_image
    )
    image_label.pack(pady=10)

    blank_label = ctk.CTkLabel(
        master=frame,
        text="",
        width=600,
        height=25,
        corner_radius=5,
        anchor="center",
        wraplength=600,
    )
    blank_label.pack(pady=10, padx=10)

    exist_file_label = ctk.CTkLabel(
        master=frame,
        text="A configuração do Painel Esus foi realizada com sucesso. \n Para iniciar o sistema e começar a usufruir dos paineis disponibilizados, basta fechar essa janela de configuração e iniciar o executável do Painel Esus presente na mesma pasta.",
        font=("arial bold", 15),
        width=600,
        height=25,
        corner_radius=5,
        anchor="center",
        wraplength=600,
    )
    exist_file_label.pack(pady=10, padx=10)

    choose_option = ctk.CTkLabel(
        master=frame,
        text="Caso aconteça algum problema na hora da execução do Painel Esus, reinicie o processo de configuração validando os dados de aceso à base de dados.",
        font=("arial bold", 15),
        width=600,
        height=25,
        corner_radius=5,
        anchor="center",
        wraplength=600,
    )
    choose_option.pack(pady=10, padx=10)

    create_new_env_button = ctk.CTkButton(
        master=frame, text="Fechar", command=root.destroy
    )
    create_new_env_button.pack(pady=12, padx=10)

def testar_conexao_com_loading(frame, user, password, host, port, database, button, loading_label):
    def tarefa():
        try:
            # Aqui faz o teste real, dentro da thread
            with DBConnectionHandler(user, password, host, port, database) as db_con:
                engine = db_con.get_engine()
                res = pd.read_sql_query("select * from information_schema.tables", con=engine)
            # Se chegou aqui sem erro:
            resultado = "Conexão bem-sucedida!"
            cor = "green"
        except Exception as e:
            resultado = f"Erro: {str(e)}"
            cor = "red"

        # Atualiza UI na thread principal
        def atualiza_ui():
            loading_label.configure(text=resultado, text_color=cor)
            button.configure(state="normal")

        frame.after(0, atualiza_ui)

    loading_label.configure(text="Conectando...", text_color="gray")
    button.configure(state="disabled")

    threading.Thread(target=tarefa).start()


def validar_ibge_codigo(codigo, label_status):
    # Exibe mensagem de verificação imediatamente
    label_status.configure(text="Verificando...", text_color="orange")
    label_status.pack(pady=(4, 10))

    # Função interna que executa a validação real
    def executar_validacao():
        try:
            with open("ibge.json", "r", encoding="utf-8") as f:
                cidades = json.load(f)
            exists = any(str(c["IBGE"]) == codigo.zfill(5) for c in cidades)
            if exists:
                label_status.configure(text="Código IBGE válido ✅\n", text_color="#66BB6A")
            else:
                label_status.configure(text="Código IBGE inválido ❌\n", text_color="#E57373")
            label_status.pack(pady=(4, 10))
        except Exception as e:
            label_status.configure(text=f"Erro ao validar código: {e}", text_color="#E57373")
        finally:
            check_all_inputs_filled()  # Atualiza botão "Finalizar"

    # Executa a validação após 1 segundo (1000 ms)
    label_status.after(1000, executar_validacao)


def testar_conexao_com_loading(frame, user, password, host, port, database, button, loading_label):
    def tarefa():
        try:
            # Aqui faz o teste real, dentro da thread
            with DBConnectionHandler(user, password, host, port, database) as db_con:
                engine = db_con.get_engine()
                res = pd.read_sql_query("select * from information_schema.tables", con=engine)
            # Se chegou aqui sem erro:
            resultado = "Conexão bem-sucedida!"
            cor = "#66BB6A"
        except Exception as e:
            resultado = f"Erro: {str(e)}"
            cor = "#E57373"

        # Atualiza UI na thread principal
        def atualiza_ui():
            loading_label.configure(text=resultado, text_color=cor)
            button.configure(state="normal")

        frame.after(0, atualiza_ui)

    loading_label.configure(text="Conectando...", text_color="orange")
    button.configure(state="disabled")

    threading.Thread(target=tarefa).start()

def create_labeled_input(parent, row, label_text, placeholder, is_password=False):
    label = ctk.CTkLabel(parent, text=label_text, font=("Arial", 14))
    label.grid(row=row, column=0, sticky="w", pady=(0, 2))

    entry = ctk.CTkEntry(
        parent,
        placeholder_text=placeholder,
        show="*" if is_password else "",
        width=600,
        height=25,
        corner_radius=10,
    )
    entry.grid(row=row + 1, column=0, pady=(0, 10))

    return entry  # retorna o CTkEntry para uso posterior

def is_filled(entry):
    return entry.get().strip() != ""

def check_db_inputs_filled(*args):
    all_filled = all([
        is_filled(input_host),
        is_filled(input_database),
        is_filled(input_user),
        is_filled(input_password),
        is_filled(input_port),
    ])
    test_connection_button.configure(state="normal" if all_filled else "disabled")
    check_all_inputs_filled()

def check_all_inputs_filled(*args):
    all_filled = all([
        is_filled(input_host),
        is_filled(input_database),
        is_filled(input_user),
        is_filled(input_password),
        is_filled(input_port),
        is_filled(input_cidade),
        is_filled(input_user_admin),
        is_filled(input_password_admin),
        is_filled(input_bridge_login_url),
    ])

    is_ibge_valid = validate_status_label.cget("text") == "Código IBGE válido ✅\n"
    create_new_env_button.configure(state="normal" if all_filled and is_ibge_valid else "disabled")

def excecute_validators(validate_button, test_connection_button):
    if input_cidade.get():
        validar_ibge_codigo(input_cidade.get(), validate_status_label)
        validate_button.configure(state="normal")

    if input_user.get() and input_password.get() and input_host.get() and input_port.get() and input_database.get():
        test_connection_button.configure(state="normal")


def tabs():
    global input_host, input_database, input_user, input_password, input_port
    global input_cidade, input_user_admin, input_password_admin, input_bridge_login_url
    global test_connection_button, create_new_env_button, validate_status_label

    tabview = ctk.CTkTabview(root, width=780, height=580)
    tabview.pack()
    tabview.add("Banco de dados")
    tabview.add("Painel e-SUS")
    # tabview.add("Responsável")

    tabview.tab("Banco de dados").grid_columnconfigure(0, weight=1)
    tabview.tab("Painel e-SUS").grid_columnconfigure(0, weight=1)
    # tabview.tab("Responsável").grid_columnconfigure(0, weight=1)

    # --------------------------------CONFIGURAÇÃO BANCO DE DADOS--------------------------------
    frame = ctk.CTkFrame(tabview.tab("Banco de dados"), height=780, width=580)
    frame.pack(fill="both", expand=True)

    label = ctk.CTkLabel(
        master=frame, text="Configuração do Banco de dados", font=("arial bold", 25)
    )
    label.pack(pady=12, padx=10)

    label_info = ctk.CTkLabel(
        master=frame,
        text="Por favor, siga todos os passos das abas apresentadas para configurar o Painel e-SUS APS. \n Preencha todos os campos abaixo solicitados para a configuração da base de dados do município.",
        font=("arial bold", 15),
    )
    label_info.pack(pady=12, padx=10)

    image_path = os.getcwd()
    image_path = os.path.join(image_path, "interface/icon/database.png")
    my_image = ctk.CTkImage(
        light_image=Image.open(image_path),
        dark_image=Image.open(image_path),
        size=(80, 80),
    )
    image_label = ctk.CTkLabel(
        master=frame, text="", font=("arial bold", 20), image=my_image
    )
    image_label.pack(pady=10)


    # FORM INPUTS
    form_frame = ctk.CTkFrame(master=frame, fg_color="transparent")
    form_frame.pack(pady=10, padx=10)

    input_host = create_labeled_input(form_frame, 0, "Endereço do banco de dados", "Host:")
    input_database = create_labeled_input(form_frame, 2, "Nome da base de dados", "Base de dados:")
    input_user = create_labeled_input(form_frame, 4, "Usuário do banco de dados", "Usuário:")
    input_password = create_labeled_input(form_frame, 6, "Senha do banco de dados", "Senha:", is_password=True)
    input_port = create_labeled_input(form_frame, 8, "Porta do banco de dados", "Porta:")


    loading_label = ctk.CTkLabel(master=frame, text="", font=("Arial", 14))
    loading_label.pack()

    test_connection_button = ctk.CTkButton(
        master=frame,
        text="Testar conexão",
        command=lambda: testar_conexao_com_loading(
            frame,
            input_user.get().strip(),
            input_password.get().strip(),
            input_host.get().strip(),
            input_port.get().strip(),
            input_database.get().strip(),
            test_connection_button,
            loading_label,
        ),
    )
    test_connection_button.pack(pady=12, padx=10)

    # --------------------------------CONFIGURAÇÃO PAINEL--------------------------------
    frame_painel = ctk.CTkFrame(tabview.tab("Painel e-SUS"), height=780, width=580)
    frame_painel.pack(fill="both", expand=True)

    image_path_painel = os.getcwd()
    image_path_painel = os.path.join(image_path_painel, "interface/icon/painel.png")
    painel_image = ctk.CTkImage(
        light_image=Image.open(image_path_painel),
        dark_image=Image.open(image_path_painel),
        size=(130, 100),
    )

    label_config_painel = ctk.CTkLabel(
        master=frame_painel, text="Configuração do Painel e-SUS APS:", font=("arial bold", 25)
    )
    label_config_painel.pack(pady=12, padx=10)

    label_info_painel = ctk.CTkLabel(
        master=frame_painel,
        text="Preencha todos os campos solicitados para a configuração dos dados de acesso ao Painel e-SUS APS. \n Os campos 'Usuário' e 'Senha' aqui configurados serão utilizados para fazer login na plataforma.",
        font=("arial bold", 15),
    )
    label_info_painel.pack(pady=12, padx=10)

    image_label_painel = ctk.CTkLabel(
        master=frame_painel, text="", font=("arial bold", 20), image=painel_image
    )
    image_label_painel.pack(pady=10)

    # Container para o input e botão lado a lado
    # Container para o input e botão lado a lado
    cod_ibge_container = ctk.CTkFrame(master=frame_painel, fg_color="transparent")
    cod_ibge_container.pack(pady=10)

    # ✅ Adiciona o título "Código IBGE" acima do input
    ibge_label = ctk.CTkLabel(
        master=cod_ibge_container,
        text="Código IBGE",
        font=("Arial", 14),
        anchor="w",  # Alinha à esquerda
        justify="left"
    )
    ibge_label.pack(anchor="w", padx=(0, 0), pady=(0, 4))  # Alinhamento e espaçamento inferior

    # Input para o código da cidade
    input_cidade = ctk.CTkEntry(
        master=cod_ibge_container,
        placeholder_text="Código IBGE da Cidade:",
        width=400,
        height=25,
        corner_radius=10,
    )
    input_cidade.pack(side="left", padx=(0, 10))

    # Ação para ativar/desativar botão
    def on_cidade_change(*args):
        if input_cidade.get().strip():
            validate_button.configure(state="normal")
        else:
            validate_button.configure(state="disabled")

    input_cidade.bind("<KeyRelease>", lambda event: on_cidade_change())

    # Botão de validação
    validate_button = ctk.CTkButton(
        master=cod_ibge_container,
        text="Validar",
        state="disabled",
        command=lambda: validar_ibge_codigo(input_cidade.get(), validate_status_label),
    )
    validate_button.pack(side="left")

    # Label de status da validação
    validate_status_label = ctk.CTkLabel(
        master=frame_painel,
        text="",
        font=("Arial", 14),
        text_color="gray",
        height=30
    )
    validate_status_label.pack(pady=(4, 10))
    

    form_frame_painel = ctk.CTkFrame(master=frame_painel, fg_color="transparent")
    form_frame_painel.pack(pady=10, padx=10)

    input_user_admin = create_labeled_input(
        form_frame_painel, 2, "Usuário de acesso ao Painel", "Usuário do painel:"
    )

    input_password_admin = create_labeled_input(
        form_frame_painel, 4, "Senha de acesso ao Painel", "Senha do painel:", is_password=True
    )

    input_bridge_login_url = create_labeled_input(
        form_frame_painel, 6, "URL do PEC e-SUS APS", "Url de login:"
    )


    fill_input_fields(
        [
            input_host,
            input_database,
            input_user,
            input_password,
            input_port,
            input_cidade,
            input_user_admin,
            input_password_admin,
            input_bridge_login_url,
        ]
    )


    def close():
        create_env(
            input_host,
            input_database,
            input_user,
            input_password,
            input_port,
            input_cidade,
            input_user_admin,
            input_password_admin,
            input_bridge_login_url,
        )
        tabview.destroy()
        tabview.update()
        frame_painel.destroy()
        frame_painel.update()
        success_frame()


    create_new_env_button = ctk.CTkButton(
        master=frame_painel, text="Finalizar configuração", command=close
    )
    create_new_env_button.pack(pady=12, padx=10)

    test_connection_button.configure(state="disabled")
    create_new_env_button.configure(state="disabled")
    excecute_validators(validate_button, test_connection_button)

    for input_field in [input_host, input_database, input_user, input_password, input_port]:
        input_field.bind("<KeyRelease>", check_db_inputs_filled)

    for input_field in [input_cidade, input_user_admin, input_password_admin, input_bridge_login_url]:
        input_field.bind("<KeyRelease>", check_all_inputs_filled)


def start_interface():
    if os.path.exists(".env"):
        exists_env(root)
    else:
        tabs()

    root.mainloop()


