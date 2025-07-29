import gulp from 'gulp';
import gulpSass from 'gulp-sass';
import * as dartSass from 'sass';
import imagemin from 'gulp-imagemin';
import uglify from 'gulp-uglify';

const sass = gulpSass(dartSass);

export function scripts() {
    return gulp.src('frontend/src/scripts/*.js')
        .pipe(uglify())
        .pipe(gulp.dest('./dist/js'));
}

export function html() {
    return gulp.src('frontend/src/index.html')
        .pipe(gulp.dest('./dist'));
}

export function styles() {
    return gulp.src('frontend/src/styles/*.scss')
        .pipe(sass({ outputStyle: 'compressed' }))
        .pipe(gulp.dest('./dist/css'));
}

export const build = gulp.parallel(styles, scripts, html);

export function watch() {
    gulp.watch('frontend/src/styles/*.scss', styles);
    gulp.watch('frontend/src/scripts/*.js', scripts);
    gulp.watch('frontend/src/index.html', html);
}