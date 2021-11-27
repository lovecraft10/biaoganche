const path = require('path')
const resolve = dir => {
    return path.join(__dirname, dir)
}
const port = process.env.port || process.env.npm_config_port || 80 // 端口
module.exports = {
    publicPath: './',
    devServer: {
        host: '0.0.0.0',
        port: port,
        open: true,
        proxy: {
            // detail: https://cli.vuejs.org/config/#devserver-proxy
            [process.env.VUE_APP_BASE_API]: {
                target: `http://127.0.0.1:5000`,
                changeOrigin: true,
                pathRewrite: {
                    ['^' + process.env.VUE_APP_BASE_API]: ''
                }
            }
        },
        disableHostCheck: true
    },
    chainWebpack: config => {
        config.resolve.alias
            .set('_c', resolve('src/components')) // key,value自行定义，比如.set('@@', resolve('src/components'))
    },
}
