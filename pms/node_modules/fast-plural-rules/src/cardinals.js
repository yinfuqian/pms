// See the plural rules at https://developer.mozilla.org/en-US/docs/Mozilla/Localization/Localization_and_Plurals#List_of_Plural_Rules
// See the expressions to identify the plural form at http://docs.translatehouse.org/projects/localization-guide/en/latest/l10n/pluralforms.html#pluralforms-list

/* eslint-disable no-confusing-arrow, no-nested-ternary */
/* istanbul ignore file */

const cardinals = {
  rules: [
    // Plural rule #0 (1 form)
    // Families: Asian (Chinese, Japanese, Korean), Persian,
    //   Turkic/Altaic (Turkish), Thai, Lao
    // Locales: ay (Aymará), bo (Tibetan), cgg (Chiga), dz (Dzongkha),
    //   id (Indonesian), ja (Japanese), jbo (Lojban), ka (Georgian),
    //   km (Khmer), ko (Korean), lo (Lao), ms (Malay), my (Burmese),
    //   sah (Yakut), su (Sundanese), th (Thai), tt (Tatar), ug (Uyghur),
    //   vi (Vietnamese), wo (Wolof), zh-CN (Simplified Chinese)
    // everything: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
    // 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
    // 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, ...
    () => 0,
    // Plural rule #1 (2 forms)
    // Families: Germanic (Danish, Dutch, English, Faroese, Frisian, German,
    //   Norwegian, Swedish), Finno-Ugric (Estonian, Finnish, Hungarian),
    //   Language isolate (Basque), Latin/Greek (Greek), Semitic (Hebrew),
    //   Romanic (Italian, Portuguese, Spanish, Catalan), Vietnamese,
    // Locales: af (Afrikaans), an (Aragonese), anp (Angika), as (Assamese),
    //   ast (Asturian), az (Azerbaijani), bg (Bulgarian), bn (Bengali),
    //   brx (Bodo), ca (Catalan), da (Danish), de (German), doi (Dogri),
    //   el (Greek), en (English), eo (Esperanto), es (Spanish),
    //   es-AR (Argentinean Spanish), et (Estonian), eu (Basque),
    //   ff (Fulah), fi (Finnish), fo (Faroese), fur (Friulian),
    //   fy (Frisian), gl (Galician), gu (Gujarati), ha (Hausa),
    //   he (Hebrew), hi (Hindi), hne (Chhattisgarhi), hu (Hungarian),
    //   hy (Armenian), ia (Interlingua), it (Italian), kk (Kazakh),
    //   kl (Greenlandic), kn (Kannada), ku (Kurdish), ky (Kyrgyz),
    //   lb (Letzeburgesch), mai (Maithili), ml (Malayalam), mn (Mongolian),
    //   mni (Manipuri), mr (Marathi), nah (Nahuatl), nap (Neapolitan),
    //   nb (Norwegian Bokmal), ne (Nepali), nl (Dutch),
    //   nn (Norwegian Nynorsk), no (Norwegian), nso (Northern Sotho),
    //   or (Oriya), pa (Punjabi), pap (Papiamento), pms (Piemontese),
    //   ps (Pashto), pt (Portuguese), rm (Romansh), rw (Kinyarwanda),
    //   sat (Santali), sco (Scots), sd (Sindhi), se (Northern Sami),
    //   si (Sinhala), so (Somali), son (Songhay), sq (Albanian),
    //   sv (Swedish), sw (Swahili), ta (Tamil), te (Telugu), tk (Turkmen),
    //   ur (Urdu), yo (Yoruba)
    // is 1: 1
    // everything else: 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
    // 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
    // 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, ...
    n => n === 1 ? 0 : 1,
    // Plural rule #2 (2 forms)
    // Families: Romanic (French, Brazilian Portuguese)
    // Locales: ach (Acholi), ak (Akan), am (Amharic), arn (Mapudungun),
    //   br (Breton), fa (Persian), fil (Filipino), fr (French), gun (Gun),
    //   ln (Lingala), mfe (Mauritian Creole), mg (Malagasy), mi (Maori),
    //   oc (Occitan), pt-BR (Brazilian Portuguese), tg (Tajik), ti (Tigrinya),
    //   tr (Turkish), uz (Uzbek), wa (Walloon), zh-TW (Traditional Chinese)
    // is 0 or 1: 0, 1
    // everything else: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
    // 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
    // 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, ...
    n => n <= 1 ? 0 : 1,
    // Plural rule #3 (3 forms)
    // Families: Baltic (Latvian, Latgalian)
    // Locales: lv (Latvian)
    // ends in 1, excluding 11: 1, 21, 31, 41, 51, 61, 71, 81, 91, 101, 121, 131,
    // 141, 151, 161, 171, 181, 191, 201, 221, 231, 241, 251, 261, 271, 281, 291,
    // ...
    // everything else: 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18,
    // 19, 22, 23, 24, 25, 26, 27, 28, 29, 32, 33, 34, 35, 36, 37, 38, 39, 42,
    // 43, 44, 45, 46, 47, 48, 49, 52, 53, ...
    // ends in 0: 0
    n => n % 10 === 1 && n % 100 !== 11 ? 0 : n % 10 !== 0 ? 1 : 2,
    // Plural rule #4 (4 forms)
    // Families: Celtic (Scottish Gaelic)
    // Locales: gd (Scottish Gaelic)
    // is 1 or 11: 1, 11
    // is 2 or 12: 2, 12
    // is 3-10 or 13-19: 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15, 16, 17, 18, 19
    // everything else: 0, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32,
    // 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
    // 51, ...
    n => n === 1 || n === 11 ? 0 : n === 2 || n === 12 ? 1 : n > 2 && n < 20 ? 2 : 3,
    // Plural rule #5 (3 forms)
    // Families: Romanic (Romanian)
    // Locales: ro (Romanian)
    // is 1: 1
    // is 0 or ends in 01-19, excluding 1: 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
    // 13, 14, 15, 16, 17, 18, 19, 101, 102, 103, 104, 105, 106, 107, 108, 109,
    // 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 201, 202, 203, 204, 205,
    // 206, 207, 208, 209, 210, 211, 212, ...
    // everything else: 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
    // 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51,
    // 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, ...
    n => n === 1 ? 0 : n === 0 || (n % 100 > 0 && n % 100 < 20) ? 1 : 2,
    // Plural rule #6 (3 forms)
    // Families: Baltic (Lithuanian)
    // Locales: lt (Lithuanian)
    // ends in 1, excluding 11: 1, 21, 31, 41, 51, 61, 71, 81, 91, 101, 121, 131,
    // 141, 151, 161, 171, 181, 191, 201, 221, 231, 241, 251, 261, 271, 281, 291,
    // ...
    // ends in 0 or ends in 11-19: 0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    // 30, 40, 50, 60, 70, 80, 90, 100, 110, 111, 112, 113, 114, 115, 116, 117,
    // 118, 119, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 211, 212, 213,
    // 214, 215, 216, 217, 218, 219, 220, ...
    // everything else: 2, 3, 4, 5, 6, 7, 8, 9, 22, 23, 24, 25, 26, 27, 28, 29,
    // 32, 33, 34, 35, 36, 37, 38, 39, 42, 43, 44, 45, 46, 47, 48, 49, 52, 53,
    // 54, 55, 56, 57, 58, 59, 62, 63, 64, 65, 66, 67, 68, 69, 72, 73, ...
    n => n % 10 === 1 && n % 100 !== 11 ? 0
      : n % 10 >= 2 && (n % 100 < 10 || n % 100 >= 20) ? 1 : 2,
    // Plural rule #7 (3 forms)
    // Families: Slavic (Belarusian, Bosnian, Croatian, Serbian, Russian, Ukrainian)
    // Locales: be (Belarusian), bs (Bosnian), hr (Croatian), ru (Russian),
    //   sr (Serbian), uk (Ukrainian)
    // ends in 1, excluding 11: 1, 21, 31, 41, 51, 61, 71, 81, 91, 101, 121, 131,
    // 141, 151, 161, 171, 181, 191, 201, 221, 231, 241, 251, 261, 271, 281, 291,
    // ...
    // ends in 2-4, excluding 12-14: 2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44,
    // 52, 53, 54, 62, 63, 64, 72, 73, 74, 82, 83, 84, 92, 93, 94, 102, 103, 104,
    // 122, 123, 124, 132, 133, 134, 142, 143, 144, 152, 153, 154, 162, 163, 164,
    // 172, 173, 174, 182, 183, ...
    // everything else: 0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
    // 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49,
    // 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68, 69, 70, 75, 76, 77, ..., 112,
    // 113, ..., 212, 213, ...
    n => n % 10 === 1 && n % 100 !== 11 ? 0
      : n % 10 >= 2 && n % 10 <= 4 && (n % 100 < 10 || n % 100 >= 20) ? 1 : 2,
    // Plural rule #8 (3 forms)
    // Families: Slavic (Slovak, Czech)
    // Locales: cs (Czech), sk (Slovak)
    // is 1: 1
    // is 2-4: 2, 3, 4
    // everything else: 0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
    // 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37,
    // 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, ...
    n => n === 1 ? 0 : n >= 2 && n <= 4 ? 1 : 2,
    // Plural rule #9 (3 forms)
    // Families: Slavic (Polish)
    // Locales: pl (Polish)
    // is 1: 1
    // ends in 2-4, excluding 12-14: 2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44,
    // 52, 53, 54, 62, 63, 64, 72, 73, 74, 82, 83, 84, 92, 93, 94, 102, 103, 104,
    // 122, 123, 124, 132, 133, 134, 142, 143, 144, 152, 153, 154, 162, 163, 164,
    // 172, 173, 174, 182, 183, ...
    // everything else: 0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
    // 20, 21, 25, 26, 27, 28, 29, 30, 31, 35, 36, 37, 38, 39, 40, 41, 45, 46,
    // 47, 48, 49, 50, 51, 55, 56, 57, 58, 59, 60, 61, 65, 66, 67, 68, ...
    n => n === 1 ? 0
      : n % 10 >= 2 && n % 10 <= 4 && (n % 100 < 10 || n % 100 >= 20) ? 1 : 2,
    // Plural rule #10 (4 forms)
    // Families: Slavic (Slovenian, Sorbian)
    // Locales: sl (Slovenian)
    // ends in 01: 1, 101, 201, ...
    // ends in 02: 2, 102, 202, ...
    // ends in 03-04: 3, 4, 103, 104, 203, 204, ...
    // everything else: 0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
    // 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37,
    // 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, ...
    n => n % 100 === 1 ? 0 : n % 100 === 2 ? 1 : n % 100 === 3 || n % 100 === 4 ? 2 : 3,
    // Plural rule #11 (5 forms)
    // Families: Celtic (Irish Gaelic)
    // Locales: ga (Irish)
    // is 1: 1
    // is 2: 2
    // is 3-6: 3, 4, 5, 6
    // is 7-10: 7, 8, 9, 10
    // everything else: 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
    // 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41,
    // 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, ...
    n => n === 1 ? 0 : n === 2 ? 1 : n > 2 && n < 7 ? 2 : n > 6 && n < 11 ? 3 : 4,
    // Plural rule #12 (6 forms)
    // Families: Semitic (Arabic)
    // Locales: ar (Arabic)
    // is 1: 1
    // is 2: 2
    // ends in 03-10: 3, 4, 5, 6, 7, 8, 9, 10, 103, 104, 105, 106, 107, 108, 109,
    // 110, 203, 204, 205, 206, 207, 208, 209, 210, ...
    // everything else but is 0 and ends in 00-02, excluding 0-2: 11, 12, 13, 14,
    // 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32,
    // 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
    // 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, ...
    // ends in 00-02, excluding 0-2: 100, 101, 102, 200, 201, 202, ...
    // is 0: 0
    n => n === 1 ? 0 : n === 2 ? 1 : n % 100 >= 3 && n % 100 <= 10 ? 2
      : n % 100 >= 11 ? 3 : n !== 0 ? 4 : 5,
    // Plural rule #13 (4 forms)
    // Families: Semitic (Maltese)
    // Locales: mt (Maltese)
    // is 1: 1
    // is 0 or ends in 01-10, excluding 1: 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 101,
    // 102, 103, 104, 105, 106, 107, 108, 109, 110, 201, 202, 203, 204, 205, 206,
    // 207, 208, 209, 210, ...
    // ends in 11-19: 11, 12, 13, 14, 15, 16, 17, 18, 19, 111, 112, 113, 114,
    // 115, 116, 117, 118, 119, 211, 212, 213, 214, 215, 216, 217, 218, 219, ...
    // everything else: 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
    // 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51,
    // 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, ...
    n => n === 1 ? 0 : n === 0 || (n % 100 > 1 && n % 100 < 11) ? 1
      : n % 100 > 10 && n % 100 < 20 ? 2 : 3,
    // Plural rule #14 (3 forms)
    // Families: unused
    // ends in 1: 1, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 111, 121, 131, 141,
    // 151, 161, 171, 181, 191, 201, 211, 221, 231, 241, 251, 261, 271, 281, 291,
    // ...
    // ends in 2: 2, 12, 22, 32, 42, 52, 62, 72, 82, 92, 102, 112, 122, 132, 142,
    // 152, 162, 172, 182, 192, 202, 212, 222, 232, 242, 252, 262, 272, 282, 292,
    // ...
    // everything else: 0, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15, 16, 17, 18, 19,
    // 20, 23, 24, 25, 26, 27, 28, 29, 30, 33, 34, 35, 36, 37, 38, 39, 40, 43,
    // 44, 45, 46, 47, 48, 49, 50, 53, 54, 55, 56, 57, 58, 59, 60, 63, ...
    n => n % 10 === 1 ? 0 : n % 10 === 2 ? 1 : 2,
    // Plural rule #15 (2 forms)
    // Families: Icelandic, Macedonian
    // Locales: is (Icelandic), mk (Macedonian)
    // ends in 1, excluding 11: 1, 21, 31, 41, 51, 61, 71, 81, 91, 101, 121, 131,
    // 141, 151, 161, 171, 181, 191, 201, 221, 231, 241, 251, 261, 271, 281, 291,
    // ...
    // everything else: 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
    // 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36,
    // 37, 38, 39, 40, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52, 53, 54, ...
    n => n % 10 === 1 && n % 100 !== 11 ? 0 : 1,
    // Plural rule #16 (5 forms)
    // Families: Celtic (Breton)
    // ends in 1, excluding 11, 71, 91: 21, 31, 41, 51, 61, 81, 101, 121, 131,
    // 141, 151, 161, 181, 201, 221, 231, 241, 251, 261, 281, ...
    // ends in 2, excluding 12, 72, 92: 2, 22, 32, 42, 52, 62, 82, 102, 122, 132,
    // 142, 152, 162, 182, 202, 222, 232, 242, 252, 262, 282, ...
    // ends in 3, 4 or 9 excluding 13, 14, 19, 73, 74, 79, 93, 94, 99: 3, 4, 9,
    // 23, 24, 29, 33, 34, 39, 43, 44, 49, 53, 54, 59, ...
    // ends in 1000000: 1000000: 1000000, 2000000, 3000000, 4000000, 5000000,
    // 6000000, 7000000, 8000000, 9000000, 10000000, ...
    // everything else: 0, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
    // 20, 25, 26, 27, 28, 30, 35, 36, 37, 38, 40, ...
    n => n % 10 === 1 && n % 100 !== 11 && n % 100 !== 71 && n % 100 !== 91 ? 0
      : n % 10 === 2 && n % 100 !== 12 && n % 100 !== 72 && n % 100 !== 92 ? 2
        : n % 10 === 3 && n % 100 !== 13 && n % 100 !== 73 && n % 100 !== 93 ? 3
          : n % 10 === 4 && n % 100 !== 14 && n % 100 !== 74 && n % 100 !== 94 ? 3
            : n % 10 === 9 && n % 100 !== 19 && n % 100 !== 79 && n % 100 !== 99 ? 3
              : 4,
    // Plural rule #17 (2 forms)
    // Families: Ecuador indigenous languages (Shuar)
    // Locales: jv (Javanese)
    // everything else: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
    // 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
    // 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, ...
    // is 0: 0
    n => n !== 0 ? 0 : 1,
    // Plural rule #18 (6 forms)
    // Families: Welsh
    // Locales: cy (Welsh)
    // is 1: 1
    // is 2: 2
    // is 3: 3
    // is 6: 6
    // everything else: 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
    // 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37,
    // 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, ...
    // is 0: 0
    n => n === 1 ? 0 : n === 2 ? 1 : n === 3 ? 2 : n === 6 ? 3 : n !== 0 ? 4 : 5,
    // Plural rule #19 (3 forms)
    // Locales: csb (Kashubian)
    // is 1: 1
    // ends in 2-4, excluding 12-14: 2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44,
    // 52, 53, 54, 62, 63, 64, 72, 73, 74, 82, 83, 84, 92, 93, 94, 102, 103, 104,
    // 122, 123, 124, 132, 133, 134, 142, 143, 144, 152, 153, 154, 162, 163, 164,
    // 172, 173, 174, 182, 183, ...
    // everything else: 0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
    // 20, 21, 25, 26, 27, 28, 29, 30, 31, 35, 36, 37, 38, 39, 40, 41, 45, 46,
    // 47, 48, 49, 50, 51, 55, 56, 57, 58, 59, 60, 61, 65, 66, 67, 68, 69, 70,
    // 71, 75, 76, 77, ..., 111, 115, ..., 211, 215, ...
    n => n === 1 ? 0
      : n % 10 >= 2 && n % 10 <= 4 && (n % 100 < 10 || n % 100 >= 20) ? 1 : 2,
    // Plural rule #20 (4 forms)
    // Locales: kw (Cornish)
    // is 1: 1
    // is 2: 2
    // is 3: 3
    // everything else: 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
    // 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37,
    // 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, ...
    n => n === 1 ? 0 : n === 2 ? 1 : n === 3 ? 2 : 3,
    // Plural rule #21 (3 forms)
    // Locales: me (Montenegro)
    // ends in 1, excluding 11: 1, 21, 31, 41, 51, 61, 71, 81, 91, 101, 121, 131,
    // 141, 151, 161, 171, 181, 191, 201, 221, 231, 241, 251, 261, 271, 281, 291,
    // ...
    // ends in 2-4, excluding 12-14: 2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44,
    // 52, 53, 54, 62, 63, 64, 72, 73, 74, 82, 83, 84, 92, 93, 94, 102, 103, 104,
    // 122, 123, 124, 132, 133, 134, 142, 143, 144, 152, 153, 154, 162, 163, 164,
    // 172, 173, 174, 182, 183, ...
    // everything else: 0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
    // 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49,
    // 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68, 69, 70, 75, 76, 77, ..., 112,
    // 113, ..., 212, 213, ...
    n => n % 10 === 1 && n % 100 !== 11 ? 0
      : n % 10 >= 2 && n % 10 <= 4 && (n % 100 < 10 || n % 100 >= 20) ? 1 : 2,
    // Plural rule #22 (3 forms)
    // Locales: mnk (Mandinka)
    // is 0: 0
    // is 1: 1
    // everything else: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
    // 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
    // 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, ...
    n => n === 0 ? 0 : n === 1 ? 1 : 2
  ],
  rulesByLocale: {
    ach: 2, // Acholi
    af: 1, // Afrikaans
    ak: 2, // Akan
    am: 2, // Amharic
    an: 1, // Aragonese
    anp: 1, // Angika
    ar: 12, // Arabic
    arn: 2, // Mapudungun
    as: 1, // Assamese
    ast: 1, // Asturian
    ay: 0, // Aymará
    az: 1, // Azerbaijani
    be: 7, // Belarusian
    bg: 1, // Bulgarian
    bn: 1, // Bengali
    bo: 0, // Tibetan
    br: 2, // Breton
    brx: 1, // Bodo
    bs: 7, // Bosnian
    ca: 1, // Catalan
    cgg: 0, // Chiga
    cs: 8, // Czech
    csb: 19, // Kashubian
    cy: 18, // Welsh
    da: 1, // Danish
    de: 1, // German
    doi: 1, // Dogri
    dz: 0, // Dzongkha
    el: 1, // Greek
    en: 1, // English
    eo: 1, // Esperanto
    es: 1, // Spanish
    'es-ar': 1, // Argentinean Spanish
    et: 1, // Estonian
    eu: 1, // Basque
    fa: 2, // Persian
    ff: 1, // Fulah
    fi: 1, // Finnish
    fil: 2, // Filipino
    fo: 1, // Faroese
    fr: 2, // French
    fur: 1, // Friulian
    fy: 1, // Frisian
    ga: 11, // Irish
    gd: 4, // Scottish Gaelic
    gl: 1, // Galician
    gu: 1, // Gujarati
    gun: 2, // Gun
    ha: 1, // Hausa
    he: 1, // Hebrew
    hi: 1, // Hindi
    hne: 1, // Chhattisgarhi
    hr: 7, // Croatian
    hu: 1, // Hungarian
    hy: 1, // Armenian
    ia: 1, // Interlingua
    id: 0, // Indonesian
    is: 15, // Icelandic
    it: 1, // Italian
    ja: 0, // Japanese
    jbo: 0, // Lojban
    jv: 17, // Javanese
    ka: 0, // Georgian
    kk: 1, // Kazakh
    kl: 1, // Greenlandic
    km: 0, // Khmer
    kn: 1, // Kannada
    ko: 0, // Korean
    ku: 1, // Kurdish
    kw: 20, // Cornish
    ky: 1, // Kyrgyz
    lb: 1, // Letzeburgesch
    ln: 2, // Lingala
    lo: 0, // Lao
    lt: 6, // Lithuanian
    lv: 3, // Latvian
    mai: 1, // Maithili
    me: 21, // Montenegro
    mfe: 2, // Mauritian Creole
    mg: 2, // Malagasy
    mi: 2, // Maori
    mk: 15, // Macedonian
    ml: 1, // Malayalam
    mn: 1, // Mongolian
    mni: 1, // Manipuri
    mnk: 22, // Mandinka
    mr: 1, // Marathi
    ms: 0, // Malay
    mt: 13, // Maltese
    my: 0, // Burmese
    nah: 1, // Nahuatl
    nap: 1, // Neapolitan
    nb: 1, // Norwegian Bokmal
    ne: 1, // Nepali
    nl: 1, // Dutch
    nn: 1, // Norwegian Nynorsk
    no: 1, // Norwegian
    nso: 1, // Northern Sotho
    oc: 2, // Occitan
    or: 1, // Oriya
    pa: 1, // Punjabi
    pap: 1, // Papiamento
    pl: 9, // Polish
    pms: 1, // Piemontese
    ps: 1, // Pashto
    pt: 1, // Portuguese
    'pt-br': 2, // Brazilian Portuguese
    rm: 1, // Romansh
    ro: 5, // Romanian
    ru: 7, // Russian
    rw: 1, // Kinyarwanda
    sah: 0, // Yakut
    sat: 1, // Santali
    sco: 1, // Scots
    sd: 1, // Sindhi
    se: 1, // Northern Sami
    si: 1, // Sinhala
    sk: 8, // Slovak
    sl: 10, // Slovenian
    so: 1, // Somali
    son: 1, // Songhay
    sq: 1, // Albanian
    sr: 7, // Serbian
    su: 0, // Sundanese
    sv: 1, // Swedish
    sw: 1, // Swahili
    ta: 1, // Tamil
    te: 1, // Telugu
    tg: 2, // Tajik
    th: 0, // Thai
    ti: 2, // Tigrinya
    tk: 1, // Turkmen
    tr: 2, // Turkish
    tt: 0, // Tatar
    ug: 0, // Uyghur
    uk: 7, // Ukrainian
    ur: 1, // Urdu
    uz: 2, // Uzbek
    vi: 0, // Vietnamese
    wa: 2, // Walloon
    wo: 0, // Wolof
    yo: 1, // Yoruba
    'zh-cn': 0, // Simplified Chinese
    'zh-tw': 2 // Traditional Chinese
  }
}

export default cardinals
