medicos_codigos = [476, 484, *range(636, 698 + 1), *range(785, 788 + 1)]

enfermeiros_codigos = [475, 479, 487, *range(627, 635 + 1), *range(782, 784 + 1)]

acs_cod = [488]

tacs_cod = [780]

acs_tacs = [488, 780]


cirurgioes_dentistas_codigos = [
    485,
    599,
    *range(699, 720),
]  # Códigos de cirurgioes dentistas cbo inicio "2232"

tec_aux_enfermagem_codigos = [483, *range(522, 524 + 1), 620, 621, *range(623, 625 + 1)]

farmaceuticos_codigos = [*range(721, 726 + 1)]

fisioterapeutas_codigos = [482, *range(727, 731 + 1), *range(796, 798 + 1)]

educacao_fisica_codigos = [738, 776]

nutricionistas_codigos = [481]

fonoaudiologos_codigos = [480, *range(732, 734 + 1), *range(799, 802 + 1)]

terapeutas_codigos = [749, 804]

assistentes_sociais_codigos = [477]

psicologos_codigos = [478, 499, 545, 736, *range(740, 746 + 1)]

tsbucal_cod = [564, 610, 614, 615, 616]  # Código Técnico em saúde bucal "3224"


tec_aux_enfermagem_codigos = [483, *range(522, 524 + 1), 620, 621, *range(623, 625 + 1)]


# exame colesterol
ex_cbo_colesterol = (
    medicos_codigos
    + enfermeiros_codigos
    + nutricionistas_codigos
    + farmaceuticos_codigos
    + cirurgioes_dentistas_codigos
)


##plot de exames dashboard
todos_codigos = (
    medicos_codigos
    + cirurgioes_dentistas_codigos
    + farmaceuticos_codigos
    + fisioterapeutas_codigos
    + nutricionistas_codigos
    + fonoaudiologos_codigos
    + terapeutas_codigos
    + educacao_fisica_codigos
    + psicologos_codigos
    + assistentes_sociais_codigos
    + enfermeiros_codigos
)

# cbo aferiacao pa
cbo_afericao_pa = (
    enfermeiros_codigos
    + medicos_codigos
    + cirurgioes_dentistas_codigos
    + fisioterapeutas_codigos
    + educacao_fisica_codigos
    + farmaceuticos_codigos
    + terapeutas_codigos
    + nutricionistas_codigos
    + tec_aux_enfermagem_codigos
    + acs_tacs
)


creatina_cbo = (
    medicos_codigos
    + enfermeiros_codigos
    + nutricionistas_codigos
    + farmaceuticos_codigos
)


# CBOs glicemia

glicemia_cbo = (
    enfermeiros_codigos
    + medicos_codigos
    + farmaceuticos_codigos
    + cirurgioes_dentistas_codigos
    + nutricionistas_codigos
)

# CBOs exame dos pés


pe_cbo = (
    enfermeiros_codigos + medicos_codigos + fisioterapeutas_codigos + terapeutas_codigos
)

# CBOs peso e altura

peso_altura_cbo = (
    enfermeiros_codigos
    + tacs_cod
    + acs_cod
    + medicos_codigos
    + cirurgioes_dentistas_codigos
    + farmaceuticos_codigos
    + fisioterapeutas_codigos
    + educacao_fisica_codigos
    + terapeutas_codigos
    + nutricionistas_codigos
    + fonoaudiologos_codigos
    + tsbucal_cod
)


# códigos sigtap ou código relativos a procedimentos

afericao_pa_codigos = "0301100039"


glicemia_codigos = ["0214010015"]

creatinina_codigos = ["0202010317", "ABEX003"]

colesterol_codigos = ["0202010295"]

hemograma_codigos = ["0202020380"]

eletrocardiograma_codigos = ["0211020036"]

eas_equ_codigos = ["0202050017", "ABEX027"]

afericao_pa = ["0301100039"]

# hipertensao
sodio_codigos = ["0202010635"]

potassio_codigos = ["0202010600"]


# diabetes?

colesterol_total = ["0202010295"]

colesterol_hdl = ["0202010279"]

colesterol_ldl = ["0202010287"]


hemoglobina_codigos = ["0202010503", " ABEX008"]


pe_diabetico_codigos = ["0301040095"]

retinografia_codigos = ["0211060178", "ABEX03"]


peso_altura_codigos = "0101040024"


# diabetes codigos cids / ciaps / abp

cid_codes_diabetes = [
    "E10",
    "E100",
    "E101",
    "E102",
    "E103",
    "E104",
    "E105",
    "E106",
    "E107",
    "E108",
    "E109",
    "E11",
    "E110",
    "E111",
    "E112",
    "E113",
    "E114",
    "E115",
    "E116",
    "E117",
    "E118",
    "E119",
    "E14",
    "E140",
    "E141",
    "E142",
    "E143",
    "E144",
    "E145",
    "E146",
    "E147",
    "E148",
    "E149",
]


ciap_codes_diabetes = ["T89", "T90"]

abp_codes_diabetes = ["ABP006"]


# agravos dashboard diabetes e hipertensao

agravos_dict = {
    "isContained_Infarto_Agudo": [
        "I21",
        "I210",
        "I211",
        "I212",
        "I213",
        "I214",
        "I219",
    ],
    "isContained_Acidente_Vascular": ["I64"],
    "isContained_Doença_Coronariana": [
        "I24",
        "I248",
        "I249",
        "I25",
        "I251",
        "I258",
        "I259",
        "I518",
        "I519",
        "I110",
        "I119",
        "I130",
        "I132",
        "I50",
        "I500",
        "I509",
    ],
    "isContained_Doença_Cerebrovascular": [
        "G46",
        "G468",
        "I67",
        "I678",
        "I679",
        "I68",
        "I688",
        "I69",
    ],  #'I699' removido wanessa indicou que não existe , alterado em 20/01/2025
}


isContained_Doença_renal_ciap = ["U14", "U99", "U88", "U90"]
isContained_Doença_renal_cid = [
    "I12",
    "I129",
    "I13",
    "I130",
    "I131",
    "I132",
    "I139",
    "N083",
    "N179",
    "N18",
    "N180",
    "N188",
    "N189",
    "N19",
]


# códigos para definir hipertensão

# códigos para definir diabetes
