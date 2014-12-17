# Django + React serverside

### Work in progress

This project demonstrates two ways to render React templates serverside before serving them to the client. Serverside rendering exposes multiple benefits:  
- Better loading  
- Search Engine indexing  

While there are also some cutbacks, by example:  
- More time spending on template feeding (0,02 to 0.1 seconds delay on a server roundtrip, without caching or memoization)  
- An extra server process to take care of or library to install
 
The smart templating of react recognizes the checksum on the server-rendered elements and won't render again; preventing flickering. It will just add all the interactivity :)

## Setup
The example uses a supervisor config to hold up three server processes:  
- The Python / Django server  
- A Node server for demonstrating simple component rendering  
- A Node server for demonstrating isomorphic routes  

## Demo
Coming soon

## Javascript runtime
With PyExecJS and any JS runtime. Read more [here](https://github.com/doloopwhile/PyExecJS)

### Context
Do not use Gulp here! Use browserify from the command-line to compile your app, and make sure to expose your requires with Browserify so that PyExecJS can use these:  
 - Dev:  `browserify -t reactify -r ./runtime/js/render.js:render -r ./runtime/jsx/component_list.jsx:app > ./runtime/js/runtime.js`- Prod: `browserify -t reactify -tg uglifyify -r ./runtime/js/render.js:render -r ./runtime/jsx/component_list.jsx:app > ./runtime/js/runtime.js`

The same bundled JS will be used to serve to your client! We will use browserify's exposed require function to expose modules 'app' and 'render' and invoke the render functions.

(You have to have browserify globally installed: `npm install -g browserify`)

### Results
Roundtime on server: (without any form of memoization)  
 - non-minified runtime js: 114ms

## Memoization
Memoization can speed up your application by caching module/props combinations. In the runtime app I included a simple decorater function testing this.  
The idea is to make a checksum of the props (or the object_list serialized to JSON) to prevent a Javascript call. I think it's a good way of caching for public web apps.

## Profiling
Simple profiling is included by adding the [django cprofile middleware](https://github.com/omarish/django-cprofile-middleware) by Omarish. By adding the ?prof parameter to URLs you can see the server roundtime.

Example:  
`checksum = hashlib.md5(props).hexdigest()`