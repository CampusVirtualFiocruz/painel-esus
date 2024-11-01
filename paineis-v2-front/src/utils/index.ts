export function formataNumero(numero: number | undefined) {
  if (numero) {
    return numero.toLocaleString("pt-BR");
  }

  return "-";
}

export function formataPorcentagemIbge(
  ibge: number | undefined,
  populacaoCadastrada: number | undefined
) {
  if (ibge && populacaoCadastrada) {
    //let totalIbge = (populacaoCadastrada / ibge) * 100;
    //let totalIbge = (ibge / populacaoCadastrada) * 100;
    let variacaoPercentual =
      ((populacaoCadastrada - ibge) / populacaoCadastrada) * 100;

    return variacaoPercentual.toFixed(0) + "%";
  }

  return "-";
}

export function somaIndicador(indicador: any) {
  let result = 0;

  if (indicador) {
    result =
      indicador.rural + indicador.urbano + (indicador.nao_informado || 0);
  }

  return formataNumero(result);
}

export function porcentagemIndicador(indicador: any) {
  let total = 0;

  if (indicador) {
    total = indicador.rural + indicador.urbano;

    //let porcentagemRural = indicador.rural / total * 100;
    //let porcentagemUrbano = indicador.urbano / total * 100;
  }

  return formataNumero(total);
}

export function getFirstName(fullName: string | undefined) {
  if (!fullName) return "-";

  const [first] = fullName.toLocaleLowerCase().split(" ");
  const name = first.charAt(0).toUpperCase() + first.slice(1);
  return name;
}

export function formataNome(nome: string | undefined) {
  if (!nome) return "-";
  let nomeTratado = nome
    .toLowerCase()
    .replace(/(?:^|\s)\S/g, function (capitalize) {
      return capitalize.toUpperCase();
    });

  let PreposM = ["Da", "Do", "Das", "Dos", "A", "E"];
  let prepos = ["da", "do", "das", "dos", "a", "e"];

  for (var i = PreposM.length - 1; i >= 0; i--) {
    nomeTratado = nomeTratado.replace(
      RegExp(
        "\\b" + PreposM[i].replace(/[-\\^$*+?.()|[\]{}]/g, "\\$&") + "\\b",
        "g"
      ),
      prepos[i]
    );
  }

  return nomeTratado;
}

export function getPorcentagemIndicador(
  name: string,
  total: number,
  value: any
) {
  let porcentagem = 0;

  if (total && value) {
    porcentagem = (value / total) * 100;
    return porcentagem.toFixed(0) + "%";
  }

  return porcentagem + "%";
}

export function formatAsPercent(value: string) {
  return `${parseFloat(value).toFixed(1)}%`;
}

type Ubs = {
  label: string;
  value: string;
};

export function getNomeUbs(data: any, id: string) {
  let ubs = Object.values(data).find(
    (item: any) => parseInt(item.value) === parseInt(id)
  ) as Ubs;
  console.log(ubs);
  return ubs ? ubs.label : "-";
}

export function prepareExamsTable(data: any) {
  let retorno = Object.entries(data).map((item: any) => {
    return {
      tipo: getNameExam(item[0]),
      avaliados: item[1].avaliados,
      solicitados: item[1].solicitados,
    };
  });

  return retorno;
}

export function showValuePerTrimester(data: any, trimestre: string) {
  let total: unknown = 0;

  switch (trimestre) {
    case "primeiro":
      total = Object.values(data)[0];
      break;
    case "segundo":
      total = Object.values(data)[1];
      break;
    case "terceiro":
      total = Object.values(data)[2];
      break;
    default:
      total = 0;
  }

  return `${total}`;
}

export function showValuePerWeeks(data: any, week: string) {
  let total: unknown = 0;

  switch (week) {
    case "1 a 12 semanas":
      total = Object.values(data)[0];
      break;
    case "13 a 16 semanas":
      total = Object.values(data)[1];
      break;
    case "17 a 20 semanas":
      total = Object.values(data)[2];
      break;
    case "21 a 24 semanas":
      total = Object.values(data)[3];
      break;
    case "25 a 28 semanas":
      total = Object.values(data)[4];
      break;
    case "29 a 32 semanas":
      total = Object.values(data)[5];
      break;
    case "33 a 36 semanas":
      total = Object.values(data)[6];
      break;
    case "37 a 41 semanas":
      total = Object.values(data)[7];
      break;
    default:
      total = 0;
  }

  return `${total}`;
}

function getNameExam(value: any) {
  let exam = "";

  switch (value) {
    case "glicemia":
      exam = "Glicemia jejum";
      break;
    case "hemograma":
      exam = "Hemograma";
      break;
    case "hiv":
      exam = "Teste rápido Anti-HIV";
      break;
    case "taxa_igm_igg":
      exam = "Taxa IgM e IgG";
      break;
    case "teste_rapido_sifilis":
      exam = "Teste rápido sífilis";
      break;
    case "tipo_sanguineo":
      exam = "Tipo sanguíneo/Rh";
      break;
    case "urina":
      exam = "Urina";
      break;
    case "urocultura":
      exam = "Urocultura";
      break;
    case "us_obstetrica":
      exam = "US Obstétrica";
      break;
    default:
      exam = "Nenhum encontrado";
  }

  return exam;
}

export const cpfMask = (value: string | undefined) => {
  if (value) {
    return value
      .replace(/\D/g, "")
      .replace(/(\d{3})(\d)/, "$1.$2")
      .replace(/(\d{3})(\d)/, "$1.$2")
      .replace(/(\d{3})(\d{1,2})/, "$1-$2")
      .replace(/(-\d{2})\d+?$/, "$1");
  }

  return "NÃO CADASTRADO";
};

export const capitalize = (s: string, lower = false) =>
  (lower ? s.toLowerCase() : s).replace(/(?:^|\s|["'([{])+\S/g, (match) =>
    match.toUpperCase()
  );

export const profiles = [
  "CBO 322415: Auxiliar de saúde bucal",
  "CBO 411010: Assistente administrativo",
];
