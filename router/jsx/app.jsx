var React = require('react');

var ComponentList = React.createFactory(require('./component_list.jsx'));

var App = React.createClass({

    render: function() {     
        return  <div>
    				{ ComponentList(this.props) }
                </div>;
    }

});

module.exports = App;