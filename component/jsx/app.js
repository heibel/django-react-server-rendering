var React = require('react');
var ComponentList = React.createFactory(require('./component_list.jsx'));

React.render(
	ComponentList(JSON.parse(document.getElementById('props').innerHTML)),
	document.getElementById('react')
);