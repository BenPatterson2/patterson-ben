'use strict';
const packageJson = require('../package.json');

// Grab NODE_ENV and REACT_APP_* environment variables and prepare them to be
// injected into the application via DefinePlugin in Webpack configuration.

var REACT_APP = /^REACT_APP_/i;

function getClientEnvironment(publicUrl) {
  var env = process.env.NODE_ENV || 'development';
  //create the thingy
  var aliases = packageJson.envAliases && packageJson.envAliases[env] || {};
  var envSpecificEnv = Object.keys(aliases).reduce((env,key) =>{
      var val = aliases[key];
      env[key] =  process.env[val];
      return env;
    },{
    // Useful for determining whether we’re running in production mode.
    // Most importantly, it switches React into the correct mode.
    'NODE_ENV': env,
    // Useful for resolving the correct path to static assets in `public`.
    // For example, <img src={process.env.PUBLIC_URL + '/img/logo.png'} />.
    // This should only be used as an escape hatch. Normally you would put
    // images into the `src` and `import` them in code to get their paths.
    'PUBLIC_URL': publicUrl
  })


  var raw = Object
    .keys(process.env)
    .filter(key => {
      return aliases[key] || REACT_APP.test(key)
    })
    .reduce((env, key) => {
      env[key] = process.env[key];
      return env;
    }, envSpecificEnv  );
  // Stringify all values so we can feed into Webpack DefinePlugin
  var stringified = {
    'process.env': Object
      .keys(raw)
      .reduce((env, key) => {
        env[key] = JSON.stringify(raw[key]);
        return env;
      }, {})
  };

  return { raw, stringified };
}

module.exports = getClientEnvironment;
