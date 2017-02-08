module.exports = {
  entry: [
    './roberthodgen-com-webapp/app.js'
  ],
  output: {
    filename: 'bundle.js',
    path: './roberthodgen-com-server/dist/'
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
          'resolve-url-loader',
          'postcss-loader',
          'sass-loader'
        ]
      },
      {
        test: /\.css$/,
        loaders: [
          'style-loader',
          'css-loader',
          'resolve-url-loader'
        ]
      },
      {
        test: /\.jpg$/,
        loaders: [
          'file-loader'
        ]
      }
    ]
  },
  plugins: []
};
