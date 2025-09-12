export const numberFormat = (number: number) => {
  return new Intl.NumberFormat('pt-BR', {
    maximumSignificantDigits: 3,
  }).format(number);
};

export const capitalizeName = (s: string) => {
  return String(s)
    .split(' ')
    .map(part => {
      if (
        part.toLowerCase() === 'do' ||
        part.toLowerCase() === 'da' ||
        part.toLowerCase() === 'de' ||
        part.toLowerCase() === 'dos' ||
        part.toLowerCase() === 'das'
      ) {
        return part.toLowerCase();
      }
      if (
        part.toUpperCase() === 'ESF' ||
        part.toUpperCase() === 'NASF' ||
        part.toUpperCase() === 'III'
      ) {
        return part.toUpperCase();
      }
      return part.charAt(0).toUpperCase() + part.slice(1).toLowerCase();
    })
    .join(' ');
};
