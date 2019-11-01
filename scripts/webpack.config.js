import { resolve } from 'path';
import { HotModuleReplacementPlugin } from 'webpack';
import HtmlWebpackPlugin from 'html-webpack-plugin';
import deepmerge from 'deepmerge';

import config from '../package.json';

const PACKAGE_NAME = 'moods-react-docs';
const APP = 'app';
const BUILD_DIR = 'dist';
const NODE_MODULES = 'node_modules';

const APP_ROOT = resolve(__dirname, '..', APP)

export default function (_, { mode = 'development' }) {
    return ({
        mode,
        entry: [
            resolve(APP_ROOT, 'index.jsx'),
        ],
        output: {
            filename: 'app.js',
            path: resolve(__dirname, '..', BUILD_DIR),
            publicPath: '/',
        },
        resolve: {
            extensions: ['.js', '.jsx', 'json'],
        },
        module: {
            rules: [
                {
                    test: /\.jsx?$/,
                    exclude: /node_modules/,
                    use: {
                        loader: 'babel-loader',
                        options: deepmerge(config.babel, {
                            plugins: ['react-hot-loader/babel'],
                        }),
                    },
                },
            ],
        },
        plugins: [
            new HotModuleReplacementPlugin(),
            new HtmlWebpackPlugin({ template: resolve(APP_ROOT, 'index.html') }),
        ],
        devServer: {
            port: 3000,
            hot: true,
            host: '0.0.0.0',
            contentBase: resolve(process.cwd(), APP),
            historyApiFallback: true,
        },
    });
}