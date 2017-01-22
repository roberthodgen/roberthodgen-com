module.exports = {
  entry: [
    './app/app.js'
  ],
  output: {
    filename: 'bundle.js',
    path: './dist'
  },
  module: {
    loaders: [
      {
        test: /app\.html/,
        loaders: [
          "file-loader?name=[name].[ext]"
        ]
      },
      {
        test: /\.html$/,
        exclude: /app\.html/,
        loaders: [
          "html-loader"
        ]
      },
      {
        test: /\.js$/,
        exclude: /(node_modules|bower_components)/,
        loaders: [
          'ng-annotate-loader',
          'babel-loader?presets[]=es2015'
        ]
      },
      {
        test: /\.scss$/,
        loaders: [
          'style-loader',
          'css-loader',
          'postcss-loader',
          'sass-loader'
        ]
      },
      {
        test: /\.css$/,
        loaders: [
          'style-loader',
          'css-loader'
        ]
      }
    ]
  },
  plugins: []
};
