import {fileURLToPath, URL} from 'node:url'
import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'
// https://vitejs.dev/config/
export default defineConfig({
    plugins: [vue(),],
    resolve: {
        alias: {
            '@': fileURLToPath(new URL('./src', import.meta.url))
        }
    },
  //跨域解决
    server: {
        //port: 4500,
        proxy: {
            '/api': {
                target: 'http://127.0.0.1:8000/api/',
                changeOrigin: true,
                rewrite: (path) => path.replace(/^\/api/, ""),
            },
        },
     //   host: '0.0.0.0'
    },
})
