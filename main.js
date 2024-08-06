const newman = require('newman'); // require newman in your project
const fs = require('fs');

// call newman.run to pass `options` object and wait for callback
newman.run({
    collection: require('./DC3.postman_collection.json'),
    global: require('./workspace.postman_globals.json'),
    reporters: 'cli'
}).on('request', (error, data) => {
    if (error) {
        console.log(error);
        return;
    }

    const requestName = data.item.name.replace(/[^a-z0-9]/gi, '-');
    const fileName = `response-${requestName}.json`;
    const content = data.response.stream.toString();
    
    fs.writeFile(fileName, content, function (error) {
        if (error) { 
             console.error(error); 
        }
     });

     /// TODO: all global error handling
});
