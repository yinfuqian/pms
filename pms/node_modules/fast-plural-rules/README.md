# Fast Plural Rules
[![NPM version](https://badge.fury.io/js/fast-plural-rules.png)](http://badge.fury.io/js/fast-plural-rules)
[![Build Status](https://travis-ci.org/prantlf/fast-plural-rules.png)](https://travis-ci.org/prantlf/fast-plural-rules)
[![Coverage Status](https://coveralls.io/repos/github/prantlf/fast-plural-rules/badge.svg?branch=master)](https://coveralls.io/github/prantlf/fast-plural-rules?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/9f1034029c0747a980cd49f64f16338b)](https://www.codacy.com/app/prantlf/fast-plural-rules?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=prantlf/fast-plural-rules&amp;utm_campaign=Badge_Grade)
[![Dependency Status](https://david-dm.org/prantlf/fast-plural-rules.svg)](https://david-dm.org/prantlf/fast-plural-rules)
[![devDependency Status](https://david-dm.org/prantlf/fast-plural-rules/dev-status.svg)](https://david-dm.org/prantlf/fast-plural-rules#info=devDependencies)
[![JavaScript Style Guide](https://img.shields.io/badge/code_style-standard-brightgreen.svg)](https://standardjs.com)

[![NPM Downloads](https://nodei.co/npm/fast-plural-rules.png?downloads=true&stars=true)](https://www.npmjs.com/package/fast-plural-rules)

Evaluates locale-specific plural rules to identify the right plural form for a cardinal number, which represents an item count. Internationalization libraries can utilize it to choose the right localized string.

* Focused and complete - [nothing but the rule evaluation](./src/index.d.ts) is included, but still [supporting almost 150 languages](./docs/languages.md#supported-languages).
* Tiny and [fast](./docs/speed.md#plural-form-lookup-speed) - 3 kB minified, 1 kB gzipped. Using [plain hand-coded functions](./src/cardinals.js) as [plural rules](./docs/design.md#plural-rules) to pick [plural forms](./docs/design.md#plural-forms).
* Reliable and correct - written using the [Translate Project documentation] and the [Mozilla documentation].

### Table of Contents

- [Synopsis](#synopsis)
- [Installation and Getting Started](#installation-and-getting-started)
- [Usage Scenarios](./docs/usage.md#usage-scenarios)
- [Design Concepts](./docs/design.md#design-concepts)
- [Supported Languages](./docs/languages.md#supported-languages)
- [API Reference](./docs/API.md#api-reference)
- [Library Integrations](#library-integrations)
- [Contributing](#contributing)
- [Release History](#release-history)
- [License](#license)

## Synopsis

```js
const { getPluralFormForCardinalByLocale } = require('fast-plural-rules')

// Returns index of the plural form for the specified locale and cardinal.
getPluralFormForCardinalByLocale('en', 1) // Returns 0; "1 file"
getPluralFormForCardinalByLocale('en', 2) // Returns 1; "2 files"
getPluralFormForCardinalByLocale('en', 5) // Returns 1; "5 files"
getPluralFormForCardinalByLocale('cs', 1) // Returns 0; "1 soubor"
getPluralFormForCardinalByLocale('cs', 2) // Returns 1; "2 soubory"
getPluralFormForCardinalByLocale('cs', 5) // Returns 2; "5 souborů"

// English: 0 - singular
//          1 - plural
// Czech:   0 - singular
//          1 - plural for 2-4 items
//          2 - plural for 5+ items
```

## Installation and Getting Started

This module can be installed in your project using [NPM] or [Yarn]. Make sure, that you use [Node.js] version 6 or newer.

```sh
$ npm i fast-plural-rules --save
```

```sh
$ yarn add fast-plural-rules
```

Functions are exposed as named exports, for example:

```js
const { getPluralFormForCardinalByLocale } = require('fast-plural-rules')
```

You can read more about the [module loading](./docs/API.md#loading) in other environments, like with ES6 or in web browsers. [Usage scenarios](./docs/usage.md#usage-scenarios) demonstrate applications of this library in typical real-world situations. [Design concepts](./docs/design.md#design-concepts) explain the approach to the correct internationalization of messages with cardinals taken by this library. Translators will read about [plural rules for supported languages](./languages.md#supported-languages) to be able to write the right plural forms to language packs. Finally, the [API reference](./docs/API.md#api-reference) lists all functions with a description of their functionality.

## Library Integrations

* [Extended Day.js] - [relativeTime plugin] formats time durations to the past and to the future.

## Contributing

In lieu of a formal styleguide, take care to maintain the existing coding style.  Add unit tests for any new or changed functionality. Lint and test your code using Grunt.

## Release History

* 2018-10-28   v0.0.1   Initial release

## License

Copyright (c) 2018 Ferdinand Prantl

Licensed under the MIT license.

[Node.js]: http://nodejs.org/
[NPM]: https://www.npmjs.com/
[Yarn]: https://yarnpkg.com/
[Translate Project documentation]: http://docs.translatehouse.org/projects/localization-guide/en/latest/l10n/pluralforms.html#pluralforms-list
[Mozilla documentation]: https://developer.mozilla.org/en-US/docs/Mozilla/Localization/Localization_and_Plurals#List_of_Plural_Rules
[Extended Day.js]: https://github.com/prantlf/dayjs
[relativeTime plugin]: https://github.com/prantlf/dayjs/blob/combined/docs/en/Plugin.md#relativetime
