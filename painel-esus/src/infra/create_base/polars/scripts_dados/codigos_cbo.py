acs_cod = ["515105"]

assistentes_sociais_codigos = ["251605"]

cirurgioes_dentistas_codigos = [
    "223293",
    "223208",
    "223204",
    "223280",
    "223284",
    "223212",
    "223216",
    "223220",
    "223224",
    "223228",
    "223276",
    "223288",
    "223232",
    "223236",
    "223240",
    "223244",
    "223248",
    "223252",
    "223256",
    "223260",
    "223264",
    "223268",
    "223272",
]

enfermeiros_codigos = [
    "223565",
    "223560",
    "223505",
    "223520",
    "223525",
    "223530",
    "223535",
    "223540",
    "223545",
    "223550",
    "223555",
    "223510",
    "223515",
    "223580",
    "2235C3",
]

farmaceuticos_codigos = ["223405", "223415", "223425", "223410", "223445", "223430"]

fisioterapeutas_codigos = [
    "223605",
    "223650",
    "223660",
    "223655",
    "223635",
    "223630",
    "223640",
    "223645",
    "223625",
]

fonoaudiologos_codigos = [
    "223810",
    "223840",
    "223815",
    "223830",
    "223820",
    "223825",
    "223835",
    "223845",
]

medicos_codigos = [
    "225142",
    "225285",
    "225105",
    "225110",
    "225148",
    "225151",
    "225115",
    "225290",
    "225122",
    "225120",
    "225210",
    "225295",
    "225215",
    "225220",
    "225225",
    "225230",
    "225235",
    "225240",
    "225305",
    "225125",
    "225280",
    "225130",
    "225135",
    "225140",
    "225203",
    "225310",
    "225145",
    "225150",
    "225315",
    "225320",
    "225155",
    "225160",
    "225165",
    "225170",
    "225175",
    "225180",
    "225250",
    "225185",
    "225340",
    "225345",
    "225195",
    "225103",
    "225106",
    "225255",
    "225109",
    "225260",
    "225350",
    "225112",
    "225118",
    "225265",
    "225121",
    "225270",
    "225275",
    "225325",
    "225335",
    "225124",
    "225127",
    "225133",
    "225330",
    "2231F9",
    "2231A2",
    "2231F8",
    "225136",
    "225139",
    "225154",
    "2231A1",
    "2231G1",
    "223150",
    "225355",
]

medicos_veterinarios = ["223305"]

nutricionistas_codigos = ["223710"]

educacao_fisica_codigos = ["2241E1", "224140"]

psicologos_codigos = [
    "251510",
    "251530",
    "251505",
    "251545",
    "251550",
    "251555",
    "251515",
    "251540",
    "251535",
    "251520",
    "251525",
]

tacs_cod = ["322255"]


tec_aux_enfermagem_codigos = [
    "322245",
    "322205",
    "322230",
    "322250",
    "322235",
    "322240",
    "322210",
    "322215",
    "322220",
]

tsbucal_cod = ["322415", "322425", "322405", "322430"]

terapeutas_codigos = ["223905"]

acs_tacs = acs_cod + tacs_cod


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

# CBOs glicemia

hemoglo_cbo = (
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
    + tec_aux_enfermagem_codigos
)


# códigos sigtap ou código relativos a procedimentos

afericao_pa_codigos = "0301100039"


glicemia_codigos = ["0214010015"]

creatinina_codigos = ["0202010317", "ABEX003"]

colesterol_codigos = ["0202010295"]

hemograma_codigos = ["0202020380", "ABEX028"]

eletrocardiograma_codigos = ["0211020036", "ABEX004"]

eas_equ_codigos = ["0202050017", "ABEX027"]

afericao_pa = ["0301100039"]

# hipertensao
sodio_codigos = ["0202010635"]

potassio_codigos = ["0202010600"]


# diabetes?

colesterol_total = ["0202010295", "ABEX002"]

colesterol_hdl = ["0202010279", "ABEX007"]

colesterol_ldl = ["0202010287", "ABEX009"]


hemoglobina_codigos = ["0202010503", "ABEX008"]


pe_diabetico_codigos = ["0301040095", "ABEPG011"]

retinografia_codigos = ["0211060178", "ABEX013"]


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
