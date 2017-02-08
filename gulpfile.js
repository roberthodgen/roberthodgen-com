var gulp = require('gulp');
var gulpUtil = require('gulp-util');
var webpack = require('webpack');
var vinylPaths = require('vinyl-paths');
var del = require('del');
var webpackConfig = require('./webpack.config');

var STATS_OPTIONS = {
    'colors': true
};

gulp.task('default', ['build']);

gulp.task('build', ['webpack']);

gulp.task('webpack', function (done) {
    var compiler = webpack(webpackConfig);

    compiler.run(function (err, stats) {
        if (err) {
            throw new gulpUtil.PluginError('webpack', err);
        }

        gulpUtil.log("[webpack]", stats.toString(STATS_OPTIONS));
        done();
    });
});

gulp.task('clean', function () {
    return gulp.src(['./roberthodgen-com-server/dist/*', '!.gitignore'])
        .pipe(vinylPaths(del));
});
