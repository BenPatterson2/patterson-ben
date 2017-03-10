const fs = require('fs');
const path = require('path');

const browserify= require('browserify');
const q = require('q');


function compileClient(){
  var b = browserify({ entries: path.join(__dirname, 'client','front_page.js') });
  return q.ninvoke(b,'bundle')
  .then(function(results){
    fs.writeFileSync(path.join(__dirname, 'app','static','js', 'front_page.js'), results);
  });
}

if (require.main === module) {

  compileClient()
  .then(function(){
    console.log("Client Compiled");
    process.exit([0]);
  })
 .fail(function(err){
   console.dir(err.message);
   process.exit([1]);
 });
}