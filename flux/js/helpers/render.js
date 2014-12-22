var React = require('react');
var Router = require('react-router');
var Async = require('async');

var Render = {
    
    renderServer: function(moduleName, props) {
        
        var module = React.createFactory(require(moduleName));
        var component = module(props);
    
        return React.renderToString(component);
    },

    renderClient: function(moduleName, props, element) {

		var module = React.createFactory(require(moduleName));
        var component = module(props);

    	return React.render(component, document.getElementById(element));
    },

    renderRouted: function(routes, route, props) {

        var routes = React.createFactory(require(routes));

        Router.run(routes, route, function(module) {
            return React.renderToString(module(props));
        });

        return "xxx"
    }
    
};

module.exports = Render