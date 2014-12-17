var React = require('react');
var Router = require('react-router');

var App = require('./app.jsx');
var ComponentList = require('./component_list.jsx');
var ComponentDetail = require('./component_detail.jsx');

var Route = Router.Route;
var NotFoundRoute = Router.NotFoundRoute;

var Routes = (
    <Route handler={App} path="/router/react/">
        <Route name="components" path="/router/react/components/" handler={ComponentList}>
            <Route name="component" path="/router/react/components/:pk" handler={ComponentDetail} />
        </Route>
    </Route>
);

module.exports = Routes;