var React = require('react');

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
    }
    
};

module.exports = Render