
var forEach = require('lodash/forEach');
var markdown = require('markdown').markdown;
exports.buildMarkDownPreview = buildMarkDownPreview;


function  buildMarkDownPreview(){
    forEach($('.markdown-panel'), function(panel){
      var preview = $(panel).find('.markdown-input-preview')[0];
      var textinput =  $(panel).find('.markdown-input')[0];
      textinput.oninput= function(){
        preview.innerHTML = markdown.toHTML(textinput.value);
      };
    });
}


