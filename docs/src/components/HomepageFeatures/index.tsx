import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

type FeatureItem = {
  title: string;
  Svg: React.ComponentType<React.ComponentProps<'svg'>>;
  description: JSX.Element;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'Município',
    Svg: require('../../../../paineis-v2-front/src/assets/images/visualizacao/Icone_Municipio.svg').default,
    description: (
      <>
        Oferece uma visão geral, sendo útil principalmente para o gestor de saúde municipal, que poderá identificar o cenário atual do município.
      </>
    ),
  },
  {
    title: 'Unidade Básica de Saúde',
    Svg: require('../../../../paineis-v2-front/src/assets/images/visualizacao/Icone_UBS.svg').default,
    description: (
      <>
        Apresenta informações sobre regras de processamento e visualização do relatório de Indicadores de cofinanciamento federal do Piso de Atenção Primária à Saúde - APS, no âmbito do Sistema Único de Saúde - SUS.
      </>
    ),
  },
  {
    title: 'Equipe',
    Svg: require('../../../../paineis-v2-front/src/assets/images/visualizacao/Icone_Equipe.svg').default,
    description: (
      <>
        Tem como principal objetivo apresentar o cenário da população acompanhada pela equipe.
      </>
    ),
  },
];

function Feature({title, Svg, description}: FeatureItem) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): JSX.Element {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className={`${styles.containerCenter} col col--6 padding-vert--md`}>
          <h2 className="text--center">O que é o Painel e-SUS APS?</h2>
          <p>Com funcionalidades que facilitam o acompanhamento de indicadores, a gestão do cuidado e a promoção de boas práticas, o Painel e-SUS APS é uma ferramenta essencial para profissionais da assistência e da gestão em saúde.</p>
          <p>
            Integrado à base de dados do Prontuário Eletrônico e-SUS APS, ele oferece suporte direto à tomada de decisão, permitindo intervenções precisas e oportunas que impulsionam resultados concretos na atenção primária.
          </p>
        </div>
        <div className={`${styles.containerCenter} col col--6 padding-vert--md`}>
          <h2 className="text--center">Tipos de visualização</h2>
          <p>Os relatórios são apresentados em três níveis de visualização: Município, Unidade Básica de Saúde (UBS) e Equipe. Os diferentes níveis de visualização apresentados no Painel dialogam com o conceito de território.</p>
        </div>
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
