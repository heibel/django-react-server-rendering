var http = require('http');
var url = require('url');

var React = require('react');
var Jsx = require('node-jsx');

Jsx.install();

http.createServer(function (req, res) {
	
	var query = url.parse(req.url, true).query;
	var ComponentList = React.createFactory(require('../component/jsx/' + query.component));

	res.writeHead(200, {'Content-Type': 'text/plain'});
	res.end(React.renderToString(ComponentList(JSON.parse(query.props))));

}).listen(9615);