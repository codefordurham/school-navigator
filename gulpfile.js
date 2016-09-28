'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');

gulp.task('sass', function () {
  return gulp.src('./frontend/sass/*.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('./frontend/css'));
});

gulp.task('sass:watch', function () {
  gulp.watch('./frontend/sass/*.scss', ['sass']);
});

// var cssTask = function () {
//     var lessOpts = {
//       relativeUrls: true,
//     };
//     if (options.development) {
//       var run = function () {
//         var start = Date.now();
//         console.log('Building CSS bundle');
//         return gulp.src(options.css.src)
//           .pipe(gulpif(options.development, livereload()))
//           .pipe(concat('index.less'))
//           .pipe(less(lessOpts))
//           .pipe(rename('bundle.css'))
//           .pipe(gulp.dest(options.css.dest))
//           .pipe(notify(function () {
//             console.log('CSS bundle built in ' + (Date.now() - start) + 'ms');
//           }));
//       };
//       gulp.watch(options.css.watch, run);
//       return run();
//     } else {
//       return gulp.src(options.css.src)
//         .pipe(concat('index.less'))
//         .pipe(less(lessOpts))
//         .pipe(rename('bundle.css'))
//         .pipe(cssmin())
//         .pipe(gulp.dest(options.css.dest));
//     }
// };
// gulp.task('css', cssTask);
