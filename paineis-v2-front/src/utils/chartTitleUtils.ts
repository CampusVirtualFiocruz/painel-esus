export function getChartDescription(description: string | undefined, reportViewType: any, content: Record<string, any>) {
  const baseDesc = !!content?.[String(description)] ? String(content?.[String(description)]) : description || '';
  
  if (reportViewType) {
    let sufixo = " no município";
    if (reportViewType === "EQUIPE") sufixo = " na Equipe";
    if (reportViewType === "UBS") sufixo = " na UBS";
    return baseDesc + sufixo;
  }
  
  return baseDesc;
}