var http = require('http');
var url = require('url');

var zerorpc = require("zerorpc");
var browserify = require('browserify');

var React = require('react');
var Router = require('react-router');
var Jsx = require('node-jsx');

Jsx.install();

var Routes = require('../router/jsx/router.jsx');

var server = new zerorpc.Server({

    render: function(url, props, reply) {

    	Router.run(Routes, url, function (Handler) {
	        reply(null, React.renderToString(React.createElement(Handler, JSON.parse(props))));
	    });

    }

});

server.bind("tcp://0.0.0.0:4242");