import gulp from 'gulp';
import gulpSass from 'gulp-sass';
import * as dartSass from 'sass';
import uglify from 'gulp-uglify';
import postcss from 'gulp-postcss';
import cssnano from 'cssnano';
import rename from 'gulp-rename';


export function styles() {
    return gulp.src('frontend/src/styles/*.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(postcss([cssnano()]))
        .pipe(rename('style.css'))
        .pipe(gulp.dest('./dist/css'))
        .pipe(gulp.dest('setup/static/styles'));
}
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



export const build = gulp.parallel(styles, scripts, html);

export function watch() {
    gulp.watch('frontend/src/styles/*.scss', styles);
    gulp.watch('frontend/src/scripts/*.js', scripts);
    gulp.watch('frontend/src/index.html', html);
}