'use strict'

import cardinals from './cardinals'

const { rules, rulesByLocale } = cardinals

function normalizeLocale (locale) {
  return locale.toLowerCase().replace('_', '-')
}

function getLanguage (locale) {
  const separator = locale.indexOf('-')
  return separator > 0 ? locale.substr(0, separator) : locale
}

function getPluralRuleForCardinalsByLocale (locale) {
  locale = normalizeLocale(locale)
  let index = rulesByLocale[locale]
  if (index === undefined) {
    const language = getLanguage(locale)
    index = rulesByLocale[language]
  }
  if (index === undefined) {
    throw new Error(`Unrecognized locale: "${locale}".`)
  }
  return rules[index]
}

function getPluralRuleForCardinalsByIndex (index) {
  const rule = rules[index]
  if (rule === undefined) {
    throw new Error(`Invalid index: "${index}".`)
  }
  return rule
}

function getPluralFormForCardinalByLocale (locale, count) {
  const rule = getPluralRuleForCardinalsByLocale(locale)
  return rule(count)
}

function getPluralFormForCardinalByIndex (index, count) {
  const rule = getPluralRuleForCardinalsByIndex(index)
  return rule(count)
}

export {
  getPluralRuleForCardinalsByLocale, getPluralFormForCardinalByLocale,
  getPluralRuleForCardinalsByIndex, getPluralFormForCardinalByIndex
}
