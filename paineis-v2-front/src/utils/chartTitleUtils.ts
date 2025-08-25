export function getChartDescription(description: string | undefined, reportViewType: any, content: Record<string, any>) {
  const baseDesc = !!content?.[String(description)] ? String(content?.[String(description)]) : description || '';

  if (reportViewType) {
    let sufixo = " no município";
    if (String(reportViewType).toUpperCase() === "EQUIPE") sufixo = " na equipe";
    if (String(reportViewType).toUpperCase() === "UBS") sufixo = " na UBS";
    return baseDesc + sufixo;
  }
  
  return baseDesc;
}