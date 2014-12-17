var http = require('http');
var url = require('url');

var React = require('react');
var Router = require('react-router');
var Jsx = require('node-jsx');

Jsx.install();

var Routes = require('../router/jsx/router.jsx');

http.createServer(function (req, res) {

    var query = url.parse(req.url, true).query;
    
    Router.run(Routes, req.url, function (Handler) {
        res.end(React.renderToString(React.createElement(Handler, JSON.parse(query.props))));
    });

}).listen(9616);