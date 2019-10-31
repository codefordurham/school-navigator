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
