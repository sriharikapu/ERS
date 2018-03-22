'use strict';

const gulp        = require('gulp');
const del         = require('del');
const util        = require('gulp-util');
const sass        = require('gulp-sass');
const prefixer    = require('gulp-autoprefixer');
const uglify      = require('gulp-uglify');
const concat      = require('gulp-concat');
const rename      = require('gulp-rename');
const handlebars  = require('gulp-compile-handlebars');
const browserSync = require('browser-sync');
const ghPages     = require('gulp-gh-pages');
const sassGlob    = require('gulp-sass-bulk-import');
const watch       = require('gulp-watch');
const babel       = require('gulp-babel');
var exec = require('child_process').exec;

var paths = {
  src: { root: 'API' },
  dist: { root: 'dist' },
  init: function() {
    this.src.wallet_sass = this.src.root + '/static/scss/*.scss';
    this.src.scripts     = this.src.root + '/static/js/*.js'
    this.src.templates   = this.src.root + '/templates/*.html';

    this.src.files       = this.src.root + '/*.{html,txt,xml}';
    this.dist.css        = this.dist.root + '/css';
    return this;
  },
}.init();

gulp.task('default', ['wallet-sass', 'templates', 'scripts', 'watch']);

gulp.task('wallet-sass', (done) => {
  gulp.src(paths.src.root + '/static/scss/*.scss')
    .pipe(sass({
      errLogToConsole: true,
    }))
    .pipe(gulp.dest(paths.src.root + '/static/scss'))
    .on('end', done);
});

gulp.task('templates', (done) => {
  gulp.src([paths.src.root + '/templates/*.html'])
    .pipe(gulp.dest(paths.dist.root))
    .on('end', done)
});

gulp.task('scripts', (done) => {
  gulp.src([paths.src.root + '/static/js/*.js'])
    .pipe(gulp.dest(paths.dist.root + '/static/js'))
    .on('end', done)
});

gulp.task('watch', () => {
  gulp.watch(paths.src.scripts, ['scripts',]);
  gulp.watch(paths.src.wallet_sass, ['wallet-sass',]);
  gulp.watch(paths.src.templates, ['templates',]);
});
