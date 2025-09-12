export type TResponse = {
  ano: number;
  classe: string;
  count: number;
  nu_cnes: string;
  mes: number;
  time: string;
};
const mapProps: { [key: string]: string } = {
  'Febre Exantemática': 'totalFebreExantematicas',
  'Febre Inespecífica': 'totalFebreInespecificas',
  'Infecção Intestinal': 'totalInfeccoesIntestinais',
  'Infecção Respiratória': 'totalInfeccoesRespiratorias',
  'Outros Atendimentos': 'totalAtendimentosPorOutrosCasos',
};

export const parseChartData = (response: TResponse[]) => {
  const result: { [key: string]: number } = {
    totalInfeccoesRespiratorias: 0,
    totalInfeccoesIntestinais: 0,
    totalFebreExantematicas: 0,
    totalFebreInespecificas: 0,
    totalAtendimentosPorSindromesAgudas: 0,
    totalAtendimentosPorOutrosCasos: 0,
  };

  response.forEach((item: TResponse) => {
    const key = mapProps[item.classe];
    result[key] += item.count;
  });
  result.totalAtendimentosPorSindromesAgudas =
    result.totalInfeccoesRespiratorias +
    result.totalInfeccoesIntestinais +
    result.totalFebreExantematicas +
    result.totalFebreInespecificas;
  return result;
};

type AccuteStackMap = {
  [key: string]: {
    [key: string]: number;
    totalFebreExantematicas: number;
    totalFebreInespecificas: number;
    totalInfeccoesIntestinais: number;
    totalInfeccoesRespiratorias: number;
    totalAtendimentosPorOutrosCasos: number;
  };
};

class StackAccuteChartItem {
  name = '';
  label = '';
  color = '';
  data: number[] = [];
  constructor() {}
  [require('util').inspect.custom]() {
    return `\tName: ${this.name}\n
        \tdata: ${this.data}\n`;
  }
}
class FebreExantematica extends StackAccuteChartItem {
  constructor(data: [number]) {
    super();
    this.name = 'Febre Exantemática';
    this.label = 'febre_exantematica';
    this.color = '#2675b0';
    this.data = data;
  }
}
class FebreInespecifica extends StackAccuteChartItem {
  constructor(data: [number]) {
    super();
    this.name = 'Febre Inespecífica';
    this.label = 'febre_inespecifica';
    this.color = '#094069';
    this.data = data;
  }
}
class InfeccaoIntestinal extends StackAccuteChartItem {
  constructor(data: [number]) {
    super();
    this.name = 'Infecção Intestinal';
    this.label = 'infeccao_intestinal';
    this.color = '#3996c1';
    this.data = data;
  }
}
class InfeccaoRespiratoria extends StackAccuteChartItem {
  constructor(data: [number]) {
    super();
    this.name = 'Infecção Respiratoria';
    this.label = 'infeccao_respiratorio';
    this.color = '#5dd2c9';
    this.data = data;
  }
}
class OutrosAtendimentos extends StackAccuteChartItem {
  constructor(data: [number]) {
    super();
    this.name = 'Outros Atendimentos';
    this.label = 'outros_atendimentos';
    this.color = '#';
    this.data = data;
  }
}

class AtendimentosAgudos extends StackAccuteChartItem {
  constructor(data: [number]) {
    super();
    this.name = 'Atendimentos por síndromes agudas';
    this.label = 'atendimentos_por_sindromes_agudas';
    this.color = '#';
    this.data = data;
  }
}

export const filterStackAccuteCare = (response: TResponse[]) => {
  const dateMap: AccuteStackMap = {};
  response.forEach((item: TResponse) => {
    const key = mapProps[item.classe];
    if (dateMap.hasOwnProperty(item.time)) {
      dateMap[item.time][key] = item.count;
    } else {
      dateMap[item.time] = {
        totalFebreExantematicas: 0,
        totalFebreInespecificas: 0,
        totalInfeccoesIntestinais: 0,
        totalInfeccoesRespiratorias: 0,
        totalAtendimentosPorOutrosCasos: 0,
      };
      dateMap[item.time][key] = item.count;
    }
  });
  const result = {
    labels: Object.keys(dateMap),
    stack: [
      new FebreExantematica(
        Object.values(dateMap).map(
          (item: any) => item.totalFebreExantematicas
        ) as [number]
      ),
      new FebreInespecifica(
        Object.values(dateMap).map(
          (item: any) => item.totalFebreInespecificas
        ) as [number]
      ),
      new InfeccaoRespiratoria(
        Object.values(dateMap).map(
          (item: any) => item.totalInfeccoesRespiratorias
        ) as [number]
      ),
      new InfeccaoIntestinal(
        Object.values(dateMap).map(
          (item: any) => item.totalInfeccoesIntestinais
        ) as [number]
      ),
      new OutrosAtendimentos(
        Object.values(dateMap).map(
          (item: any) => item.totalAtendimentosPorOutrosCasos
        ) as [number]
      ),
      new AtendimentosAgudos(
        Object.values(dateMap).map(
          (item: any) =>
            item.totalFebreExantematicas +
            item.totalFebreInespecificas +
            item.totalInfeccoesRespiratorias +
            item.totalInfeccoesIntestinais
        ) as [number]
      ),
    ],
  };
  return result;
};
