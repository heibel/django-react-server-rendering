var gulp = require('gulp'),
    browserify = require('browserify'),
    source = require('vinyl-source-stream'),
    reactify = require('reactify'),
    watchify = require('watchify');

function react(watch) {
    var bundler, rebundle;

    bundler = browserify('./router/jsx/app.js', {
        basedir: __dirname,
        debug: false,
        cache: {}, // required for watchify
        packageCache: {}, // required for watchify
        fullPaths: watch // required to be true only for watchify
    });

    if (watch) {
        bundler = watchify(bundler)
    }

    bundler.transform(reactify);

    rebundle = function() {
        var stream = bundler.bundle();
        stream.on('error', function(err) {
            console.error(err.message);
        });
        stream = stream.pipe(source('router.js'));

        return stream
            .pipe(gulp.dest('./router/static/js/'))
    };
    bundler.on('update', rebundle);

    return rebundle();
}

gulp.task('react', function() {
   react(false);
});

