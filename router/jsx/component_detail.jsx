var React = require('react');
var Router = require('react-router');

var Link = Router.Link;

var ComponentDetail = React.createClass({

	mixins: [Router.State],

	getInitialState: function() {
		return {
			'active': false
		};
	},

	render: function() {
		return 	<div className={ this.getParams().pk == this.props.pk ? 'active' : '' }>
					<Link to="component" params={ this.props }>{ this.props.fields.title }</Link>
				</div>;
	}

});

module.exports = ComponentDetail;