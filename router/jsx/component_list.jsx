var React = require('react');

var ComponentDetail = React.createFactory(require('./component_detail.jsx'));

var ComponentList = React.createClass({

	render: function() {
		var items = [];
		var props = this.props;

		for (item in props) {
			items.push(ComponentDetail(this.props[item]));
		}

		return <div>{ items }</div>;
	}
});

module.exports = ComponentList;