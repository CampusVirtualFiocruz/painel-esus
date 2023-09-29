import {CHART_DATA, CHART_STACK_DATA} from './chart_data';
import {parseChartData,filterStackAccuteCare } from '../chart-data';

type TResponse = {
    ano: number;
    classe: string; 
    count: number; 
    nuCnes: number;
    mes: number;
    time: string;
}

describe('Chart data parser', () => { 

    test('testing conversion', () => {
        const totalInfeccoesRespiratorias = 21;    
        const totalInfeccoesIntestinais = 9;
        const totalFebreExantematicas = 2;
        const totalFebreInespecificas = 22;
        const totalAtendimentosPorSindromesAgudas = (
            totalInfeccoesRespiratorias +
            totalInfeccoesIntestinais +
            totalFebreExantematicas +
            totalFebreInespecificas
        );
        const totalAtendimentosPorOutrosCasos = (194+291);
        const response = parseChartData(CHART_DATA.data as TResponse[])
        expect(response.totalInfeccoesRespiratorias).toBe(totalInfeccoesRespiratorias);
        expect(response.totalInfeccoesIntestinais).toBe(totalInfeccoesIntestinais);
        expect(response.totalFebreExantematicas).toBe(totalFebreExantematicas);
        expect(response.totalFebreInespecificas).toBe(totalFebreInespecificas);
        expect(response.totalAtendimentosPorSindromesAgudas).toBe(totalAtendimentosPorSindromesAgudas);
        expect(response.totalAtendimentosPorOutrosCasos).toBe(totalAtendimentosPorOutrosCasos);

    });

    test('testing empty response', () => {
        const response = parseChartData([])
        expect(response.totalInfeccoesRespiratorias).toBe(0);
        expect(response.totalInfeccoesIntestinais).toBe(0);
        expect(response.totalFebreExantematicas).toBe(0);
        expect(response.totalFebreInespecificas).toBe(0);
        expect(response.totalAtendimentosPorSindromesAgudas).toBe(0);
        expect(response.totalAtendimentosPorOutrosCasos).toBe(0);
    })
});

describe('Chart Stack data parser', () => { 

    test('testing stack parse for Accute Cases', () => {

        const result = filterStackAccuteCare(CHART_STACK_DATA.data as TResponse[]);
        expect(result.labels.length).toBe(result.stack[0].data.length)
        expect(result.labels.length).toBe(result.stack[1].data.length)
        expect(result.labels.length).toBe(result.stack[2].data.length)
        expect(result.labels.length).toBe(result.stack[3].data.length)
    });

});