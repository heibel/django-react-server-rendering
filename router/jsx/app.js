var React = require('react');
var Router = require('react-router');

var Routes = require('./router.jsx');

Router.run(Routes, Router.HistoryLocation, function (Handler) {

	var props = JSON.parse(document.getElementById('props').innerHTML);

	React.render(
		React.createElement(Handler, props),
		document.getElementById('react')
	);
});