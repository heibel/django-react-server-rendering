var fs = require('fs');

var browserify = require('browserify');
var reactify = require('reactify');

var bundle = browserify({
	basedir: './runtime/'
});

bundle
	.add('./jsx/component_list.jsx')
	.transform(reactify)
	.require('./js/render.js', { expose: 'render' })
	.require('./jsx/component_list.jsx', { expose: 'app' })
	.bundle()
	.pipe(fs.createWriteStream(__dirname + '/runtime_prog.js'));
