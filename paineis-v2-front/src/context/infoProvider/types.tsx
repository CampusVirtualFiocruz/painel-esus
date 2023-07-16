 
  export interface IContext{
    cityInformation: ICityInfomation|null;
    setCityInformation: (value: ICityInfomation) => void;
    city: string|null
  }
  export interface ICityInfomation{
    cep: string;
    codIgbe: string;
    estado: string;
    municipio: string
    uf: string;
  }
  
  export interface IInfoProvider {
    children: JSX.Element;
  }
  