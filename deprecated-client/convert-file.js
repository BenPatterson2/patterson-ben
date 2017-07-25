
exports.convertFile = convertFile;

  //EXPORTED FUNCTIONS

// input
// options
//  maxHeight: number in px
//  maxWidth: number in px
//  quality: 1-100

function convertFiles(files, options) {
  var opts = options || {};
  opts.quality = (options.quality || 100)/100;
  var promises = input.files.reduce(function(acc,file){
    var reader = new FileReader();
    var promise = processImage(reader,options);
    acc.push(promise);

    return acc;
  }, []);
  return Promise.all(promises);
}

function scaledDimensions(img,options){
  var width = img.width;
  var height = img.height;
  if (options.maxWidth && width > options.maxWidth) {
    height *= maxWidth / width;
    width = maxWidth;
  }
  if (options.maxHeight && height > options.maxHeight)  {
    width *= maxHeight / height;
    height = maxHeight;
  }
  return { height:height, width:width };
}

function processFile(file, options){
  var img = document.createElement('img');
  var canvas = document.createElement('canvas');
  var ctx = canvas.getContext("2d");
  var promise = new Promise(function(resolve, reject){
    reader.onerror = reject;
    img.addEventListener("error", reject);
    img.addEventListener("load", function() {
      ctx.drawImage(img, 0, 0);
      var dimensions = scaleDimensions(img, options);
      canvas.width = dimensions.width;
      canvas.height = dimensions.height;
      ctx.drawImage(img, 0, 0, dimensions.width, dimensions.height);
      resolve({
        name: dimensions.width + '-' + dimensions.height + '_' + file.name ,
        data: canvas.toDataURL("image/png",options.quality)
      });
    });
  });
  reader.onload = function() { img.src = reader.result; };
  reader.readAsDataURL(file);
  return promise;
}
