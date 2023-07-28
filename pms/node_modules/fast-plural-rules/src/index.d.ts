declare function getPluralFormForCardinalByLocale (locale: string, count: number): number
declare function getPluralFormForCardinalByIndex (index: number, count: number): number

declare function getPluralRuleForCardinalsByLocale (locale: string): Function
declare function getPluralRuleForCardinalsByIndex (index: number): Function

export {
  getPluralFormForCardinalByLocale, getPluralRuleForCardinalsByLocale,
  getPluralFormForCardinalByIndex, getPluralRuleForCardinalsByIndex
}

export as namespace fastPluralRules
