var React = require('react');

var ComponentDetail = React.createClass({

	getInitialState: function() {
		return {
			'checked': false
		};
	},

	render: function() {				
		return 	<div className="panel" data-checked={ this.state.checked }>
					<h4><input type="checkbox" onChange={ this._onHandleCheckboxChange } />{ this.props.item.fields.title }</h4>
					<p>{ this.props.item.fields.description }</p>
				</div>;
	},

	_onHandleCheckboxChange: function(event) {
		this.setState({ 'checked': !this.state.checked });
	}

});

module.exports = ComponentDetail;